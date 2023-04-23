#!/usr/bin/python3
"""this loads flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def _route_hello_():
    """returns the sstipulated text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def _route_hbnb_():
    """returns second stipulated text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def _route_c_is_fun_text(text):
    """Displays 'C' followed by the value of the text variable"""
    new_text = text.replace('_', ' ')
    return 'C %s' % new_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
