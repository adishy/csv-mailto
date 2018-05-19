import csv
from os.path import basename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import tkinter as tk
from tkinter import messagebox 

def read_csv_file(filename_provided, some_callback_provided):
	try:
		somefile = open(filename_provided, 'r')

		read_csv_provided = csv.reader(somefile)

		for some_row in read_csv_provided:
			some_callback_provided(some_row)

	except FileNotFoundError:
		messagebox.showerror("Error", "File not found in: " + filename_provided)
		print('File not found in: ' + filename_provided);

class EmailDetails:
	def __init__(self, 
				 receiver_email_address_provided, 
				 subject_text_provided, 
				 email_data_provided,
				 attachments_path_provided,
				 filepaths_provided):
		self.receiver_email_address = receiver_email_address_provided
		self.subject_text = subject_text_provided
		self.email_data = email_data_provided
		self.attachments_path = attachments_path_provided

		if self.attachments_path == 'Current directory':
			self.attachments_path = ''

		self.filepaths = filepaths_provided

class Emailer:
	def __del__(self):
		self.server.quit()

	def __init__(self, 
				sender_email_provided, 
				sender_password_provided, 
				smtp_server_provided = '',
				output_log_callback_provided = {}):
		self.sender_email = sender_email_provided
		self.sender_password = sender_password_provided
		self.smtp_server = smtp_server_provided

		self.output_log_callback = output_log_callback_provided

		self.server = ''

		self.login_smtp()

	def login_smtp(self):
		self.server = smtplib.SMTP(self.smtp_server)

		self.output_log_callback["OUTPUT_LOG_LOGGING_IN"](self.sender_email)

		self.server.ehlo()
		self.server.starttls()

		try:
			self.server.login(self.sender_email, 
							  self.sender_password)
			
			self.output_log_callback["OUTPUT_LOG_LOGGED_IN"]()

		except:

			self.output_log_callback["OUTPUT_LOG_LOGIN_ERROR"]()

	def create_msg_string(self, some_email_provided):
		msg = MIMEMultipart()
		msg['From'] = self.sender_email
		msg['To'] = some_email_provided.receiver_email_address
		msg['Subject'] = some_email_provided.subject_text

		while(len(some_email_provided.filepaths)):
			
			self.output_log_callback["OUTPUT_LOG_ATTACHING_FILE"](some_email_provided.filepaths[len(some_email_provided.filepaths) -1], 
																  some_email_provided.receiver_email_address)

			try:
				filepath = some_email_provided.attachments_path + '/' + some_email_provided.filepaths[len(some_email_provided.filepaths) -1]
				
				if some_email_provided.attachments_path == '':
					filepath = some_email_provided.filepaths[len(some_email_provided.filepaths) -1]

				some_file = open(filepath, 'rb')
				some_attach_data = MIMEApplication(some_file.read(), 
												   Name=basename(some_email_provided.filepaths[len(some_email_provided.filepaths) -1]))
				some_file.close()
				msg.attach(some_attach_data)
	
				self.output_log_callback["OUTPUT_LOG_ATTACHED_FILE"](some_email_provided.filepaths[len(some_email_provided.filepaths) -1], 
																	 some_email_provided.receiver_email_address)

			except FileNotFoundError:
				
				self.output_log_callback["OUTPUT_LOG_ATTACHING_FILE_ERROR"](some_email_provided.filepaths[len(some_email_provided.filepaths) -1], 
																			some_email_provided.receiver_email_address)

				print("File does not exist at: " + some_email_provided.filepaths[len(some_email_provided.filepaths) -1]) 

			some_email_provided.filepaths.pop()

		msg.attach(MIMEText(some_email_provided.email_data, 'html'))

		return msg.as_string()

	def send(self, some_email_provided):

		self.output_log_callback["OUTPUT_LOG_SENDING_RECIPIENT_EMAIL"](some_email_provided.receiver_email_address)

		try:
			self.server.sendmail(self.sender_email, 
								 some_email_provided.receiver_email_address, 
								 self.create_msg_string(some_email_provided))

			
			self.output_log_callback["OUTPUT_LOG_EMAIL_SEND"](some_email_provided.receiver_email_address)

		except:
			
			self.output_log_callback["OUTPUT_LOG_EMAIL_SEND_ERROR"](some_email_provided.receiver_email_address)
