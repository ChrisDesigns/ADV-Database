from bottle import get, template
from app.database import return_execute


@get("/read")
def read():
    result = return_execute("select * from todo")
    return template("read", rows=result)
