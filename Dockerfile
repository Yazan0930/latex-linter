# get python image
FROM ubuntu:latest

RUN apt update
RUN apt install python3-pip -y

# insatll git
RUN apt install git -y

#install pytest
RUN pip3 install -U  pytest

# set working directory
WORKDIR /root/app

# download a github repo
ADD https://github.com/Yazan0930/latex-linter/releases/download/installer/install_macos.bash /root/app/install_macos.bash
RUN bash install_macos.bash 

WORKDIR /root/files


CMD ["source ~/.bash_profile"]
