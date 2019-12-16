import sqlite3

NAME_DB = 'C:/Users/ruben/OneDrive/Python/ejemplo.db'
NAME_TABLE = "Animales"


def get_connection(name_db):
    return sqlite3.connect(NAME_DB)


def show_by_nombre(cursor, name_table):
    return cursor.execute("SELECT Nombre FROM " + name_table).fetchall()


def show_by_especie(cursor, name_table):
    return cursor.execute("SELECT Especie FROM Animales")


def insert_item(connection, cursor, name_table, item):
    cursor.execute("INSERT INTO " + name_table + " VALUES (" + item + ")")
    connection.commit()


db_connection = get_connection(NAME_DB)
db_cursor = db_connection.cursor()

#insert_item(db_connection, db_cursor, NAME_TABLE, "16, 'Rayo', 'Gato'")
print(show_by_nombre(db_cursor, NAME_TABLE))
print(show_by_especie(db_cursor, NAME_TABLE).fetchall()[-1])

db_connection.close()
