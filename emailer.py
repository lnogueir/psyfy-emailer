from smtplib import SMTP, SMTPResponseException, SMTPRecipientsRefused
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from template import Template
import os


class Emailer:
    connected = False
    connection = None

    def __init__(self, user_email, password, receiver=None):
        self.account = Emailer.Account(user_email, password)
        self.msg = None
        self.receiver = receiver

    def run(self, email_type, user_package, logger=None):
        self.msg = MIMEMultipart("alternative")
        self.msg['From'] = f'PsyCare <{self.account.user}>'
        try:
            self.connect()
            self.make_email(email_type, user_package)
            self.send_email()
        except SMTPResponseException as e:
            error_code = e.smtp_code
            error_message = e.smtp_error
            if logger:
                logger.info(
                    f'CONNECTION ERROR: SMTP CONNECTION FAILED: {error_message}, CODE: {error_code}\n\n')
        except ConnectionAbortedError:
            if logger:
                logger.info(
                    f'CONNECTION ERROR: ATTEMPT TO OVERRIDE EXISTING CONNECTING - {user_package}\n\n')
        except SMTPRecipientsRefused:
            if logger:
                logger.info(
                    f'ERROR SENDING: INVALID RECEIVER - {self.receiver}\n\n')
        except TypeError:
            if logger:
                logger.info(
                    f'ERROR SENDING: INVALID USER PACKAGE - {user_package}\n\n')
        except ConnectionError:
            if logger:
                logger.info(
                    f'ERROR SENDING: ATTEMPT TO SEND MESSAGE WITH NO CONNECTION - {user_package}\n\n')
        else:
            if logger:
                logger.info(
                    f'EMAIL SENT SUCCESSFULLY: USER PACKAGE - {user_package}\n\n')
            return True
        finally:
            self.disconnect()
        return False

    def connect(self):
        if not Emailer.connected:
            try:
                connection = SMTP(os.getenv('SMTP_SERVER_ADDRESS'), 587)
                connection.ehlo()
                connection.starttls()
                connection.login(self.account.user, self.account.password)
            except SMTPResponseException as e:
                raise e
            else:
                Emailer.connected = True
                Emailer.connection = connection
        else:
            self.disconnect()
            raise ConnectionAbortedError

    @classmethod
    def disconnect(cls):
        if cls.connected:
            cls.connection.close()
            cls.connected = False

    def add_attachment(self, file):
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file['base64'])
        part.add_header('Content-Transfer-Encoding', 'base64')
        part['Content-Disposition'] = 'attachment; filename="%s"' % file['fileName']
        self.msg.attach(part)

    def make_email(self, email_type, user_package):
        for key in user_package:
            if ('files' != key and
                str != type(user_package[key]) and
                int != type(user_package[key]) and
                    float != type(user_package[key])):
                raise TypeError
        self.receiver = user_package['contact_email'] if email_type != 'REQUEST_ACCOUNT' else self.account.user
        self.msg["To"] = self.receiver
        template = Template(email_type, user_package)
        self.msg["Subject"] = template.subject
        if 'files' in user_package:
            for file in user_package['files']:
                self.add_attachment(file)
        self.msg.attach(MIMEText(template.body, 'html'))

    def send_email(self):
        if Emailer.connected:
            try:
                Emailer.connection.sendmail(
                    self.account.user, self.receiver, self.msg.as_string())
            except SMTPRecipientsRefused as e:
                raise e
            else:
                del self.msg
        else:
            raise ConnectionError

    class Account:
        def __init__(self, user_email, password):
            self.user = user_email
            self.password = password
