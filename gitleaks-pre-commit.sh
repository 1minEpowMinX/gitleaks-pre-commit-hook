#!/bin/bash

curl -sSL https://github.com/1minEpowMinX/gitleaks-pre-commit-hook/pre-commit.py -o pre-commit.py
sudo chmod +x pre-commit.py
mv pre-commit.py .git/hooks/pre-commit.py