#!/usr/bin/python3
"""Simple Flask web app"""
from flask import Flask, render_template
from models import storage

# create flask app
app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """teardown method"""
    storage.close()


# route for /
@app.route('/states_list', strict_slashes=False)
def states_list():
    """Shows html of states list"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('states_list.html', states=sorted_states)


# run app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
