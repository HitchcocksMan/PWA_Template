from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import database_manager as dbHandler
import json
import os


app = Flask(__name__)


@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("/index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


def index():
    data = dbHandler.listExtension()
    return render_template("/index.html", content=data)
