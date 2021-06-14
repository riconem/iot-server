# syntax=dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /tester
COPY . .
RUN apt-get update \
&& apt-get install -y iputils-ping
#  && apt-get install -y python3-pip python3-dev \
#  && cd /usr/local/bin \
#  && ln -s /usr/bin/python3 python \
#  && pip3 --no-cache-dir install --upgrade pip \
#  && rm -rf /var/lib/apt/lists/*
RUN pip3 install paho-mqtt

CMD [ "python3", "check_connection.py" ] 

