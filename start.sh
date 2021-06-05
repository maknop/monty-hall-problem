#!/bin/sh

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt --upgrade

python3 src/main.py
