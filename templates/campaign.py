from templates.images import LOGO_ICON_BLUE
from templates.images import LOGO_RED
def campaign_template(user_package):
    return (
        f"""
            <html>
                <body style="font-size: 14px;overflow-x:hidden;">
                    <div>
                        <div style="display:flex;">
                            <span style="font-size:20px;font-weight:900;">Hello {user_package['full_name']},</span>
                            <img style="float:right;" alt="PsyCare Logo" style="width:150px;" src="{LOGO_RED}"/>
                        </div>
                        <p style="padding: 5px 7.5px 7.5px 20px">
                            Our names are Lucas and Jawad and we are the founders of PsyCare - a not for profit initiative, that helps connect people with therapists. <br/>
                            We started a website called psycare.ca, in hopes to make it easier for people struggling with mental health to get the care they need. <br/>
                            We noticed you are a reputable doctor and would love to have you on board as a beta tester on our site. You may be wondering why you should sign up? </br>
                            The answer to that is simple, you will be able to expand your practice, and help more people at the same time! And, best of all, our platform is completely free! <br/>
                            We are only allowing a <b>select few </b>therapists to join the platform, so make sure to sign up! <br/>
                            How'd you sign up? It is very easy and simple:
                            <ol>
                                <li>Go to the following site <ahref="https://psycare.ca">psycare.ca</a></li>
                                <li>Click the button labeled as 'Get Listed' on the top right</li>
                                <li>Fill out the form (you may skip 'About you' tab since we are aware of your certifications)</li>
                                <li>We will process your request within 24 hours, and then you're in!</li>
                            </ol>
                            We hope you sign, and support our initiative! If you have any question about signing up, our story, the initiative or any other questions, you can reply to this email, and we will get back to you
                        </p>
                        <h4>Again, thanks for joining us!</h4>
                        <div>
                            <div style="margin-bottom:5px;">
                                <img style="width:80px;" src="{LOGO_ICON_BLUE}"/>
                            </div>
                            <div align="left" style="margin-left:15px;margin-bottom:5px;">
                                <span style="font-weight:900;font-size:19px;">PsyCare Info Team</span>
                            </div>
                            <div style="margin-left:15px;">
                                <div style="display:flex; justify-content:flex-start">
                                    <div style="margin-right:7.5px;">
                                        <a style="color:#9fa8da;" href="https://psycare.ca">psycare.ca</a>
                                    </div>
                                    <div style="margin-right:7.5px;">|</div>
                                    <div style="margin-right:7.5px;">
                                        <a style="color:#9fa8da;" href="https://fb.me/psycareorg">Facebook</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </body>
            </html>
			"""
    )
