FROM ubuntu:20.04

WORKDIR /root
COPY ./Dockerfile /root

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python
RUN apt-get install -y python3-pip
RUN pip3 install uvicorn
RUN pip3 install fastapi
RUN pip3 install statistics
RUN pip3 install httptools==0.1.

RUN mkdir /root/assignment
WORKDIR /root/assignment
RUN git clone https://github.com/Hruthvik/finalexam_oss.git
WORKDIR /root/assignment/finalexam_oss


CMD ["uvicorn","sell:app1","--reload","--host","0.0.0.0","--port","8080"]


