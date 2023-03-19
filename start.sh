#!/bin/sh
export FLASK_APP=./app/main.py
flask --debug run -h 0.0.0.0 --port 8080


# Todo: setup production
# https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/
