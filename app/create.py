import datetime

from bottle import get, post, template, request, redirect
from app.database import void_execute


@get("/create")
def create():
    return template("create")


@post("/insert")
def insert():
    message_to_insert = request.forms.get("message").strip()
    current_time = datetime.datetime.now()
    void_execute(
        "insert into todo (todo_message, date_created, date_updated) values (?, ?, ?)",
        [message_to_insert, current_time,  current_time])
    redirect("/create")
