import sys

import getpass 

from csvemail import *

from module2 import *

def csvmail(USER_EMAIL, 
			USER_PASSWORD, 
			EMAIL_SMTP, 
			CSV_FILENAME, 
			EMAIL_SUBJECT, 
			EMAIL_CONTENT_FILENAME, 
			EMAIL_COLUMN,
			ATTACHMENTS_PATH,
			ATTACHMENTS_COLUMN, 
			SUBSTITUTIONS_IN_COLUMN, 
			OUTPUT_LOG_FILENAME):

	FUNCTIONS_FOR_OUTPUT = csvoutputfunctions(OUTPUT_LOG_FILENAME)

	email_sender = ''

	try:
		email_sender = Emailer(USER_EMAIL, 
							   USER_PASSWORD, 
							   EMAIL_SMTP,
							   FUNCTIONS_FOR_OUTPUT.outputlogcallback)
	except:
		enable_select()
		return
		

	EMAIL_TEXT = 'Text'
	
	try:
		EMAIL_TEXT_FILE = open(EMAIL_CONTENT_FILENAME, 'r')
		EMAIL_TEXT = EMAIL_TEXT_FILE.read()

	except:
		print('Could not open file: ' + EMAIL_CONTENT_FILENAME)
		messagebox.showerror("Error", "Could not open: " + EMAIL_CONTENT_FILENAME)
		enable_select()
		return

	def get_email_content(EMAIL_TEXT_PROVIDED, SUBSTITUTIONS_PROVIDED, SOME_ROW_PROVIDED):
		for i in SUBSTITUTIONS_PROVIDED:
			if i[0] == '':
				continue

			EMAIL_TEXT_PROVIDED = EMAIL_TEXT_PROVIDED.replace(i[0].get(), 
															  SOME_ROW_PROVIDED[int(i[1].get())])

		return EMAIL_TEXT_PROVIDED

	def process_row_from_file_provided(some_row_provided):
		email_sender.send(EmailDetails(some_row_provided[EMAIL_COLUMN], 
									   EMAIL_SUBJECT,
									   get_email_content(EMAIL_TEXT, SUBSTITUTIONS_IN_COLUMN, some_row_provided),
									   ATTACHMENTS_PATH,
									   some_row_provided[ATTACHMENTS_COLUMN].split(",")))
		
	read_csv_file(CSV_FILENAME, process_row_from_file_provided)

	FUNCTIONS_FOR_OUTPUT.OUTPUT_FILE.close()

	enable_select()

	#globals()['root'].nametowidget('emailsend.email')['state'] = tk.NORMAL
	#globals()['root'].nametowidget('csvfileselectframe.csvfileselect')['state'] = tk.NORMAL
	#globals()['root'].nametowidget('emaildataframe.emaildatafileselect')['state'] = tk.NORMAL
	#globals()['root'].nametowidget('attachmentfilenameframe.attachmentfilenameselect')['state'] = tk.NORMAL
	#globals()['root'].nametowidget('substitutionsframe.substitutions')['state'] = tk.NORMAL
	#globals()['root'].nametowidget('outputlogframe.outputlogfilenameselect')['state'] = tk.NORMAL