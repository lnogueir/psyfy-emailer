import smtplib
from smtplib import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class Emailer:
	connected=False
	connection=None
	class Account():
		def __init__(self, user_email, password):
			self.user=user_email
			self.password=password
	
	def __init__(self, user_email, password, receiver=None):
		self.msg = MIMEMultipart("alternative")
		self.emailer=Emailer.Account(user_email, password)
		self.msg['From'] = user_email
		self.receiver = receiver

	def connect(self):
		if not Emailer.connected:
			try:
				connection = smtplib.SMTP('smtp.gmail.com',587)
				connection.ehlo()
				connection.starttls()
				connection.login(self.emailer.user,self.emailer.password)
			except SMTPResponseException as e:
				error_code=e.smtp_code
				error_message=e.smtp_error
				print('ERROR CONNECTING:'+str(error_message))
			else:
				Emailer.connected=True
				Emailer.connection = connection


	@classmethod
	def disconnect(cls):
		if cls.connected:
			cls.connection.close()
			cls.connected=False



	def make_base64_attachment_email(self, file_as_base64):
		try:
			if not Emailer.connected:
				self.connect()
			self.msg['To'] = self.receiver	
			self.msg["Subject"] = "Making sure this works"
			part = MIMEBase("application", "octet-stream")
			part.set_payload(file_as_base64)
			part.add_header('Content-Transfer-Encoding', 'base64')
			part['Content-Disposition'] = 'attachment; filename="%s"' % 'file_test.png'
			self.msg.attach(part);
		except:
			self.disconnect()


	def make_request_accepted_email(self, user_package):
		try:
			if not Emailer.connected:
				self.connect()
			self.receiver=user_package['contact_email'] 
			self.msg["To"] = self.receiver
			self.msg["Subject"] = "Your request has been approved!"
			body = 'User Package:\n'
			body += 'Name: ' + str(user_package['full_name']) + '\n' 
			body += 'Contact Number: ' + str(user_package['phone_number']) + '\n'
			body += 'Email: ' + str(user_package['contact_email']) + '\n'
			body += 'Address: ' + str(user_package['address']) + '\n'
			body += 'Password: ' + str(user_package['password'])
			self.msg.attach(MIMEText(body,'plain'))
		except:
			self.disconnect()


	def make_request_declined_email(self, user_package):
		try:
			if not Emailer.connected:
				self.connect()
			self.receiver=user_package['contact_email'] 
			self.msg["To"] = self.receiver
			self.msg["Subject"] = "Your request has been declined"
			body = 'User Package:\n'
			body += 'Name: ' + str(user_package['full_name'])
			self.msg.attach(MIMEText(body,'plain'))
		except:
			self.disconnect()



	def make_request_account_email(self, user_package):

		if not Emailer.connected:
			print('checking in email connected')
			self.connect()
		self.receiver = self.emailer.user	
		self.msg['To'] = self.emailer.user
		self.msg["Subject"] = "Account Request for " + str(user_package['full_name'])
		body = 'User Package:\n'
		body += 'Name: ' + str(user_package['full_name']) + '\n' 
		body += 'Contact Number: ' + str(user_package['phone_number']) + '\n'
		body += 'Email: ' + str(user_package['contact_email']) + '\n'
		body += 'Address: ' + str(user_package['address']) + '\n'
		body += 'About: ' + str(user_package['about']) + '\n'
		body += 'Accept: ' + str(user_package['accept']) + '\n'
		body += 'Deny: ' + str(user_package['deny'])
		self.msg.attach(MIMEText(body,'plain'))
		if 'files' in user_package:
			for file in user_package['files']:
				part = MIMEBase("application", "octet-stream")
				part.set_payload(file['base64'])
				part.add_header('Content-Transfer-Encoding', 'base64')
				part['Content-Disposition'] = 'attachment; filename="%s"' % file['fileName']
				self.msg.attach(part)

	def make_forgot_password_email(self, email_info):
		if not Emailer.connected:
			self.connect()
		self.receiver = email_info['email']
		self.msg["To"] = self.receiver
		self.msg["Subject"] = "Forgot Password Request"
		body = "Reset password link: " + str(email_info["reset_password_link"])
		self.msg.attach(MIMEText(body, 'plain'))
 





	def make_html_email(self):
		try:
			if not Emailer.connected:
				self.connect()
			self.msg["To"] = self.receiver
			self.msg["Subject"] = "Making sure this works"
			body = """
				<b>This is an html email</b>
				<a href="https://stackoverflow.com/questions/882712/sending-html-email-using-python">Aperta aqui viado</a>
			"""
			self.msg.attach(MIMEText(body,'html'))
		except:
			self.disconnect()		


	def send_email(self):
		if Emailer.connected:    
			try:
				Emailer.connection.sendmail(self.emailer.user, self.receiver, self.msg.as_string())
			except SMTPRecipientsRefused as e:
				refused = e.recipients
				print("ERROR: "+str(e.recipients))
			else:
				print("EMAIL SENT SUCCESSFULLY")
				del self.msg
				self.msg = MIMEMultipart("alternative")
				self.msg['From'] = self.emailer.user
