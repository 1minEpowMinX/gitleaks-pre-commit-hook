#!/bin/bash

# Display success messages
printf "Installation...\n"
printf "The installation was successful!\n"
printf "The pre-commit script has been moved to .git/hooks/pre-commit. Enjoy using it!\n"

curl -sSL https://raw.githubusercontent.com/1minEpowMinX/gitleaks-pre-commit-hook/main/pre-commmit.py -o pre-commit.py
chmod +x pre-commit.py
mv pre-commit.py .git/hooks/pre-commit
