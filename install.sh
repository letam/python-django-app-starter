#!/bin/bash

# Directory where the virtual environment is located.
venv_dir=".venv"

# Ensure the virtual environment exists.
if [ ! -d "$venv_dir" ]; then
	./create_venv.py
fi

# Install project dependencies.
./install_dependencies.py
