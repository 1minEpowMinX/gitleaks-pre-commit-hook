#!/usr/bin/env python3
"""Helper script to be used as a pre-commit hook."""
import os
import sys
import subprocess
import platform


def gitleaksInstall():
    TARGETOS = platform.system()
    TARGETARCH = platform.machine()
    URL = f"https://github.com/gitleaks/gitleaks/releases/download/v8.18.1/gitleaks_8.18.1_{TARGETOS}_{TARGETARCH}"

    if TARGETOS == "Linux" or TARGETOS == "Darwin":
        os.system(f"curl -sSL {URL}.tar.gz -o gitleaks.tar.gz")
        os.system("tar -xzf gitleaks.tar.gz")
        os.system("chmod +x gitleaks")
        # os.system("sudo mv gitleaks /usr/local/bin/")
    elif TARGETOS == "Windows":
        os.system("Invoke-WebRequest -Uri {URL}.exe -OutFile gitleaks.zip")
        os.system("Add-Type -AssemblyName System.IO.Compression.FileSystem")
        os.system("[System.IO.Compression.ZipFile]::ExtractToDirectory(gitleaks.zip, (Get-Location))")

def is_gitleaks_installed():
    try:
        subprocess.run(['gitleaks', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if not is_gitleaks_installed():
    gitleaksInstall()

def gitleaksEnabled():
    """Determine if the pre-commit hook for gitleaks is enabled."""
    out = subprocess.getoutput("git config --bool hooks.gitleaks")
    if out == "false":
        os.system("git config --global gitleaks.enable true")
    return True


if gitleaksEnabled():
    exitCode = os.WEXITSTATUS(os.system('gitleaks protect -v --staged'))
    if exitCode == 1:
        print('''Warning: gitleaks has detected sensitive information in your changes.
To disable the gitleaks precommit hook run the following command:

    git config hooks.gitleaks false
''')
        sys.exit(1)
else:
    print('gitleaks precommit disabled\
     (enable with `git config hooks.gitleaks true`)')