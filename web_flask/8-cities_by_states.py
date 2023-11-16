#!/usr/bin/python3
"""Simple Flask web app"""
from flask import Flask, render_template
import models
from models import storage
from models.state import State

# create flask app
app = Flask(__name__)


# route for /
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Shows html of cities by state"""
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states_sorted)


@app.teardown_appcontext
def teardown_storage(exception):
    """teardown method"""
    storage.close()


# run app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
