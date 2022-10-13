#!/bin/bash



if [ "$OS" = "Windows_NT" ]; then
    # Windows
    echo "Windows"
    # Create folder in %USERPROFILE%\bin
    mkdir -p $USERPROFILE/bin
    # pull code from github to %USERPROFILE%\bin
    git clone https://github.com/Yazan0930/latex-linter $USERPROFILE/bin/latex-linter

    # add %USERPROFILE%\bin to %PATH%
    echo "export PATH=$USERPROFILE/bin/latex-linter:$PATH" >> $USERPROFILE/.bash_profile

    # add to .profile
    echo "alias latex-linter='index.py'" >> $USERPROFILE/.bash_profile

    # add to .zshrc
    echo "alias latex-linter='index.py'" >> $USERPROFILE/.zshrc

    # create alias latex-linter to %USERPROFILE%\bin\index.py
    echo "alias latex-linter='index.py'" >> $USERPROFILE/.bash_profile

    # reload bash profile
    source $USERPROFILE/.bash_profile

    # give permission to execute index.py
    chmod +x $USERPROFILE/bin/latex-linter/index.py

    # reload bash profile
    source $USERPROFILE/.bash_profile

elif [ "$(uname)" = "Darwin" ]; then
    # Mac
    echo "Mac"
    # Create folder in $HOME/bin
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

    # reload bash profile
    source ~/.bash_profile

    # give permission to execute index.py
    chmod +x $HOME/bin/latex-linter/index.py

    # reload bash profile
    source ~/.bash_profile
elif [ "$(expr substr $(uname -s) 1 5)" = "Linux" ]; then
    # Linux
    echo "Linux"
    # Create folder in $HOME/bin
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

    # reload bash profile
    source ~/.bash_profile

    # give permission to execute index.py
    chmod +x $HOME/bin/latex-linter/index.py

    # reload bash profile
    source ~/.bash_profile

fi
