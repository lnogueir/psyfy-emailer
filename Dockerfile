FROM python:3.6
# RUN apk add build-base
RUN apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

# RUN apk add --no-cache --update \
#   python3 \
#   python3-dev \
#   py3-gevent \
#   uwsgi \
#   uwsgi-python3 \
#   uwsgi-http \
#   uwsgi-gevent3
RUN pip install uwsgi
ADD . /emailer
WORKDIR /emailer
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# EXPOSE 5000
CMD [ "uwsgi", "--ini", "app.ini" ]
