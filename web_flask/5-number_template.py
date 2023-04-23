#!/usr/bin/python3
"""initialises web flask"""
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def _route_index_():
    """returns first stipulated text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def _route_hbnb_():
    """returns second stipulated text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def _route_c_is_fun_text_(text):
    """returns third stipulated text"""
    _new_text_one_ = text.replace('_', ' ')
    return 'C {}'.format(_new_text_one_)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def _route_python_is_cool_text_(text="is cool"):
    """returns fourth stipulated text plus format"""
    _new_text_two_ = text.replace('_', ' ')
    return 'Python {}'.format(_new_text_two_)


@app.route('/number/<n>', strict_slashes=False)
def _route_number_(n):
    """returns fifth stipulated text plus format"""
    return "%i is a number" % n


@app.route('/number_template/<n>', strict_slashes=False)
def _route_number_template_(n):
    """returns sixth stipulated text plus format"""
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
