#!/bin/bash

# remove $HOME/bin/latex-linter
rm -rf $HOME/bin/latex-linter

# remove $HOME/bin from $PATH
sed -i '' '/export PATH=$HOME\/bin\/latex-linter:$PATH/d' $HOME/.bash_profile

# remove alias latex-linter
sed -i '' '/alias latex-linter='index.py'/d' $HOME/.bash_profile

# reload bash profile
source ~/.bash_profile