from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# -----------------------------
# MODELO: Usuario
# -----------------------------
class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.Text, nullable=False)

    # Relaciones
    preguntas = db.relationship('Pregunta', backref='usuario', lazy=True)
    respuestas = db.relationship('Respuesta', backref='usuario', lazy=True)

    def hashear_password(self, password_original):
        self.contraseña = generate_password_hash(password_original)

    def verificar_password(self, password_plano):
        return check_password_hash(self.contraseña, password_plano)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# -----------------------------
# MODELO: Pregunta
# -----------------------------
class Pregunta(db.Model):
    __tablename__ = 'preguntas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text, nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.Date, default=datetime.utcnow, nullable=False)

    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    # Relación con respuestas
    respuestas = db.relationship('Respuesta', backref='pregunta', lazy=True)


# -----------------------------
# MODELO: Respuesta
# -----------------------------
class Respuesta(db.Model):
    __tablename__ = 'respuestas'

    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha_respuesta = db.Column(db.Date, default=datetime.utcnow, nullable=False)

    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('preguntas.id'), nullable=False)
