#!/usr/bin/python3
"""initialises web flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def _route_index_():
    """returns the first stipulated text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def _route_hbnb_():
    """returns second stipulated text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def _route_c_is_fun_text(text):
    """returns third stipulated text"""
    _new_text_one_ = text.replace('_', ' ')
    return 'C {}'.format(_new_text_one_)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """returns fourth stipulated text"""
    _new_text_two_ = text.replace('_', ' ')
    return 'Python {}'.format(_new_text_two_)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
