from os.path import basename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
 
class EmailDetails:
    def __init__(self, 
                 receiver_email_address_provided, 
                 subject_text_provided, 
                 email_data_provided,
                 filepaths_provided):
        self.receiver_email_address = receiver_email_address_provided
        self.subject_text = subject_text_provided
        self.email_data = email_data_provided
        self.filepaths = filepaths_provided

class Emailer:
    def __del__(self):
        self.server.quit()

    def __init__(self, 
                sender_email_provided, 
                sender_password_provided, 
                email_list_provided = [], 
                smtp_server_provided = 'smtp-mail.outlook.com:587'):
        self.sender_email = sender_email_provided
        self.sender_password = sender_password_provided
        self.email_list = email_list_provided
        self.smtp_server = smtp_server_provided

        print("Logging in: " + self.sender_email)
        self.server = smtplib.SMTP(self.smtp_server)
        self.server.starttls()
        self.server.login(self.sender_email, 
                          self.sender_password)
        print("Logged in")

    def create_msg_string(self, some_email_provided):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = some_email_provided.receiver_email_address
        msg['Subject'] = some_email_provided.subject_text

        while(len(some_email_provided.filepaths)):
            print("Attaching file: " + some_email_provided.filepaths[len(some_email_provided.filepaths) -1])
            some_file = open(some_email_provided.filepaths[len(some_email_provided.filepaths) -1], 'rb')
            some_attach_data = MIMEApplication(some_file.read(), Name=basename(some_email_provided.filepaths[len(some_email_provided.filepaths) -1]))
            some_file.close()
            msg.attach(some_attach_data)
            some_email_provided.filepaths.pop()

        msg.attach(MIMEText(some_email_provided.email_data, 'plain'))

        return msg.as_string()

    def send(self, some_email_provided):
        self.server.sendmail(self.sender_email, 
                             some_email_provided.receiver_email_address, 
                             self.create_msg_string(some_email_provided))

    def add_email(self, some_email_provided):
        print("Added email recipient: " + some_email_provided.receiver_email_address)
        self.email_list.append(some_email_provided)


    def send_emails(self):

        while(True):
            while(len(self.email_list)):
                print("Sending email to: " + self.email_list[len(self.email_list) -1].receiver_email_address)
                try:
                    self.send(self.email_list[len(self.email_list) - 1])
                    print("Sent email to: " + self.email_list[len(self.email_list) -1].receiver_email_address)
                except:
                    print("Email could not be sent to: " + self.email_list[len(self.email_list) -1].receiver_email_address)
                self.email_list.pop()

class EmailProvided:
    def __init__(self, 
                 sender_email_address_provided, 
                 sender_password_provided, 
                 receiver_email_address_provided, 
                 subject_text_provided, 
                 email_data_provided, 
                 filepaths_provided, 
                 smtp_server_provided = 'smtp-mail.outlook.com:587'):
        self.sender_email_address = sender_email_address_provided
        self.sender_email_password = sender_password_provided
        self.receiver_email_address = receiver_email_address_provided
        self.subject_text = subject_text_provided
        self.email_data = email_data_provided
        self.filepaths = filepaths_provided
        self.SMTP_server = smtp_server_provided

        server = smtplib.SMTP(self.SMTP_server)
        server.starttls()
        server.login(self.sender_email_address, 
                     self.sender_email_password)

    def create_msg_string(self):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email_address
        msg['To'] = self.receiver_email_address
        msg['Subject'] = self.subject_text
        msg.attach(MIMEText(self.email_data, 'plain'))

        return msg.as_string()

    def sendEmail(self):
        
        server.sendmail(self.sender_email_address, 
                        self.receiver_email_address, 
                        self.create_msg_string())

        server.quit()

