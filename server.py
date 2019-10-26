from flask import Flask, jsonify, request
from emailer import Emailer

app = Flask(__name__)
emailer = Emailer('ece150sucks@gmail.com', 'jawad123')
@app.route('/test_request1', methods=['POST'])
def test_request():
	file = request.get_json()['file']
	emailer.receiver = 'lnogueir@uwaterloo.ca'
	emailer.connect()
	emailer.make_base64_attachment_email(file)
	emailer.send_email()
	emailer.disconnect()
	return jsonify({'message':'Email sent successfully'})


@app.route('/test_request2', methods=['POST'])
def test_request2():
	try:
		emailer.connect()
		emailer.make_request_account_email(request.get_json())
		emailer.send_email()
		emailer.disconnect()
		return jsonify({'message':'Email sent successfully'})		
	except:
		return jsonify({'error': 'Email was not sent properly'}), 500	

@app.route('/request_accepted', methods=['POST'])
def request_accepted():
	try:
		emailer.connect()
		emailer.make_request_accepted_email(request.get_json())
		emailer.send_email()
		emailer.disconnect()
		return jsonify({'message':'Email sent successfully'})		
	except:
		return jsonify({'error': 'Email was not sent properly'}), 500	

@app.route('/request_declined', methods=['POST'])
def request_declined():
	try:
		emailer.connect()
		emailer.make_request_declined_email(request.get_json())
		emailer.send_email()
		emailer.disconnect()
		return jsonify({'message':'Email sent successfully'})		
	except:
		return jsonify({'error': 'Email was not sent properly'}), 500	





if __name__ == '__main__':
    app.run(debug=True)

