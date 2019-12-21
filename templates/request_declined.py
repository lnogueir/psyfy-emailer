def request_declined_template(user_package):
    return ("""
                <html>
                    <body style="font-size: 20px;overflow-x:hidden;">
                        <div style="background: url(https://raw.githubusercontent.com/lnogueir/psyfy-frontend/master/psyfy/src/assets/main_background.jpg);
                                height:35px; 
                                width: 100%;
                                padding: 20px 20px 29px 20px;
                                ">
                            <img src="https://raw.githubusercontent.com/lnogueir/psyfy-frontend/master/psyfy/src/assets/images/psycare_logo.png" 
                            style="height: 47.5px"/>   
                        </div>
                        <div>
                            <p style="padding: 5px 7.5px 7.5px 20px">
                                <span style="font-size:22px;font-weight:900;">Hello {0},</span>
                                <br/>
                                <br/>
                                We are sorry to inform you that your account request has been declined by our admission team.
                                <br/>
                                This decision may have been taken due to one or more of the following:
                                <ul>
                                    <li>Lack of information to determine truthfulness of your certification as a therapist.</li>
                                    <li>Your clinic location is not supported by our platform.</li>
                                    <li>Invalid and/or explicit content.</li>
                                </ul>
                                <br/>
                                If you disagree with the decision taken by our admission team, 
                                feel free to reply to this email with further information or try 
                                submitting another application at <a href="https://www.google.com/">psycare.ca</a>.
                            </p>
                            <h4>Thank you for your interest in PsyCare.</h4>
                            <div>
                                <i>Best regards, PsyCare info team.</i>
                            </div>    
                        </div>
                    </body>
                </html>""".format(user_package['full_name'])
            )
