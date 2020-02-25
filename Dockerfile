FROM python:3.6-buster
RUN pip3 install Flask
COPY hello.py /
COPY Templates/* /    

ENV FLASK_APP=hello.py
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0 