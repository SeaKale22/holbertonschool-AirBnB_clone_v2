#!/usr/bin/python3
"""Simple Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

# create flask app
app = Flask(__name__)


# route for /
@app.route('/states_list', strict_slashes=False)
def states_list():
    """Shows html of states list"""
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda state:state.name)
    return render_template('states_list.html', states=states_sorted)


@app.teardown_appcontext
def teardown_storage(exception):
    """teardown method"""
    storage.close()


# run app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
