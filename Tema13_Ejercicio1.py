import sqlite3

NAME_TABLE = "Coches"


def get_connection(name_db):
    return sqlite3.connect(name_db)


def create_table(cursor, name_table):
    cursor.execute(name_table)


def insert_table(db_connection, cursor, name_table, item):
    cursor.execute("INSERT INTO " + name_table + " VALUES (" + item + ")")
    db_connection.commit()


def show_all_table(db_cursor, name_table):
    return db_cursor.execute("SELECT * FROM " + NAME_TABLE).fetchall()


def show_by_name(db_cursor, name_table, name_car):
    return db_cursor.execute("SELECT * FROM " + name_table + " WHERE Nombre = '" + name_car + "'").fetchall()


db_connection = get_connection('C:/Users/ruben/OneDrive/Python/ejemplo.db')
db_cursor = db_connection.cursor()

#create_table(db_cursor, "CREATE TABLE Coches (Id INT, Nombre TEXT, Precio INT)")
#insert_table(db_connection, db_cursor, "Coches", "1, 'Mercedes', 54000")

#print(show_all_table(db_cursor, NAME_TABLE))
#print(show_by_name(db_cursor, NAME_TABLE, "Mercedes"))

db_connection.close()
