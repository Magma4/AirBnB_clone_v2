#!/usr/bin/python3
""" Test """

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """Test"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Test"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
