import sys

import getpass 

from csvemail import *



def csvmail(USER_EMAIL, 
			USER_PASSWORD, 
			EMAIL_SMTP, 
			CSV_FILENAME, 
			EMAIL_SUBJECT, 
			EMAIL_CONTENT_FILENAME, 
			EMAIL_COLUMN,
			ATTACHMENTS_COLUMN, 
			SUBSTITUTIONS_IN_COLUMN):

	email_sender = Emailer(USER_EMAIL, 
						   USER_PASSWORD, 
						   EMAIL_SMTP)

	EMAIL_TEXT = 'Text'

	try:
		EMAIL_TEXT_FILE = open(EMAIL_CONTENT_FILENAME, 'r')
		EMAIL_TEXT = EMAIL_TEXT_FILE.read()

	except:
		print('Could not open file: ' + EMAIL_CONTENT_FILENAME)
		exit(1)

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