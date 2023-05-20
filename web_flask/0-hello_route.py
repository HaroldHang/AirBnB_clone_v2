#!/usr/bin/python3
"""
Start a flask application
Listen on port 5000
"""

from flask import Flask

app = Flask(__name__)

@app.route("/airbnb-onepage", strict_slashes=False)
def hello_hbnb():
    """ Display the hello hbnb """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")