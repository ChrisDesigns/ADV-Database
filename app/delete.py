from bottle import get, post, template, request


@get("/delete")
def delete():
    return template("update")


@get("/remove/<id:int>")
@post("/remove")
def remove(id=-1):
    index = id if id >= 0 else int(request.forms.get("id").strip())
    return "The ID to remove is [" + str(index) + "]..."
