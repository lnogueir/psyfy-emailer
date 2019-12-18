FROM python:3.6-alpine
RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi


ADD . /emailer
WORKDIR /emailer
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# EXPOSE 5000
CMD [ "uwsgi", "--ini", "app.ini" ]
