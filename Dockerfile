FROM thinkwhere/gdal-python:3.7-ubuntu as base

ENV PYTHONUNBUFFERED=1

ENV DJANGO_DIR=/api_django

WORKDIR $DJANGO_DIR

RUN apt-get -y install python3

RUN apt-get -y install python3-pip

RUN pip3 install --upgrade pip

COPY requirements.txt $DJANGO_DIR/

RUN pip3 install -r requirements.txt