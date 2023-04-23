#!/usr/bin/python3
"""m_web_flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays stipulated text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns stipulated text"""
    return 'HBNB'


if __name__ == '__main__':
    # Start the Flask web application
    app.run(host='0.0.0.0', port=5000)
