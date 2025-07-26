import sqlite3

# Ruta a tu base de datos local
conn = sqlite3.connect('instance/mi_base.db')
cursor = conn.cursor()

# Crear tabla: usuario
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Crear tabla: preguntas
cursor.execute('''
CREATE TABLE IF NOT EXISTS preguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    contenido TEXT,
    fecha_creacion DATE DEFAULT CURRENT_DATE,
    usuarios_id INTEGER,
    FOREIGN KEY (usuarios_id) REFERENCES usuario(id)
)
''')

# Crear tabla: respuestas
cursor.execute('''
CREATE TABLE IF NOT EXISTS respuestas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contenido TEXT,
    fecha_respuesta DATE DEFAULT CURRENT_DATE,
    usuarios_id INTEGER,
    pregunta_id INTEGER,
    FOREIGN KEY (usuarios_id) REFERENCES usuario(id),
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(id)
)
''')

conn.commit()
conn.close()

print("✅ ¡Tablas creadas correctamente en mi_base.db!")
