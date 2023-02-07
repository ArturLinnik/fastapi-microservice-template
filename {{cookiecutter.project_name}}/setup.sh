#!/bin/bash

set -e

if ! python3 -m poetry; then
    echo "Poetry is not installed"
    echo "[*] Installing poetry..."
    pip install poetry
fi

echo "[*] Configuring poetry virtualenvs..."
python3 -m poetry config virtualenvs.in-project true

python_version=$(python -c 'import platform; print(platform.python_version())')

echo "[*] Creating virtualenv..."
python3 -m poetry env use $python_version

echo "[*] Activating virtualenv..."
source .venv/bin/activate

echo "[*] Executing poetry install..."
poetry install

while true; do
    read -p "Do you wish to initiate a git repository? (y/n) " yn
    case $yn in
        [Yy]* )
            if ! git -v &> /dev/null; then 
                echo "Git is not installed"
                break
            fi
            echo -n "Enter the origin of the repository: "
            read remote
            git init --initial-branch=main
            git remote add origin $remote
            git add .
            git commit -m "Initial commit"
            git push -u origin main
            break ;;
        [Nn]* ) exit ;;
        * ) echo "Please answer yes or no." ;;
    esac
done
