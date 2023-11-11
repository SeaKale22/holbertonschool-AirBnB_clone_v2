#!/usr/bin/python3
"""Simple Flask web app"""
from flask import Flask

# create flask app
app = Flask(__name__)


# route for /
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns string"""
    return 'Hello HBNB!'


# route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


# run app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
