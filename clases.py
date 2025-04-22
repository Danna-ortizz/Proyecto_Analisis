
from conexionsql import cur
from datetime import datetime

class asistencias:
    def registrar_asistencia(self, id_usuario, id_materia, fecha=None, hora=None, asistencia=0):
        if fecha is None:
            fecha = datetime.now().date()
        if hora is None:
            hora = datetime.now().time()
        sql = """INSERT INTO Asistencias (id_usuario, id_materia, fecha, hora, asistencia)
                 VALUES (%s,%s,%s,%s,%s)"""
        cur.execute(sql, (id_usuario, id_materia, fecha, hora, asistencia))
        cur.connection.commit()

    def obtener_asistencias_alumno_id(self, id_usuario):
        sql = """SELECT * FROM asistencias WHERE id_usuario=%s"""
        cur.execute(sql, (id_usuario,))
        return cur.fetchall()

class usuarios:
    def obtener_todos_usuarios(self):
        cur.execute("SELECT id_usuario, usuario, nombre, contraseña, tipo FROM Usuarios")
        return cur.fetchall()

    def validar_credenciales(self, usuario, contraseña):
        cur.execute("SELECT tipo FROM Usuarios WHERE usuario=%s AND contraseña=%s", (usuario, contraseña))
        return cur.fetchone()

    def obtener_usuarios_nombre_id(self, id_usuario):
        cur.execute("SELECT nombre FROM Usuarios WHERE id_usuario=%s", (id_usuario,))
        return cur.fetchone()

class materias:
    def obtener_materias(self):
        cur.execute(""" SELECT * FROM Materias""")
        return cur.fetchall()

    def obtener_materias_nombre(self):
        cur.execute("SELECT nombre FROM Materias")
        return [m[0] for m in cur.fetchall()]

    def obtener_materias_id_nombre(self, nombre):
        cur.execute("SELECT id_materia FROM Materias WHERE nombre=%s", (nombre,))
        row = cur.fetchone()
        return row[0] if row else None

class grupos:
    def obtener_grupo(self):
        cur.execute("SELECT * FROM Grupos")
        return cur.fetchall()

class alumno(usuarios):
    def obtener_alumno(self):
        cur.execute("SELECT * FROM Usuarios WHERE tipo='alumno'")
        return cur.fetchall()

    def obtener_alumno_nombre(self):
        cur.execute("SELECT nombre FROM Usuarios WHERE tipo='alumno'")
        return [a[0] for a in cur.fetchall()]

    def obtener_alumno_id_nombre(self, nombre):
        cur.execute("SELECT id_usuario FROM Usuarios WHERE nombre=%s AND tipo='alumno'", (nombre,))
        row = cur.fetchone()
        return row[0] if row else None

class admin:
    def crear_usuario(self, usuario, contraseña, nombre, tipo):
        cur.execute("INSERT INTO Usuarios(usuario, contraseña, nombre, tipo) VALUES (%s,%s,%s,%s)",
                    (usuario, contraseña, nombre, tipo))
        cur.connection.commit()

    def modificar_usuario(self, id_usuario, usuario, contraseña, nombre, tipo):
        cur.execute("""UPDATE Usuarios SET usuario=%s, contraseña=%s, nombre=%s, tipo=%s WHERE id_usuario=%s""",
                    (usuario, contraseña, nombre, tipo, id_usuario))
        cur.connection.commit()

    def eliminar_usuario(self, id_usuario):
        cur.execute("DELETE FROM Usuarios WHERE id_usuario=%s", (id_usuario,))
        cur.connection.commit()

    def crear_materia(self, nombre, id_grupo, id_docente):
        cur.execute("INSERT INTO Materias(nombre, id_grupo, id_docente) VALUES (%s,%s,%s)",
                    (nombre, id_grupo, id_docente))
        cur.connection.commit()

    def modificar_materia(self, id_materia, nombre, id_grupo, id_docente):
        cur.execute("""UPDATE Materias SET nombre=%s, id_grupo=%s, id_docente=%s WHERE id_materia=%s""",
                    (nombre, id_grupo, id_docente, id_materia))
        cur.connection.commit()

    def eliminar_materia(self, id_materia):
        cur.execute("DELETE FROM Materias WHERE id_materia=%s", (id_materia,))
        cur.connection.commit()

    def crear_grupo(self, id_grupo, nombre, periodo, id_docente):
        cur.execute("INSERT INTO Grupos(id_grupo, nombre, periodo_academico, id_docente) VALUES (%s,%s,%s,%s)",
                    (id_grupo, nombre, periodo, id_docente))
        cur.connection.commit()

    def modificar_grupo(self, id_grupo, nombre, periodo,id_docente):
        cur.execute("""UPDATE Grupos SET nombre=%s, periodo_academico=%s, id_docente=%s WHERE id_grupo=%s""",
                    (nombre, periodo, id_docente, id_grupo))
        cur.connection.commit()

    def eliminar_grupo(self, id_grupo):
        cur.execute("DELETE FROM Grupos WHERE id_grupo=%s", (id_grupo,))
        cur.connection.commit()