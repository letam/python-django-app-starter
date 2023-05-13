#!/usr/bin/env python3

# Generate requirements.txt and dev-requirements.txt files

import glob
import os
import shutil
import subprocess
from pathlib import Path

if __name__ == '__main__':
    # Directory where the virtual environment is located.
    venv_dir = '.venv'

    # Directory where the virtual environment's binary files/scripts are located.
    bin_dir = Path(venv_dir) / 'Scripts' if os.name == 'nt' else 'bin'

    # Generate requirements.txt
    print('Generating requirements.txt...')
    generate_requirements_cmd = (
        str(bin_dir / 'pip-compile') + ' --generate-hashes'
    )
    subprocess.run(generate_requirements_cmd.split())

    # Generate dev-requirements.txt
    print('Generating dev-requirements.txt...')
    generate_dev_requirements_cmd = (
        str(bin_dir / 'pip-compile')
        + ' --generate-hashes'
        + ' --extra dev -o dev-requirements.txt'
    )
    subprocess.run(generate_dev_requirements_cmd.split())

    # Remove *.egg-info directories created by pip-compile
    for file in glob.glob('*.egg-info'):
        shutil.rmtree(file)
