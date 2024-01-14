#!/usr/bin/env python3
"""Helper script to be used as a pre-commit hook."""
import os
import sys
import subprocess
import platform

gitleaksWinPath = "C:\Program Files\gitleaks"


def addPath():
    current_path = os.environ.get('PATH')
    path_to_add = gitleaksWinPath
    new_path = current_path + ";" + path_to_add
    os.environ['PATH'] = new_path


def gitleaksInstall():
    TARGETOS = platform.system().lower()
    TARGETARCH = "x64"
    URL = f"https://github.com/gitleaks/gitleaks/releases/download/v8.18.1/gitleaks_8.18.1_{TARGETOS}_{TARGETARCH}"


    if TARGETOS == "linux" or TARGETOS == "darwin":
        os.system(f"curl -sSL {URL}.tar.gz -o gitleaks.tar.gz")
        os.system("sudo mkdir gitleaks_temp_directory")
        os.system("sudo tar -xzf gitleaks.tar.gz -C gitleaks_temp_directory")
        os.system("sudo chmod +x gitleaks_temp_directory/gitleaks")
        os.system("sudo mv gitleaks_temp_directory/gitleaks /usr/local/bin/")
        os.system("sudo rm -r gitleaks_temp_directory")
        os.system("sudo rm gitleaks.tar.gz")
    elif TARGETOS == "windows":
        os.system("Invoke-WebRequest -Uri {URL}.exe -OutFile gitleaks.zip")
        os.system("Add-Type -AssemblyName System.IO.Compression.FileSystem")
        os.system("[System.IO.Compression.ZipFile]::ExtractToDirectory(gitleaks.zip, (Get-Location))")
        os.system(f"mkdir {gitleaksWinPath} && move gitleaks.exe {gitleaksWinPath}")
        addPath()
        os.system("Remove-Item gitleaks.zip")
        

def is_gitleaks_installed():
    try:
        subprocess.run(['gitleaks', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except:
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