# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=run.py
# ENV CLIENT_ID=2995d8d9fd51a2cc241e
# ENV CLIENT_SECRET=919a89f241c9eee8ee476ad250da27cb2d2f6893
# ENV EMAIL_USER=zdanukmichalmail@gmail.com
# ENV EMAIL_PASS="zqry zich dhwp ptzr"

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD [ "python3", "run.py", "&"]