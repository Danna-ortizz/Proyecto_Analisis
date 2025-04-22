from conexionsql import cur
from datetime import datetime

# Clase asistencias
class asistencias:
    def __init__(self):
        pass

    # Usada en interfaz_alumno.py e interfaz_docente.py
    def registrar_asistencia(self, id_usuario, id_materia, fecha=None, hora=None, asistencia=0):
        if fecha is None:
            fecha = datetime.now().date()
        if hora is None:
            hora = datetime.now().time()

        sql = """INSERT INTO Asistencias (id_usuario, id_materia, fecha, hora, asistencia) 
                 VALUES (%s, %s, %s, %s, %s)"""
        cur.execute(sql, (id_usuario, id_materia, fecha, hora, asistencia))
        cur.connection.commit()

    # Usada en interfaz_alumno.py para mostrar las asistencias del alumno
    def obtener_asistencias_alumno_id(self, id_usuario):
        sql = """
            SELECT Asistencias.id_usuario, Usuarios.nombre, Asistencias.id_materia, Materias.nombre,
                   Asistencias.fecha, Asistencias.hora, Asistencias.asistencia
            FROM Asistencias
            JOIN Usuarios ON Asistencias.id_usuario = Usuarios.id_usuario
            JOIN Materias ON Asistencias.id_materia = Materias.id_materia
            WHERE Asistencias.asistencia = 1
              AND Asistencias.id_usuario = %s
        """
        cur.execute(sql, (id_usuario,))
        return cur.fetchall()

# Clase usuarios
class usuarios:
    def __init__(self):
        pass

    # Usada en interfaz_admin.py (para mostrar todos los usuarios)
    def obtener_todos_usuarios(self):
        sql = "SELECT id_usuario, usuario, nombre, contraseña, tipo FROM Usuarios"
        cur.execute(sql)
        return cur.fetchall()

    # Usada en interfaz_login.py (para validar credenciales)
    def validar_credenciales(self, usuario, contraseña):
        sql = """SELECT tipo FROM Usuarios WHERE usuario = %s AND contraseña = %s"""
        cur.execute(sql, (usuario, contraseña))
        tipo_usuario = cur.fetchone()
        return tipo_usuario

    # Usada en interfaz_docente.py (para mostrar el nombre, dado el ID)
    def obtener_usuarios_nombre_id(self, nombre):
        sql = "SELECT nombre FROM Usuarios WHERE id_usuario = %s"
        cur.execute(sql, (nombre,))
        return cur.fetchall()

# Clase materias

class materias:
    def __init__(self):
        pass

    # Usada en interfaz_admin.py (para mostrar la tabla de materias)
    def obtener_materias(self):
        sql = """
            SELECT Materias.id_materia, Materias.nombre, Materias.id_grupo, Grupos.nombre,
                   Materias.id_docente, Usuarios.nombre
            FROM Materias
            JOIN Grupos ON Materias.id_grupo = Grupos.id_grupo
            JOIN Usuarios ON Materias.id_docente = Usuarios.id_usuario
        """
        cur.execute(sql)
        return cur.fetchall()

    # Usada en interfaz_alumno.py e interfaz_docente.py (para poblar el combobox de materias)
    def obtener_materias_nombre(self):
        sql = """
            SELECT Materias.nombre
            FROM Materias
            JOIN Grupos ON Materias.id_grupo = Grupos.id_grupo
            JOIN Usuarios ON Materias.id_docente = Usuarios.id_usuario
        """
        cur.execute(sql)
        materias = cur.fetchall()
        return [materia[0] for materia in materias]

    # Usada en interfaz_alumno.py e interfaz_docente.py (para convertir nombre de materia en su ID)
    def obtener_materias_id_nombre(self, nombre):
        sql = """
            SELECT Materias.id_materia
            FROM Materias
            JOIN Grupos ON Materias.id_grupo = Grupos.id_grupo
            JOIN Usuarios ON Materias.id_docente = Usuarios.id_usuario
            WHERE Materias.nombre = %s
        """
        cur.execute(sql, (nombre,))
        fila = cur.fetchone()
        return fila[0] if fila else None

