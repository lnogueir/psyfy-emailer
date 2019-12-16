from templates.request_accepted import request_accepted_template
from templates.request_declined import request_declined_template
from templates.forgot_password import forgot_password_template


class Template:
	
	def request_declined(user_package):
                return request_declined_template(user_package)
	def forgot_password(user_package):
                return forgot_password_template(user_package)
	def request_accepted(user_package):
                return request_accepted_template(user_package)
       
	
        
