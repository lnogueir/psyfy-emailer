from templates.request_accepted import request_accepted_template

class Template:
	@classmethod
	def request_accepted(cls, user_package):
		return request_accepted_template(user_package)