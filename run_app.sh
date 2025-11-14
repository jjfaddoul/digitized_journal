#!/bin/bash

# Activate virtual environment and run Streamlit app
cd "$(dirname "$0")"

echo "Starting CARE Journal Survey App..."
echo "=================================="

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

# Run the Streamlit app
streamlit run app.py
