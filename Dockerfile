# get python image
FROM ubuntu:latest

RUN apt update
RUN apt install python3-pip -y

# insatll git
RUN apt install git -y

#install pytest
RUN pip3 install -U  pytest

WORKDIR /root/files

# set working directory
WORKDIR /root/app

# download a github repo
ADD https://github.com/Yazan0930/latex-linter/releases/download/installer/install_macos.bash /root/app/install_macos.bash

CMD ["source ~/.bash_profile"]
