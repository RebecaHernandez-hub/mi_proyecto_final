import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('instance/mi_base.db')
cursor = conn.cursor()

# Insertar usuarios
cursor.execute("INSERT INTO usuario (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Ana_Lopez", "ana@example.com", "1234"))
cursor.execute("INSERT INTO usuario (nombre, correo, contraseña) VALUES (?, ?, ?)", ("JuanPerez", "juan@example.com", "5678"))
cursor.execute("INSERT INTO usuario (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Maria99", "maria@example.com", "abcd"))

# Obtener los IDs insertados
conn.commit()
cursor.execute("SELECT id FROM usuario WHERE nombre = 'Ana_Lopez'")
id_ana = cursor.fetchone()[0]
cursor.execute("SELECT id FROM usuario WHERE nombre = 'JuanPerez'")
id_juan = cursor.fetchone()[0]
cursor.execute("SELECT id FROM usuario WHERE nombre = 'Maria99'")
id_maria = cursor.fetchone()[0]

# Insertar preguntas
cursor.execute("INSERT INTO preguntas (titulo, contenido, usuarios_id) VALUES (?, ?, ?)",
               ("¿Cómo resolver un sistema de ecuaciones con matrices?", "Estoy atorada con matrices.", id_ana))
cursor.execute("INSERT INTO preguntas (titulo, contenido, usuarios_id) VALUES (?, ?, ?)",
               ("¿Qué es una API REST y cómo funciona?", "¿Me pueden explicar qué es una API?", id_juan))
cursor.execute("INSERT INTO preguntas (titulo, contenido, usuarios_id) VALUES (?, ?, ?)",
               ("¿Cuál es la diferencia entre una variable local y global?", "Tengo duda con variables.", id_maria))

# Obtener IDs de preguntas
conn.commit()
cursor.execute("SELECT id FROM preguntas WHERE titulo LIKE '%ecuaciones%'")
id_p1 = cursor.fetchone()[0]
cursor.execute("SELECT id FROM preguntas WHERE titulo LIKE '%API REST%'")
id_p2 = cursor.fetchone()[0]
cursor.execute("SELECT id FROM preguntas WHERE titulo LIKE '%variable local%'")
id_p3 = cursor.fetchone()[0]

# Insertar respuestas
cursor.execute("INSERT INTO respuestas (contenido, usuarios_id, pregunta_id) VALUES (?, ?, ?)",
               ("Primero debes convertir la matriz a su forma escalonada.", id_juan, id_p1))
cursor.execute("INSERT INTO respuestas (contenido, usuarios_id, pregunta_id) VALUES (?, ?, ?)",
               ("Una API REST funciona sobre HTTP y usa métodos como GET y POST.", id_maria, id_p2))
cursor.execute("INSERT INTO respuestas (contenido, usuarios_id, pregunta_id) VALUES (?, ?, ?)",
               ("Una variable local vive dentro de una función, la global vive fuera.", id_ana, id_p3))

conn.commit()
conn.close()

print("✅ Datos de prueba insertados correctamente.")
