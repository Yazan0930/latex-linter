FROM python:3.9

# git clone https://github.com/Yazan0930/latex-linter $HOME/bin/latex-linter
# cd $HOME/bin/latex-linter
# docker build -t latex-linter .
# docker run -it latex-linter   # to run the container
# docker run -it latex-linter /bin/bash   # to run the container and get a shell

RUN git clone


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "index.py -h" ]