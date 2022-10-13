#!/bin/bash

# remove $HOME/app/latex-linter
rm -rf $HOME/app/latex-linter

# remove $HOME/bin from $PATH
sed -i '' '/export PATH=$HOME\/app\/latex-linter:$PATH/d' $HOME/.bash_profile

# remove alias latex-linter
sed -i '' '/alias latex-linter='index.py'/d' $HOME/.bash_profile

# reload bash profile
source ~/.bash_profile