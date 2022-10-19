# get python image
FROM ubuntu:latest

RUN apt update
RUN apt install python3-pip -y

# insatll git
RUN apt install git -y

#install pytest
RUN pip3 install -U  pytest

WORKDIR /root/files

# Create folder $HOME/app
WORKDIR /root/app

# pull code from github to $HOME/bin
RUN git clone https://github.com/Yazan0930/latex-linter.git /root/app/latex-linter

# add $HOME/bin to $PATH
ENV PATH="/root/app/latex-linter:${PATH}"
#echo "export PATH=$HOME/app/latex-linter:$PATH" >> $HOME/.bash_profile

# add to .profile
RUN echo "export PATH=/root/app/latex-linter:$PATH" >> $HOME/.profile
#echo "alias latex-linter='index.py'" >> $HOME/.bash_profile

# add to .zshrc
RUN echo "export PATH=/root/app/latex-linter:$PATH" >> $HOME/.zshrc
#echo "alias latex-linter='index.py'" >> $HOME/.zshrc

# create alias latex-linter to $HOME/app/latex-linter/index.py
#echo "alias latex-linter='index.py'" >> ~/.bash_profile
RUN echo "alias linter='python3 $HOME/app/latex-linter/index.py'" >> ~/.bashrc

# give permission to execute index.py
RUN chmod +x $HOME/app/latex-linter/index.py
#chmod +x $HOME/app/latex-linter/index.py

# reload bash profile
RUN echo "source ~/.bash_profile" >> ~/.bashrc
#source ~/.bash_profile

WORKDIR /root

CMD ["echo", "Run: docker run -it latex-linter /bin/bash"]

