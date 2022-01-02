FROM cimg/python:3.8
MAINTAINER Olivier Samin <oliviersamin@gmail.com>
EXPOSE 80
RUN ["pip install - r", "requirements.txt"]
