FROM python:3.6-alpine
RUN apk add build-base



RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip install uwsgi

ADD . /emailer
WORKDIR /emailer
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 5000
CMD [ "uwsgi", "--ini", "app.ini" ]
