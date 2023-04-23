#!/usr/bin/python3
"""WebFlask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_nflask():
    """Dispaly the stipulated text"""
    return 'Hello HBNB!'


def start_app():
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print("There was an error initializing flask {}".format(e))


if __name__ == '__main__':
    start_app()

