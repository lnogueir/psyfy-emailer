def request_declined_template(user_package):
	return ("""
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
                                Hello {},
                                <br>
                                <br>
                                
                                We are sorry to inform you that your account request to PsyCare wasn't
                                accepted by our team . You can try to make a new request in the link below: 
                                <br>
                                <a href="google.com">psycare.com/accountrequest/</a>
                                <br>
                                
                                <hr/>
                                <i>
                                        Best regards, PsyCare Inc.
                                </i>
                            </div>
                    </body>
                </html>""".format(user_package['full_name'])

            )
