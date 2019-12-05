FROM python:3.6-alpine
ADD . /emailer
WORKDIR /emailer
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "server.py"]
