#!/usr/bin/env python3

import os
import subprocess
import sys

_venv_pip_path: str


def set_venv_pip_path(venv_dir):
    global _venv_pip_path
    if os.name == 'nt':  # Windows
        _venv_pip_path = os.path.join(venv_dir, 'Scripts', 'pip')
    else:  # Unix or macOS
        _venv_pip_path = os.path.join(venv_dir, 'bin', 'pip')


def install_toml():
    def is_module_installed(name):
        import importlib.util

        spec = importlib.util.find_spec(name)
        return spec is not None

    if not is_module_installed('toml'):
        print('The package "toml" is required and is not found. Fixing that...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'toml'])
        print()


def install_dependencies_from_pyproject_toml(pyproject_toml_path):
    # Load the contents of the pyproject.toml file.
    try:
        import toml

        with open(pyproject_toml_path, 'r') as f:
            pyproject_toml = toml.load(f)
    except FileNotFoundError:
        print(f'File "{pyproject_toml_path}" not found.')
        sys.exit(1)
    except Exception as e:
        print(f'Error while reading "{pyproject_toml_path}": {e}')
        sys.exit(1)

    # Extract the dependencies from the [project.dependencies] section.
    try:
        dependencies = pyproject_toml['project']['dependencies']
    except KeyError:
        print('Dependencies not found in the pyproject.toml file.')
        sys.exit(1)

    # Install the dependencies into virtual environment using pip.
    print('Installing Python package dependencies for project...')
    for package in dependencies:
        try:
            subprocess.check_call([_venv_pip_path, 'install', package])
        except subprocess.CalledProcessError as e:
            print(f'Error while installing "{package}": {e}')
            sys.exit(1)

    print('Dependencies installed successfully.')


if __name__ == '__main__':
    # Path to the pyproject.toml file.
    pyproject_toml_path = 'pyproject.toml'

    # Directory where the virtual environment is located.
    venv_dir = '.venv'

    # Gather path to pip for virtual environment.
    set_venv_pip_path(venv_dir)

    # Install toml to system to read pyproject.toml file in this Python script.
    install_toml()

    # Install the dependencies from the pyproject.toml file.
    install_dependencies_from_pyproject_toml(pyproject_toml_path)