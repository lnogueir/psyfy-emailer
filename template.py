from templates.request_account import request_account_template
from templates.request_accepted import request_accepted_template
from templates.request_declined import request_declined_template
from templates.forgot_password import forgot_password_template


class Template:
    def __init__(self, email_type, user_package):
        self.subject = Template.TYPE_MAPPER[email_type]['subject']
        self.body = Template.TYPE_MAPPER[email_type]['body'](user_package)

    TYPE_MAPPER = {
        'REQUEST_ACCOUNT': {
            'body': request_account_template,
            'subject': 'New Account Request'
        },
        'REQUEST_DECLINED': {
            'body': request_declined_template,
            'subject': 'Your request has been declined'
        },
        'REQUEST_ACCEPTED': {
            'body': request_accepted_template,
            'subject': 'Your request has been accepted!'
        },
        'FORGOT_PASSWORD': {
            'body': forgot_password_template,
            'subject': 'Reset Password Request'
        }
    }
