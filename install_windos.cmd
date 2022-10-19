#!/bin/bash

@REM check if ther is a python or python3 installed on the system if not, install python3
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    echo "installing python3"
    sudo apt-get install python3
fi

@REM ckreat a folder in user home directory
mkdir ~/Desktop/bin

@REM pull code from github to the folder
git clone https://github.com/Yazan0930/latex-linter ~/Desktop/bin

@REM add the folder to the path
echo "export PATH=$PATH:~/Desktop/bin" >> ~/.bashrc

@REM add to .profile
echo "export PATH=$PATH:~/Desktop/bin" >> ~/.profile

@REM add to .zshrc
echo "export PATH=$PATH:~/Desktop/bin" >> ~/.zshrc

@REM create alias latex-linter to the ~/Desktop/bin/index.py
echo "alias linter='python3 ~/Desktop/bin/index.py'" >> ~/.bashrc

@REM give permission to execute index.py
chmod +x ~/Desktop/bin/index.py

@REM reload bash profile
source ~/.bashrc
