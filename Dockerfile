# get python image
FROM ubuntu:latest

RUN apt update
RUN apt install python3-pip -y

# insatll git
RUN apt install git -y

#install pytest
RUN pip3 install -U  pytest

# set working directory
WORKDIR /app
# download a github repo
RUN git clone https://github.com/Yazan0930/latex-linter.git

COPY . .

CMD ["docker run -it linter /bin/bash"]
