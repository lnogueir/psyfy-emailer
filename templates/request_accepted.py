def request_accepted_template(user_package):
	return (
			"""
				<html>
					<body style="border:0.4px solid #c5cae9;border-radius:10px;padding:15px;">
						<div align="left" style="text-align:left;">
							<h2>Hello {}, you are officially a member of PsyCare!</h2>
							<p>We are happy to say that your account has been approved by our team!</p>
							<p>Your account is now available for <b>patients</b> to see.</p>
							<h3>Next steps:</h3>
							<ol>
								<li>Login to your account with this password: <i><b>{}</b></i></li>
								<li>Update your password on <a href="#">'Manage your credentials'</a></li>
								<li>On your <a href="#">Overview</a> confirm that your account contain the following info:<br/>
									<ul>
										<li><b>Full Name</b>: {}</li>
										<li><b>Contact Email</b>: {}</li>
										<li><b>Contact Number</b>: {}</li>
										<li><b>Clinic Address</b>: {}</li>
									</ul>
								</li> 
								<li>Add profile image and trailer video to catch patient's attention</li>
								<li>Set your available hours on your <a href="#">Calendar</a></li>
								<li>You are all set!</li>
							</ol>
							<hr/>
							<h4>Again, thanks for joining us!</h4>
							<p>
								<i>
									Best Regards,
									PsyCare Inc.
								</i>
							</p>
						</div>
					</body>
				</html>
			""".format(
					user_package['full_name'], 
					user_package['password'],
					user_package['full_name'],
					user_package['contact_email'],
					user_package['phone_number'],
					user_package['address']
			   )


