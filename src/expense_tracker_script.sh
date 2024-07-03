#!/bin/bash

if ! type -P python3 >/dev/null;
then 
    echo "Error: Python3 isn't installed. Please follow the instructions to install Python3 at https://www.python.org/downloads/ and re run the script."
    exit 1
fi

if [ -d "venv" ]; then 
    echo "Virtual environment exists"
else
    echo "There is an error: Virtual environment does not exist. Please setup a virtual environment by inputing 'python3 -m venv venv' and retry."
    exit 1
fi

source venv/bin/activate

pip install -r requirements.txt

python3 main.py

deactivate