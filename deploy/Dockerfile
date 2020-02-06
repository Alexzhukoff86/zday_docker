FROM python:3.7

ENV TESTTOOL /app

RUN mkdir $TESTTOOL

WORKDIR $TESTTOOL

RUN apt-get update

RUN apt-get install \
mc \
vim

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./src .

CMD ["/bin/bash"]