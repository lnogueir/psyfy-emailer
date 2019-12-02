from flask import Flask, jsonify, request
from emailer import Emailer

app = Flask(__name__)
emailer = Emailer('ece150sucks@gmail.com', 'jawad123')


@app.route('/request_account', methods=['POST'])
def request_account():	
	emailer.connect()
	emailer.make_request_account_email(request.get_json())
	emailer.send_email()
	emailer.disconnect()
	return jsonify({'message':'Email sent successfully'})		
	


@app.route('/request_accepted', methods=['POST'])
def request_accepted():	
	emailer.connect()
	emailer.make_request_accepted_email(request.get_json())
	emailer.send_email()
	emailer.disconnect()
	return jsonify({'message':'Email sent successfully'})		



@app.route('/request_declined', methods=['POST'])
def request_declined():	
	emailer.connect()
	emailer.make_request_declined_email(request.get_json())
	emailer.send_email()
	emailer.disconnect()
	return jsonify({'message':'Email sent successfully'})		
	

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	try:
		emailer.connect()
		emailer.make_forgot_password_email(request.get_json())
		emailer.send_email()
		emailer.disconnect()
		return jsonify({'message':'Email sent successfully'})		
	except:
		return jsonify({'error': 'Email was not sent properly'}), 500	




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


