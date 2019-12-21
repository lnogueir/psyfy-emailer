FROM python:3
ADD . /emailer
WORKDIR /emailer
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "uwsgi", "--ini", "app.ini" ]
