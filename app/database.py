import sqlite3
from peewee import AutoField, CharField, DateTimeField, SqliteDatabase, Model
import datetime

db = SqliteDatabase("database.db")


class Todo(Model):
    current_time = datetime.datetime.now
    id = AutoField()
    todo_message = CharField()
    date_created = DateTimeField(default=current_time)
    date_updated = DateTimeField(default=current_time)

    class Meta:
        database = db


# make sure table is good
def setup_table():
    db.connect()
    db.create_tables([Todo])
    db.close()


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
