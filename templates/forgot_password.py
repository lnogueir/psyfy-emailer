def forgot_password_template(user_package):
    return(

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
                        Hello {},
                        <br>
                        <br>
                        Somebody (hopefully you) requested a new password for your
                        PsyCare account. No changes where made to your account yet.
                        Please visit the link below to make a new password:
                        <br>
                        <a href="{}">Reset password link</a>
                        <br>
                        
                        
                        <hr/>
                        <i>
                                Best regards, PsyCare Inc.
                        </i>
                    </div>
            </body>
        </html>

        """.format(user_package['full_name'],user_package['reset_password_link'])

        )
