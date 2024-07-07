#!/bin/bash

# Check whether Python3 is installed.
if command -v python3 &> /dev/null
then
    echo "You currently have Python3 installed."
else
    echo "You do not currently have Python3 installed. Please install Python3 and run the script again"
fi

# Check whether Pip is installed.
check_pip() {
    if command -v pip &> /dev/null; then
        echo "You current have pip installed."
    else
        echo "You current do not have pip installed please install pip."
    fi
}

# Check whether a Virtual Environment exists.
if [ -d "venv" ]; then 
    echo "Virtual environment exists"
else
    echo "There is an error: Virtual environment does not exist. Please setup a virtual environment by inputing 'python3 -m venv venv' and retry."
    exit 1
fi

# Activate the existing Virtual Environment
source venv/bin/activate

# Install dependencies from requirements.txt file
pip install -r requirements.txt

# Echo message to user successful setup completion
echo "Environment setup complete. Virtual environment activated."

# Run the Expense Tracker Application
python3 main.py

# Deactivate the Virtual Environment
deactivate