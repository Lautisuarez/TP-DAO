import sqlite3


def connection_bd(consulta):
    try:
        conn = sqlite3.connect('bd.db')
        cursor = conn.cursor()

        cursor.execute(consulta)

        conn.commit()
    except:
        print("error BD")
    finally:
        cursor.close()
        conn.close()