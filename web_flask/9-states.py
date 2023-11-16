#!/usr/bin/python3
"""Simple Flask web app"""
from flask import Flask, render_template
import models
from models import storage
from models.state import State

# create flask app
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Shows html of states"""
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Shows html of states by id"""
    state = storage.get("State", id)
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_storage(exception):
    """teardown method"""
    storage.close()


# run app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
