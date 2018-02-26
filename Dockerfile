FROM python:3.6

COPY ./ /pydev
WORKDIR /pydev

RUN pip3 install -r requirements_dev.txt
RUN pip3 install Click>=6.0 redis>=2.1
