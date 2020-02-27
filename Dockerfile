FROM python:3.6-buster 

RUN pip3 install Flask
RUN pip3 install Flask-SQLAlchemy 
RUN pip3 install flask-marshmallow
RUN pip3 install marshmallow-sqlalchemy

RUN mkdir templates
RUN apt update
RUN apt install sqlite3 -y
RUN mkdir basedatos/

COPY basedatos/tasks.db basedatos/
COPY hello.py /
COPY templates/* /templates/


ENV FLASK_APP=hello.py
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0 