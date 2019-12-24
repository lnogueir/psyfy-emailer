def request_accepted_template(user_package):
    return (
        """
            <html>
                <body style="font-size: 20px;overflow-x:hidden;">
                    <div>
                        <div style="display:flex;justify-content:space-between;">
                            <span style="font-size:22px;font-weight:900;">Hello {0},</span>
                            <img alt="PsyCare Logo" src="/bla"/>
                        </div>
                        <p style="padding: 5px 7.5px 7.5px 20px">
                            We are happy to say that your account has been aproved 
                            by our team and you are now a official PsyCare member!
                            <br><br>
                            <h3>Next steps:</h3>
                            <ol>
                                <li>Login to your account with this password: <i><b>{1}</b></i></li>
                                <li>Update your password on <a href="https://psycare.ca/manage_credentials">'Manage your credentials'</a></li>
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
                            </ol>
                            <br/>
                            Feel free to contact us about any concerns and/or any new features you would like to see on our platform.
                        </p>
                        <h4>Again, thanks for joining us!</h4>
                        <div>
                            <i>Best regards, PsyCare info team.</i>
                        </div>
                        <div style="display:flex;justify-content:space-between;">
                            <div style="display:flex; justify-content:flex-start">
                                <div style="margin-right:7.5px;">
                                    <a href=""></a>
                                </div>
                                <div style="margin-right:7.5px;">
                                    <a href="#"></a>
                                </div>
                                <div style="margin-right:7.5px;">
                                    <a href="#"></a>
                                </div>
                            </div>
                            <div>
                                <img src="bla"/>
                            </div>
                        </div>
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
