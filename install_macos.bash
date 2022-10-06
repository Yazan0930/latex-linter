#!/bin/bash

# Create folder $HOME/bin
mkdir -p $HOME/bin
# pull code from github to $HOME/bin
git clone https://github.com/Yazan0930/latex-linter $HOME/bin/latex-linter

# add $HOME/bin to $PATH
echo "export PATH=$HOME/bin/latex-linter:$PATH" >> $HOME/.bash_profile

# add to .profile
echo "alias latex-linter='index.py'" >> $HOME/.bash_profile

# add to .zshrc
echo "alias latex-linter='index.py'" >> $HOME/.zshrc

# create alias latex-linter to $HOME/bin/index.py
echo "alias latex-linter='index.py'" >> ~/.bash_profile

# give permission to execute index.py
chmod +x $HOME/bin/latex-linter/index.py

# reload bash profile
source ~/.bash_profile