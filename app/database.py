import sqlite3


def connection_handler():
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


# execute with returns (IE select)
def return_execute(statement):
    result = {}
    connection = connection_handler()
    try:
        cursor = connection.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()
        cursor.close()
    except:
        print("failed to select data")
    return result


# execute with no returns  (IE insert or update)
def void_execute(statement):
    connection = connection_handler()
    try:
        cursor = connection.cursor()
        cursor.execute(statement)
        connection.commit()
        cursor.close()
    except:
        print("failed to execute")
