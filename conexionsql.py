import mariadb
import sys


try:
    conn = mariadb.connect(
        user="root",
        password="CoCo2528",
        host="localhost",
        port=3306,
        database="control_asistencia"

    )
    print("Conexión exitosa")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
