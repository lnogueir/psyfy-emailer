import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, jsonify, redirect, render_template
import os
from os.path import join, dirname, realpath

UPLOADS_PATH = join(dirname(realpath(__file__)), '/Users/Andre_1/Documents/Flask Files/uploads' )
UPLOAD_FOLDER = '/Users/Andre_1/Documents/Flask Files/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Emailer():   # Needs the receiver email to know where to send the message

    def __init__(self,receiver_email):

        self.receiver_email = receiver_email
        self.sender_email = "andrenetto@poli.ufrj.br"
        self.password = "mypassword123" ###################### EMAIL PASSWORD #################
    
        #Setting defalut message:
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "Email teste vindo do python"
        self.message["From"] = self.sender_email
        self.message["To"] = receiver_email 
        self.message.attach( MIMEText( "Email automatico vindo do python" , "plain") )

    def addAttachment(self,path):
        with open(path, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)
            # Add header as key/value pair to attachment part
            part.add_header( "Content-Disposition",  f"attachment; filename= {path}" )
            self.message.attach(part)  # Adding attachment to the message

    def connect(self):
        context = ssl.create_default_context()
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
        self.server.login(sender_email, password)
                    
    def sendEmail(self):
        text= self.message.as_string()
        self.server.sendmail(self.sender_email, self.receiver_email, text)
        print("Message Sent! ")
    



@app.route("/upload_image", methods = ["POST","GET"])
def upload_image():
    
    if request.method == "POST":

            print("Sending email...")
            files = request.files.getlist("files[]") # List of files coming from React

            emailer = Emailer("andrenetto@poli.ufrj.br")
            
            #Adding all files in the message:
            for file in files:  
                filePath = '/Users/Andre_1/Documents/Flask Files/uploads/'+ file.filename #Getting the image path
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))       #Saving the image in the "uploads" folder
                emailer.addAttachment( filePath ) #Addding file attachment
                    
            # Loging in and sending the message:
            emailer.connect()
            emailer.sendEmail()
        
            return "Success in saving the File"
            
    return "SUCCESS!!"

if __name__ == "__main__":
    app.run(debug = True)