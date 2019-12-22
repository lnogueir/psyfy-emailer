from flask import Flask, jsonify, request, logging
from logging import FileHandler, basicConfig, WARNING, DEBUG, Formatter
from emailer import Emailer
import os
from time import sleep

app = Flask(__name__)
logging.default_handler.setFormatter(
    Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))

emailer = Emailer(os.getenv('EMAILER_ADDRESS'), os.getenv('EMAILER_PASSWORD'))

if not app.debug:
    file_handler = FileHandler('emailer.log')
    file_handler.setLevel(WARNING)
    app.logger.addHandler(file_handler)
else:
    basicConfig(level=DEBUG)


@app.route("/request_account", methods=["POST"])
def request_account():
    user_package = request.get_json()
    app.logger.info(f'REQUEST_ACCOUNT REQUEST FOR: {user_package}')
    num_of_attemps_to_send_email = 1
    while (not emailer.run('REQUEST_ACCOUNT', user_package, app.logger)
           and num_of_attemps_to_send_email <= 5):
        num_of_attemps_to_send_email += 1
        sleep(0.5)
    app.logger.info(
        f'REQUEST_ACCOUNT EMAILER FINISHED ON ATTEMPT: {num_of_attemps_to_send_email}')
    return (
        (jsonify({"message": "Email sent successfully"}), 200)
        if num_of_attemps_to_send_email <= 5 else
        (jsonify({"error": "Failed to send email"}), 500)
    )


@app.route("/request_accepted", methods=["POST"])
def request_accepted():
    user_package = request.get_json()
    app.logger.info(f'REQUEST_ACCEPTED REQUEST FOR: {user_package}')
    num_of_attemps_to_send_email = 1
    while (not emailer.run('REQUEST_ACCEPTED', user_package, app.logger)
           and num_of_attemps_to_send_email <= 5):
        num_of_attemps_to_send_email += 1
        sleep(0.5)
    app.logger.info(
        f'REQUEST_ACCEPTED EMAILER FINISHED ON ATTEMPT: {num_of_attemps_to_send_email}')
    return (
        (jsonify({"message": "Email sent successfully"}), 200)
        if num_of_attemps_to_send_email <= 5 else
        (jsonify({"error": "Failed to send email"}), 500)
    )


@app.route("/request_declined", methods=["POST"])
def request_declined():
    user_package = request.get_json()
    app.logger.info(f'REQUEST_DECLINED REQUEST FOR: {user_package}')
    num_of_attemps_to_send_email = 1
    while (not emailer.run('REQUEST_DECLINED', user_package, app.logger)
           and num_of_attemps_to_send_email <= 5):
        num_of_attemps_to_send_email += 1
        sleep(0.5)
    app.logger.info(
        f'REQUEST_DECLINED EMAILER FINISHED ON ATTEMPT: {num_of_attemps_to_send_email}')
    return (
        (jsonify({"message": "Email sent successfully"}), 200)
        if num_of_attemps_to_send_email <= 5 else
        (jsonify({"error": "Failed to send email"}), 500)
    )


@app.route("/forgot_password", methods=["POST"])
def forgot_password():
    user_package = request.get_json()
    app.logger.info(f'FORGOT_PASSWORD REQUEST FOR: {user_package}')
    num_of_attemps_to_send_email = 1
    while (not emailer.run('FORGOT_PASSWORD', user_package, app.logger)
           and num_of_attemps_to_send_email <= 5):
        num_of_attemps_to_send_email += 1
        sleep(0.5)
    app.logger.info(
        f'FORGOT_PASSWORD EMAILER FINISHED ON ATTEMPT: {num_of_attemps_to_send_email}')
    return (
        (jsonify({"message": "Email sent successfully"}), 200)
        if num_of_attemps_to_send_email <= 5 else
        (jsonify({"error": "Failed to send email"}), 500)
    )


if __name__ == "__main__":
    app.run(host=os.getenv('HOST_ADDRESS'),
            debug=bool(os.getenv('FLASK_DEBUG')))
