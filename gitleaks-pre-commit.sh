#!/bin/bash

curl -sSL https://raw.githubusercontent.com/1minEpowMinX/gitleaks-pre-commit-hook/main/pre-commmit.py -o pre-commit.py
sudo chmod +x pre-commit.py
mv pre-commit.py .git/hooks/pre-commit.py