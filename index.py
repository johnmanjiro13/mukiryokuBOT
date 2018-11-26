import os
from bottle import route, run


@route("/")
def index():
    return ""

run(host="0.0.0.0", port=int(os.getenv("ROOT", 5000)))
