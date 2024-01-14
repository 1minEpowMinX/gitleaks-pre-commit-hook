#!/bin/bash

curl -sSL https://raw.githubusercontent.com/1minEpowMinX/gitleaks-pre-commit-hook/main/pre-commmit.py -o pre-commit.py
echo "Installation..."
sudo chmod +x pre-commit.py
echo "The installation was successful!"
mv pre-commit.py .git/hooks/pre-commit
echo "The pre-commit script has been moved to .git/hooks/pre-commit. Enjoy using it!"