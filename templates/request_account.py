def request_account_template(user_package):
    return (
        """
            <html>
                <body style="font-size: 20px;overflow-x:hidden;">
                    <div>
                        <p style="padding: 5px 7.5px 7.5px 20px;">
                            <span style="font-size:22px;font-weight:900;">User Package:</span>
                            <ul>
                                <li>Name: {0} <br/></li>
                                <li>Email: {1}</li>
                                <li>Contact Number: {2}</li>
                                <li>Clinic Address: {3}</li>
                                <li>About: {4}</li>
                            </ul>
                            <span style="font-size:22px;font-weight:900;">Decision:</span>
                            <ol>
                                <li><a href="{5}">Accept</a></li>
                                <li><a href="{6}">Deny</a></li>
                            </ol>
                        </p>
                        <div>
                            <i>PsyCare info team.</i>
                        </div>
                    </div>
                </body>
            </html>
			""".format(
            user_package['full_name'],
            user_package['contact_email'],
            user_package['phone_number'],
            user_package['address'],
            user_package['about'],
            user_package['accept'],
            user_package['deny']
        )
    )
