#!/bin/sh
export FLASK_APP=./app/main.py
flask --debug run -h 0.0.0.0 --port 8888