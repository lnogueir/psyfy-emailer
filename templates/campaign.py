from templates.images import LOGO_ICON_BLUE
from templates.images import LOGO_RED


def campaign_template(user_package):
    return (
        f"""
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml"
                xmlns:v="urn:schemas-microsoft-com:vml"
                xmlns:o="urn:schemas-microsoft-com:office:office">
                <head>
                <!--[if gte mso 9]><xml>
                <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
                </xml><![endif]-->
                <title>PsyCare</title>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0 " />
                <meta name="format-detection" content="telephone=no"/>
                <!--[if !mso]><!-->
                <link href="https://fonts.googleapis.com/css?family=Lato:100,100i,300,300i,400,700,700i,900,900i" rel="stylesheet" />
                <!--<![endif]-->
                </head>
                <body style="font-size: 15px;overflow-x:hidden;">
                    <div>
                        <div style="margin-top:20px;">
                            <img style="width:230px;" src="{LOGO_RED}"/>
                        </div>
                        <div style="margin-left:15px;">
                            <div style="margin-top:20px;font-size:20px;font-weight:900;">Hello {user_package['full_name']},</div>
                            <p style="padding: 5px 7.5px 7.5px 20px;line-height:25px;">
                                Our names are Lucas and Jawad and we are the founders of PsyCare - a not for profit initiative, that helps connect people with therapists. <br/>
                                We started a website called psycare.ca, in hopes to make it easier for people struggling with mental health to get the care they need. <br/>
                                We noticed you are a reputable doctor and would love to have you on board as a beta tester on our site. You may be wondering why you should sign up? </br>
                                The answer to that is simple, you will be able to expand your practice, and help more people at the same time! And, best of all, our platform is completely free! <br/>
                                We are only allowing a <b>select few </b>therapists to join the platform, so make sure to sign up! <br/>
                                How'd you sign up? It is very easy and simple: <br/>
                                &nbsp;&nbsp;1.&nbsp;Visit our website <a href="https://psycare.ca"><b>psycare.ca</b></a><br/>
                                &nbsp;&nbsp;2.&nbsp;Click the button labeled as 'Get Listed' on the top right.<br/>
                                &nbsp;&nbsp;3.&nbsp;Fill out the form (you may skip 'About you' tab since we are aware of your certifications).<br/>
                                &nbsp;&nbsp;4.&nbsp;We will process your request within 24 hours, and then you're in!<br/>
                                <br/>
                                We hope you sign, and support our initiative! 
                                <br/>
                                If you have any question about signing up, <b>our story</b>, the initiative or any other questions, you can reply to this email, and we will get back to you as soon as possible.
                                <br/><br/>
                                <b style="font-size:18px;">Thanks!</b>
                            </p> 
                            <div style="display:flex;">
                                <div style="margin-bottom:5px;">
                                    <img alt="PsyCare Logo" style="width:80px;" src="{LOGO_ICON_BLUE}"/>
                                </div>
                                <div style="margin-left:15px;margin-top:14px;">
                                    <div align="left" style="margin-bottom:5px;">
                                        <span style="font-weight:900;font-size:19px;">PsyCare Info Team</span>
                                    </div>
                                    <div>
                                        <div style="display:flex; justify-content:flex-start">
                                            <div style="margin-right:7.5px;">
                                                <a style="color:#9fa8da;" href="https://psycare.ca">psycare.ca</a>
                                            </div>
                                            <div style="margin-right:7.5px;">|</div>
                                            <div style="margin-right:7.5px;">
                                                <a style="color:#9fa8da;" href="https://fb.me/psycareorg">Facebook</a>
                                            </div>
                                            <div style="margin-right:7.5px;">|</div>
                                            <div style="margin-right:7.5px;">
                                                <a href="https://www.linkedin.com/company/psycare-org">
                                                    LinkedIn
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </body>
            </html>
			"""
    )
