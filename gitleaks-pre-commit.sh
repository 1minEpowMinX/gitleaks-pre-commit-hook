#!/bin/bash

curl -sSL https://raw.githubusercontent.com/1minEpowMinX/gitleaks-pre-commit-hook/main/pre-commmit.py -o pre-commit.py
sudo chmod +x pre-commit.py
mv pre-commit.py .git/hooks/pre-commit

# Display success messages
printf "Installation..."
printf "The installation was successful!"
printf "The pre-commit script has been moved to .git/hooks/pre-commit. Enjoy using it!"