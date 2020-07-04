FROM python:3.8

COPY ./ /pydev
WORKDIR /pydev

RUN pip3 install -r requirements_dev.txt
RUN pip3 install Click>=6.0 redis>=2.1 twine>=1.9
