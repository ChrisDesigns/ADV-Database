import datetime

from bottle import get, post, template, request, redirect
from app.database import void_execute


@get("/update")
def update():
    return template("update")


@get("/overwrite/<id:int>/<message>")
@post("/overwrite")
def overwrite(id=-1, message=None):
    index = id if id >= 0 else int(request.forms.get("id").strip())
    new_message = message if message else request.forms.get("message").strip()
    current_time = datetime.datetime.now()
    void_execute(
        "update todo set todo_message=?, date_updated=? where id=?",
        [new_message, current_time, index])
    redirect("/update")
