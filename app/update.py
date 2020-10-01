from bottle import get, post, template, request


@get("/update")
def update():
    return template("update")


@get("/overwrite/<id:int>/<message>")
@post("/overwrite")
def overwrite(id=-1, message=None):
    index = id if id >= 0 else int(request.forms.get("id").strip())
    new_message = message if message else request.forms.get("message").strip()
    return "The ID: [" + str(index) + "] is being update with [" + new_message + "]..."
