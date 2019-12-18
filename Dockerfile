FROM python:3.6-alpine
ADD . /emailer
WORKDIR /emailer
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# EXPOSE 5000
CMD [ "uwsgi", "--ini", "app.ini" ]
