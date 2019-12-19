FROM python:3.6-alpine
RUN apk add build-base


RUN apk add --no-cache --update \
  python3 \
  python3-dev \
  py3-gevent \
  uwsgi \
  uwsgi-python3 \
  uwsgi-http \
  uwsgi-gevent3

ADD . /emailer
WORKDIR /emailer
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 5000
CMD [ "uwsgi", "--ini", "app.ini" ]
