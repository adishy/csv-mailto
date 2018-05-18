import sys

import getpass 

from csvemail import *

def outputlog_logging_in(sender_email_provided):
	print("Logging in: " + sender_email_provided)

def outputlog_logged_in():
	print("Logged in")

def outputlog_login_error():
	print("Could not login with credentials provided")

def outputlog_attaching_file(filename_provided, recipient_email_provided):
	print("Attaching file: " + filename_provided + " for recipient: " + recipient_email_provided)

def outputlog_attached_file(filename_provided, recipient_email_provided):
	print("Attached file: " + filename_provided + " for recipient: " + recipient_email_provided)

def outputlog_attaching_file_error(filename_provided, recipient_email_provided):
	print("Did not attach file: " + filename_provided + " for recipient: " + recipient_email_provided)

def outputlog_sending_recipient_email(recipient_email_provided):
	print("Sending email to: " + recipient_email_provided)

def outputlog_email_send(recipient_email_provided):
	print("Sent email to: " + recipient_email_provided)

def outputlog_email_send_error(recipient_email_provided):
	print("Could not send email to: " + recipient_email_provided)

outputlogcallback = {"OUTPUT_LOG_LOGGING_IN" : outputlog_logging_in, 
			         "OUTPUT_LOG_LOGGED_IN" : outputlog_logged_in,
			         "OUTPUT_LOG_LOGIN_ERROR" : outputlog_login_error,
			         "OUTPUT_LOG_ATTACHING_FILE" : outputlog_attaching_file,
			         "OUTPUT_LOG_ATTACHED_FILE" : outputlog_attached_file,
			         "OUTPUT_LOG_ATTACHING_FILE_ERROR" : outputlog_attaching_file_error,
			         "OUTPUT_LOG_SENDING_RECIPIENT_EMAIL" : outputlog_sending_recipient_email,
			         "OUTPUT_LOG_EMAIL_SEND" : outputlog_email_send,
			         "OUTPUT_LOG_EMAIL_SEND_ERROR" : outputlog_email_send_error}

def csvmail(USER_EMAIL, 
			USER_PASSWORD, 
			EMAIL_SMTP, 
			CSV_FILENAME, 
			EMAIL_SUBJECT, 
			EMAIL_CONTENT_FILENAME, 
			EMAIL_COLUMN,
			ATTACHMENTS_COLUMN, 
			SUBSTITUTIONS_IN_COLUMN, OUTPUT_LOG_FILENAME):

	email_sender = Emailer(USER_EMAIL, 
						   USER_PASSWORD, 
						   EMAIL_SMTP, outputlogcallback)

	EMAIL_TEXT = 'Text'

	try:
		EMAIL_TEXT_FILE = open(EMAIL_CONTENT_FILENAME, 'r')
		EMAIL_TEXT = EMAIL_TEXT_FILE.read()

	except:
		print('Could not open file: ' + EMAIL_CONTENT_FILENAME)

	def get_email_content(EMAIL_TEXT_PROVIDED, SUBSTITUTIONS_PROVIDED, SOME_ROW_PROVIDED):
		for i in SUBSTITUTIONS_PROVIDED:
			EMAIL_TEXT_PROVIDED = EMAIL_TEXT_PROVIDED.replace(i[0].get(), 
															  SOME_ROW_PROVIDED[int(i[1].get())])

		return EMAIL_TEXT_PROVIDED

	def process_row_from_file_provided(some_row_provided):
		email_sender.send(EmailDetails(some_row_provided[EMAIL_COLUMN], 
									   EMAIL_SUBJECT,
									   get_email_content(EMAIL_TEXT, SUBSTITUTIONS_IN_COLUMN, some_row_provided), 
									   some_row_provided[ATTACHMENTS_COLUMN].split(",")))
		

	read_csv_file(CSV_FILENAME, process_row_from_file_provided)