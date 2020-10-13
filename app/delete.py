from bottle import get, post, template, request, redirect
from app.database import void_execute


@get("/delete")
def delete():
    return template("delete")


@get("/remove/<id:int>")
@post("/remove")
def remove(id=-1):
    index = id if id >= 0 else int(request.forms.get("id").strip())
    void_execute("delete from todo where id=?", [index])
    redirect("/delete")
