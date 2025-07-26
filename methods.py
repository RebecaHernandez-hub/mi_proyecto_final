from flask_jwt_extended import create_access_token
from datetime import datetime
from models import Usuario

# -----------------------------
# Crear una cuenta nueva
# -----------------------------
def crear_cuenta(nombre, correo, password):
    usuario_existente = Usuario.query.filter_by(correo=correo).first()

    if usuario_existente:
        print('❌ El correo ya existe en la base de datos')
        return {'status': 'error', 'error': 'La cuenta ya está registrada'}

    nuevo_usuario = Usuario(
        nombre=nombre,
        correo=correo,
        created_at=datetime.utcnow()
    )
    nuevo_usuario.hashear_password(password_original=password)
    nuevo_usuario.save()

    print('✅ Usuario creado correctamente')
    return {'status': 'ok', 'email': correo}

# -----------------------------
# Iniciar sesión
# -----------------------------
def iniciar_sesion(correo, password):
    usuario = Usuario.query.filter_by(correo=correo).first()

    if not usuario:
        print('❌ La cuenta no existe')
        return {'status': 'error', 'error': 'La cuenta no existe'}

    if usuario.verificar_password(password_plano=password):
        print('✅ Inicio de sesión exitoso')
        token_acceso = create_access_token(identity=usuario.nombre)
        return {'status': 'ok', 'token': token_acceso}
    else:
        print('❌ Contraseña incorrecta')
        return {'status': 'error', 'error': 'Contraseña incorrecta'}
