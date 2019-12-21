def forgot_password_template(user_package):
    return(
        """
        <html>
            <body style="font-size: 20px;overflow-x:hidden;">
                <div style="background: url(https://raw.githubusercontent.com/lnogueir/psyfy-frontend/master/psyfy/src/assets/main_background.jpg);
                            height:35px; 
                            width: 100%;
                            padding: 20px 20px 31px 20px;
                            ">
                    <img src="https://raw.githubusercontent.com/lnogueir/psyfy-frontend/master/psyfy/src/assets/images/psycare_logo.png" 
                    style="height: 47.5px"/>   
                </div>
                <div>
                    <p style="padding: 5px 7.5px 7.5px 20px;">
                        <span style="font-size:22px;font-weight:900;">Hello {},</span>
                        <br/>
                        A reset password request has been made for your account. <br/>
                        Please visit the link below to reset your password:<br/>
                        <a href="{}">Reset Password</a>
                    </p>
                    <div>
                        <i>PsyCare info team.</i>
                    </div>
                </div>
            </body>
        </html>

        """.format(user_package['full_name'], user_package['reset_password_link'])

    )
