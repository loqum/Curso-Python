import sqlite3

NAME_DB = 'C:/Users/ruben/OneDrive/Python/ejemplo.db'
NAME_TABLE = "Trabajadores"
LISTA_TRABAJADORES = [(1, "Jaime", 30), (2, "Esteban", 24), (3, "Marta", 22), (4, "Gonzalo", 56),
                      (5, "Lucia", 45), (6, "David", 56), (7, "Sandra", 34), (8, "Marcos", 29)]


def get_connection(name_db):
    return sqlite3.connect(NAME_DB)


def create_table(cursor, name_table):
    cursor.execute("create table if not exists " +
                   name_table + "(id INT, nombre TEXT, edad INT)")


def insert_table(connection, cursor, name_table, lista_items):
    for item in lista_items:
        cursor.execute("INSERT INTO " + name_table + " VALUES (?, ?, ?)", item)
    connection.commit()


def show_by_col(cursor, name_table, col, item_col):
    return cursor.execute("SELECT * FROM " + name_table + " WHERE " + col + " = '" + item_col + "'").fetchall()


def show_all_table(cursor, name_table):
    return cursor.execute("SELECT * FROM " + name_table).fetchall()


db_connection = get_connection(NAME_DB)
db_cursor = db_connection.cursor()

#create_table(db_cursor, NAME_TABLE)
#insert_table(db_connection, db_cursor, NAME_TABLE, LISTA_TRABAJADORES)

print(show_all_table(db_cursor, NAME_TABLE))
print(show_by_col(db_cursor, NAME_TABLE, "edad", "56"))
print(show_by_col(db_cursor, NAME_TABLE, "nombre", "David"))
