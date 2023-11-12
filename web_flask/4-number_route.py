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


# route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """returns C + text"""
    # create string
    start_str = 'C {}'.format(text)
    # replace underscores in text
    start_str = start_str.replace("_", " ")
    return start_str


# route for /python/<text>
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_text(text='is cool'):
    """returns Python + text"""
    # create string
    start_str = 'Python {}'.format(text)
    # replace underscores in text
    start_str = start_str.replace("_", " ")
    return start_str


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Says if n is a number"""
    return '{} is a number'.format(n)


# run app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
