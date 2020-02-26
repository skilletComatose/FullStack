FROM python:3.6-buster
RUN pip3 install Flask
RUN mkdir templates
RUN apt update
RUN apt install sqlite3 -y
RUN mkdir basedatos/

COPY basedatos/tasks.db basedatos/
COPY hello.py /
COPY templates/* /templates/
#COPY templates/2.html /templates

RUN pip3 install Flask-SQLAlchemy 

ENV FLASK_APP=hello.py
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0 