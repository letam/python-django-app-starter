#!/bin/bash

# Directory where the virtual environment is located.
venv_dir=".venv"

for arg in "$@"; do
	case "$arg" in
		--dev) # Install dev dependencies
			install_dev_dependencies=1
	esac
done

# Ensure the virtual environment exists.
if [ ! -d "$venv_dir" ]; then
	./install/create_venv.py
fi

# Install project dependencies.
echo "Installing project dependencies..."
if [ ! -z $install_dev_dependencies ]; then
	./install/install_dependencies.py --dev
else
	./install/install_dependencies.py
fi
