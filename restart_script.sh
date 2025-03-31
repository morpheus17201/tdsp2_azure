#!/bin/bash


# Name of the Python script (replace with the actual name of your script)
WORKING_DIR="/home/azureuser/tdsp2_azure"
SCRIPT_NAME="main_tdsp2_azure.py"
VENV_PYTHON="/home/azureuser/tdsp2_azure/.venv/bin/python3"


cd "$WORKING_DIR" || { echo "Failed to change directory to $WORKING_DIR"; exit 1; }


# Check if the script is running
PID=$(pgrep -f "$SCRIPT_NAME")

# If the script is running (PID is not empty)
if [ -n "$PID" ]; then
    echo "$SCRIPT_NAME is running with PID: $PID"
    # Kill the running process
    kill "$PID"
    echo "$SCRIPT_NAME has been stopped."
else
    echo "$SCRIPT_NAME is not running."
fi

# Start the script again
echo "Starting $SCRIPT_NAME using $VENV_PYTHON..."
nohup "$VENV_PYTHON" "$SCRIPT_NAME" &>/dev/null &
echo "$SCRIPT_NAME has been started."