# get python image
FROM ubuntu:latest

RUN apt update
RUN apt install python3-pip -y

# insatll git
RUN apt install git -y

# set working directory
WORKDIR /app
# download a github repo
RUN git clone https://github.com/Yazan0930/latex-linter.git

COPY . .

CMD [ "python3", "-m" ,"run", "--host=0.0.0.0"]
# docker run -it linter /bin/bash
