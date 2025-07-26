# Flask es la librería que nos permite crear un servidor web
from flask import Flask

# Importamos la función que carga las rutas desde routes.py
from routes import cargar_rutas

# Importamos la base de datos y JWT desde extensions.py
from extensions import db, jwt

# Creamos la aplicación Flask
app = Flask(__name__)

# Clave secreta para sesiones y cookies seguras
app.secret_key = 'clave_super_secreta'

# Clave secreta para los tokens JWT
app.config['JWT_SECRET_KEY'] = 'clave_super_jwt'

# Configuramos la conexión con la base de datos (Supabase)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.cdhjxgcqmrfwmsdywgkj:MufLJeYUOo7rCLj7@aws-0-us-east-2.pooler.supabase.com:6543/postgres'

# Desactivamos el seguimiento de modificaciones (mejora el rendimiento)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos las extensiones con la app
db.init_app(app)
jwt.init_app(app)

# Cargamos las rutas definidas en routes.py
cargar_rutas(app)

# Iniciamos el servidor solo si este archivo se ejecuta directamente
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    app.run(port=8000, debug=True)

# puerto 8000: en este puerto serviremos la aplicación
# debug=True: reinicia automáticamente el servidor si detecta cambios



 #   MufLJeYUOo7rCLj7