FROM python:3.6.2-slim
MAINTAINER Alberto Galera "galerajimenez@gmail.com"
RUN apt-get update -y
RUN apt-get install -y gcc
RUN apt-get install python3-magic -y
WORKDIR apistar
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
#ENTRYPOINT bash
ENTRYPOINT cd exampleapp; apistar run --port=5000 --host="0.0.0.0"
