from bottle import get, post, template, request


@get("/create")
def create():
    return template("create")


@post("/insert")
def insert():
    message_to_insert = request.forms.get("message").strip()
    return "The new item is [" + message_to_insert + "]..."
