#!/usr/bin/python3
"""WebFlask"""
from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_nflask():
    """Display the stipulated text"""
    return 'Hello HBNB!'


def start_app():
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print("There was an error initializing Flask: {}".format(e))


if __name__ == '__main__':
    start_app()

