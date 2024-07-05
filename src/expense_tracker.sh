#!/bin/bash

if command -v python3 &> /dev/null
then
    echo "You currently have Python3 installed."
else
    echo "You do not currently have Python3 installed. Please install Python3 and run the script again"
fi

check_pip() {
    if command -v pip &> /dev/null; then
        echo "You current have pip installed."
    else
        echo "You current do not have pip installed please install pip."
    fi
}

if [ -d "venv" ]; then 
    echo "Virtual environment exists"
else
    echo "There is an error: Virtual environment does not exist. Please setup a virtual environment by inputing 'python3 -m venv venv' and retry."
    exit 1
fi

source venv/bin/activate

pip install -r requirements.txt

echo "Environment setup complete. Virtual environment activated."

python3 main.py

deactivate