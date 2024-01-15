# gitleaks-pre-commit-hook
A pre-commit hook script with automatic installation of gitleaks depending on the operating system, with the enable option using git config and installation using the "curl pipe sh" method
# Usage  
**Navigate to the desired git repository for installation.**  
Install:  
**For Windows, use Git Bash**
```sh
curl -sSL https://raw.githubusercontent.com/1minEpowMinX/gitleaks-pre-commit-hook/main/gitleaks-pre-commit.sh | sh
```
Done! The system will automatically check commits.  
To disable the gitleaks system, type in the terminal:  
```sh
git config hooks.gitleaks false
```
<br>

# Auto installation

If gitleaks is not install, the script will automatically download it for a supported OS:<br>  

| Linux | Windows | Future OS support |
| ----------- | ----------- | ----------- |
| Create a temporary directory gitleaks_temp_directory | Creates the D:\gitleaks directory | --- |
| Unpack the archive and move gitleaks to /usr/local/bin/ | Extracts the archive to the D:\gitleaks directory | --- |
| Will delete the temporary directory gitleaks_temp_directory and the archive | Deletes the archive | --- |

<br>

**Enjoy It!**
