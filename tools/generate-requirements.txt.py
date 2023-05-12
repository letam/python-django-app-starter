#!/usr/bin/env python3

# Generate requirements.txt and dev-requirements.txt files

import subprocess

if __name__ == '__main__':
    # Directory where the virtual environment is located.
    venv_dir = '.venv'

    # Generate requirements.txt
    print('Generating requirements.txt...')
    generate_requirements_cmd = f'{venv_dir}/bin/pip-compile --generate-hashes'
    subprocess.run(generate_requirements_cmd.split())

    # Generate dev-requirements.txt
    print('Generating dev-requirements.txt...')
    generate_dev_requirements_cmd = (
        f'{venv_dir}/bin/pip-compile --generate-hashes'
        + ' --extra dev -o dev-requirements.txt'
    )
    subprocess.run(generate_dev_requirements_cmd.split())
