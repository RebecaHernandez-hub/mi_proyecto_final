from flask import render_template, request, redirect, url_for, make_response
from methods import crear_cuenta, iniciar_sesion
import sqlite3  # Importante para consultar la base de datos

def cargar_rutas(app):

    # Página principal
    @app.route('/')
    def pagina():
        return render_template('index.html')

    # Página de login
    @app.route('/login')
    def informacion_rebe():
        resultado = request.args.get('status')
        return render_template('login.html', estado=resultado)

    # Página de registro y procesar formulario
    @app.route('/signup', methods=['GET', 'POST'])
    def datos():
        if request.method == 'POST':
            nombre = request.form.get('name')
            correo = request.form.get('email')
            password = request.form.get('password')

            print(f'''
            Nombre: {nombre}
            Correo: {correo}
            Contraseña: {password}
            ''')

            respuesta_signup = crear_cuenta(nombre, correo, password)

            print(respuesta_signup)

            if respuesta_signup['status'] == 'error':
                return redirect(url_for('datos', status=respuesta_signup['status']))

            return redirect(url_for('pagina', status='ok'))

        # Si es GET
        resultado = request.args.get('status')
        return render_template('signup.html', estado=resultado)

    # Procesar formulario de inicio de sesión
    @app.route('/manipulacion', methods=['POST'])
    def manipular_datos():
        correo = request.form.get('email')
        password = request.form.get('password')

        print(f'''
        Correo: {correo}
        Contraseña: {password}
        ''')

        respuesta_login = iniciar_sesion(correo, password)

        if respuesta_login['status'] == 'error':
            return redirect(url_for('informacion_rebe', status=respuesta_login['status']))

        respuesta = make_response(redirect(url_for('pagina')))
        respuesta.set_cookie('access_token', respuesta_login['token'], secure=True, max_age=3600)
        return respuesta

    # Página de error
    @app.route('/error')
    def pantalla_error():
        return render_template('error.html')

    # ✅ Página: Mostrar preguntas desde la base de datos
    @app.route('/preguntas')
    def mostrar_preguntas():
        conn = sqlite3.connect('instance/mi_base.db')
        cursor = conn.cursor()

        # Consulta SQL con JOIN para obtener título, fecha, usuario y total de respuestas
        cursor.execute('''
            SELECT preguntas.id, preguntas.titulo, preguntas.fecha_creacion, usuario.nombre,
                   COUNT(respuestas.id) as total_respuestas
            FROM preguntas
            JOIN usuario ON preguntas.usuarios_id = usuario.id
            LEFT JOIN respuestas ON respuestas.pregunta_id = preguntas.id
            GROUP BY preguntas.id
            ORDER BY preguntas.fecha_creacion DESC
        ''')

        preguntas = cursor.fetchall()
        conn.close()

        # Convertimos los resultados a una lista de diccionarios
        preguntas_formateadas = [{
            'id': fila[0],
            'titulo': fila[1],
            'fecha': fila[2],
            'usuario': fila[3],
            'respuestas': fila[4]
        } for fila in preguntas]

        return render_template('mis_consultas.html', preguntas=preguntas_formateadas)
