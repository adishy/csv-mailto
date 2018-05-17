import csv
from os.path import basename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
 
def read_csv_file(filename_provided, some_callback_provided):
	try:
		somefile = open(filename_provided, 'r')

		read_csv_provided = csv.reader(somefile)

		for some_row in read_csv_provided:
			some_callback_provided(some_row)

	except FileNotFoundError:
		print('File not found in: ' + filename_provided);

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
		self.email_send_close = False
		self.sender_email = sender_email_provided
		self.sender_password = sender_password_provided
		self.email_list = email_list_provided
		self.smtp_server = smtp_server_provided

		print("Logging in: " + self.sender_email)
		self.server = smtplib.SMTP(self.smtp_server)
		self.server.starttls()

		try:
			self.server.login(self.sender_email, 
							  self.sender_password)
			print("Logged in")
		except:
			print("Could not login with credentials provided")
	
	def close_send_emails(self):
		self.email_send_close = True

	def create_msg_string(self, some_email_provided):
		msg = MIMEMultipart()
		msg['From'] = self.sender_email
		msg['To'] = some_email_provided.receiver_email_address
		msg['Subject'] = some_email_provided.subject_text

		while(len(some_email_provided.filepaths)):
			print("Attaching file: " + some_email_provided.filepaths[len(some_email_provided.filepaths) -1] + " for recipient: " + some_email_provided.receiver_email_address)

			try:
				some_file = open(some_email_provided.filepaths[len(some_email_provided.filepaths) -1], 'rb')
				some_attach_data = MIMEApplication(some_file.read(), 
												   Name=basename(some_email_provided.filepaths[len(some_email_provided.filepaths) -1]))
				some_file.close()
				msg.attach(some_attach_data)
				print("Attached file: " + some_email_provided.filepaths[len(some_email_provided.filepaths) -1] + " for recipient: " + some_email_provided.receiver_email_address)

			except FileNotFoundError:
				print("Did not attach file: " + some_email_provided.filepaths[len(some_email_provided.filepaths) -1])
				print("File does not exist at: " + some_email_provided.filepaths[len(some_email_provided.filepaths) -1]) 
					   
			some_email_provided.filepaths.pop()

		msg.attach(MIMEText(some_email_provided.email_data, 'html'))

		return msg.as_string()

	def send(self, some_email_provided):
		print("Sending email to: " + some_email_provided.receiver_email_address)

		try:
			self.server.sendmail(self.sender_email, 
								 some_email_provided.receiver_email_address, 
								 self.create_msg_string(some_email_provided))
			print("Sent email to: " + some_email_provided.receiver_email_address)
		except:
			print("Could not send email to: " + some_email_provided.receiver_email_address)