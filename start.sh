#!/usr/bin/env bash

if [[ "$PYTHON_ENV" = "production" ]]
then
    waitress-serve --call 'server:create_app'
else
    export FLASK_APP=./app/main.py
    flask --debug run -h 0.0.0.0 --port 8080
fi
