#!/usr/bin/python3
""" flask module """
from models.state import State
from flask import Flask
fro, flask import session
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def _teardown_(session):
    """tears sown current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def listing_states():
    """lists all states"""
    from models.state import State
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
