#!/bin/bash

# setup the database if needed
poetry run python create_db.py

# run the server
poetry run flask --app flask-app run --host=0.0.0.0