# Clase grupos
class grupos:
    def __init__(self):
        pass

    # Usada en interfaz_admin.py (para mostrar la tabla de grupos)
    def obtener_grupo(self):
        sql = "SELECT * FROM Grupos"
        cur.execute(sql)
        return cur.fetchall()
    
 

# Clase alumno (hereda de usuarios)
class alumno(usuarios):
    def __init__(self):
        pass

    # Usada en interfaz_docente.py (para mostrar todos los alumnos)
    def obtener_alumno(self):
        sql = "SELECT * FROM Usuarios WHERE tipo = 'alumno'"
        cur.execute(sql)
        return cur.fetchall()

    # Usada en interfaz_docente.py (para poblar el combobox de alumnos)
    def obtener_alumno_nombre(self):
        sql = "SELECT nombre FROM Usuarios WHERE tipo = 'alumno'"
        cur.execute(sql)
        alumnos = cur.fetchall()
        return [alumno[0] for alumno in alumnos]

    # Usada en interfaz_alumno.py e interfaz_docente.py (para convertir nombre de alumno a su ID)
    def obtener_alumno_id_nombre(self, nombre):
        sql = "SELECT id_usuario FROM Usuarios WHERE tipo = 'alumno' AND nombre = %s"
        cur.execute(sql, (nombre,))
        fila = cur.fetchone()
        return fila[0] if fila else None

class admin:
    def __init__(self):
        pass
        # Usada en interfaz_admin.py (para crear usuarios)
    def crear_usuario(usuario, contraseña, nombre, tipo):
        sql = """INSERT INTO Usuarios(usuario, contraseña, nombre, tipo) VALUES (%s, %s, %s, %s)"""
        cur.execute(sql, (usuario, contraseña, nombre, tipo))
        cur.connection.commit()
    # Usada en interfaz_admin.py (para modificar usuarios)
    def modificar_usuario(usuario, contraseña, nombre, tipo):
        sql = """UPDATE Usuarios SET usuario=%s, contraseña=%s, nombre=%s, tipo=%s WHERE usuario=%s"""
        cur.execute(sql, (usuario, contraseña, nombre, tipo, usuario))
        cur.connection.commit()
    # Usada en interfaz_admin.py (para eliminar usuarios)
    def eliminar_usuario(usuario):
        sql = """DELETE FROM Usuarios WHERE id_usuario=%s"""
        cur.execute(sql, (usuario,))
        cur.connection.commit()
       # Usada en interfaz_admin.py (para crear materias)
    def crear_materia(self, nombre_materia, id_grupo, id_docente):
        sql = """INSERT INTO Materias (nombre, id_grupo, id_docente)
                 VALUES (%s, %s, %s)"""
        cur.execute(sql, (nombre_materia, id_grupo, id_docente))
        cur.connection.commit()
             # Usada en interfaz_admin.py (para modificar materias)
    def modificar_materia(self, id_materia, nombre_materia, id_grupo, id_docente):
        sql = """UPDATE Materias
                 SET nombre = %s, id_grupo = %s, id_docente = %s
                 WHERE id_materia = %s"""
        cur.execute(sql, (nombre_materia, id_grupo, id_docente, id_materia))
        cur.connection.commit()
            # Usada en interfaz_admin.py (para eliminar materias)
    def eliminar_materia(self, id_materia):
        sql = "DELETE FROM Materias WHERE id_materia = %s"
        cur.execute(sql, (id_materia,))
        cur.connection.commit()
           # Usada en interfaz_admin.py (para crear grupos)
    def crear_grupo(self, nombre, periodo):
        sql = """INSERT INTO Grupos (nombre, periodo_academico) VALUES (%s, %s)"""
        cur.execute(sql, (nombre, periodo))
        cur.connection.commit()
    # Usada en interfaz_admin.py (para modificar grupos)
    def modificar_grupo(self, id_grupo, nombre, periodo):
        sql = """UPDATE Grupos SET nombre = %s, periodo_academico = %s WHERE id_grupo = %s"""
        cur.execute(sql, (nombre, periodo, id_grupo))
        cur.connection.commit()
    # Usada en interfaz_admin.py (para eliminar grupos)
    def eliminar_grupo(self, id_grupo):
        sql = "DELETE FROM Grupos WHERE id_grupo = %s"
        cur.execute(sql, (id_grupo,))
        cur.connection.commit()