FROM python:3.5

RUN mkdir -p /code/vendors

ENV PYTHONUNBUFFERED=1
ENV PYTHONUSERBASE=/code/vendors

RUN pip install --upgrade pip


RUN apt-get update && \
    apt-get install -y gettext-base gettext
RUN pip install Pillow    
EXPOSE 8000