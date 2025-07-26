# Este archivo nos ayudará a evitar las importaciones circulares

# Objeto para manejar la base de datos
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Objeto para manejar los JWT (tokens de sesión)
from flask_jwt_extended import JWTManager
jwt = JWTManager()
