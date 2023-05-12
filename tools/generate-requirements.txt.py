#!/usr/bin/env python3

# Generate requirements.txt and dev-requirements.txt files

import subprocess

if __name__ == '__main__':
    # Directory where the virtual environment is located.
    venv_dir = '.venv'

    # Generate requirements.txt
    print('Generating requirements.txt...')
    subprocess.run(f'{venv_dir}/bin/pip-compile --generate-hashes'.split())

    # Generate dev-requirements.txt
    print('Generating dev-requirements.txt...')
    subprocess.run(
        f'{venv_dir}/bin/pip-compile --generate-hashes'.split()
        + ' --extra dev -o dev-requirements.txt'.split()
    )
