#!/bin/bash

# Directory where the virtual environment should be created.
venv_dir=".venv"

# Check if the virtual environment directory exists.
if [ -d "$venv_dir" ]; then
	echo "Virtual environment already exists in '$venv_dir'."
else
	# Create a new virtual environment.
	python3 -m venv "$venv_dir"
	echo "Virtual environment created in '$venv_dir'."
fi

# Provide instructions for activating the virtual environment.
echo "To activate the virtual environment, run 'source $venv_dir/bin/activate' (Unix/macOS) or 'source $venv_dir/Scripts/activate' (Windows)."
