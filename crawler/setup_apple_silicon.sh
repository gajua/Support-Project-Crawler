#!/bin/bash

# Check conda installation
if command -v conda &> /dev/null; then
    # Conda is installed
    echo "Conda is installed."
else
    # Conda is not installed
    echo "Conda is not installed."
    echo "Installing Conda..."

    # Install miniforge3
    curl -LO https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
    chmod +x ./Miniforge3-MacOSX-arm64.sh
    sh ./Miniforge3-MacOSX-arm64.sh
    source ~/miniforge3/bin/activate

    echo "Conda is installed."
fi

# Check version
conda --version

# Check if the "crawler_py39" environment exists
if conda env list | grep -q "^crawler_py39[[:space:]]"; then
    # Environment exists
    echo "Conda environment 'crawler_py39' exists."
else
    # Environment does not exist
    echo "Conda environment 'crawler_py39' does not exist."

    # Create the environment
    conda create --name crawler_py39 python=3.9 -y
fi

echo "Activating the environment..."
conda init
conda activate crawler_py39

# Install the required packages
echo "Installing the required packages..."
pip install -r requirements.txt

echo "Setup is complete."