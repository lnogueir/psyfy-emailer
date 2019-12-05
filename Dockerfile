FROM python:3.7
ADD . /emailer
WORKDIR /emailer
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "server.py"]
