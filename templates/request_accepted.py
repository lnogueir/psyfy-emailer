def request_accepted_template(user_package):
	return (
			"""
	<html>


    <body style="font-size: 20px;">
        <div style="background: url(https://raw.githubusercontent.com/lnogueir/psyfy-frontend/master/psyfy/src/assets/main_background.jpg);
                     height:40px; 
                     width: 100%;
                     padding: 20px 20px 33px 20px;
                     
                     ">

        <img src="https://raw.githubusercontent.com/lnogueir/psyfy-frontend/master/psyfy/src/assets/images/psycare_logo.png" 
        style="height: 57px"/>   
        </div>
            <div style="padding-left: 20px">
                <br><br>
                Hello {0},
                <br>
                <br>
                We are happy to say that your account has been aproved 
                by our team and you are now a official PsyCare member!
                <br><br>
                Next steps:</h3>
							<ol>
								<li>Login to your account with this password: <i><b>{1}</b></i></li>
								<li>Update your password on <a href="#">'Manage your credentials'</a></li>
								<li>On your <a href="#">Overview</a> confirm that your account contain the following info:<br/>
									<ul>
										<li><b>Full Name</b>: {0}</li>
										<li><b>Contact Email</b>: {2}</li>
										<li><b>Contact Number</b>: {3}</li>
										<li><b>Clinic Address</b>: {4}</li>
									</ul>
								</li> 
								<li>Add profile image and trailer video to catch patient's attention</li>
								<li>Set your available hours on your <a href="#">Calendar</a></li>
								<li>You are all set!</li>

                
                <h4>Again, thanks for joining us!</h4>
                
                <hr/>
                <i>
                        Best regards, PsyCare Inc.
                </i>
            </div>
    </body>
</html>
			""".format(
					user_package['full_name'], 
					user_package['password'],
					user_package['contact_email'],
					user_package['phone_number'],
					user_package['address']
			   )
			)


