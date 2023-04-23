#!/usr/bin/python3
""" flask module """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def _route_index_():
    """return stipulated text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def _route_hbnb_():
    """return second stipulated text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def _route_c_is_fun_text_(text):
    """return third stipulated text"""
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def _route_ptyhon_is_fun_(text="is_cool"):
    """return fourth stipulated text"""
    return 'python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def _route_number_(n):
    """return fifth stipulated text"""
    return "%i is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def _route_number_template_(n):
    """return sixth stipulated text"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def _route_odd_or_even_checker_(n):
    """checks odd or even value"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
