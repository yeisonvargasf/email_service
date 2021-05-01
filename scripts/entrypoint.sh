#!/bin/bash


if [[ $DEPLOYMENT_PLATFORM == "heroku" ]]; then
    if [[ $PROCESS_TYPE == "web" ]]; then
        # Do a db revision upgrade as it is idempotent
        flask db upgrade $DB_REVISION

        gunicorn --config "python:config.gunicorn"
    fi
elif [[ $DEPLOYMENT_PLATFORM == "local" ]]; then
    if [[ $PROCESS_TYPE == "web" ]]; then
        gunicorn --config "python:config.gunicorn"
    fi
fi
