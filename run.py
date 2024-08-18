#!/usr/bin/python3
""" This module contains the script to run my flask app """
from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
