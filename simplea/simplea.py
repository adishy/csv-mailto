from module1 import *

filename_provided = 'cnaj.csv'

EMAIL_SUBJECT = 'This is some subject'

EMAIL_TEXT = '<p>Hello {}<h1>This is some title</h1><a href=\'github.com/adishy\'>This is a link in the email</a>'

email_sender = Emailer('aditya.shylesh@hotmail.com', 
					   '1123581321345589_$RRs')

EMAIL_COLUMN = 0

NAME_COLUMN = 1

ATTACHMENTS_COLUMN = 2

def get_email_data(some_given_text):
	return str.format(EMAIL_TEXT, some_given_text)

def process_row_from_file_provided(some_row_provided):
	email_sender.send(EmailDetails(some_row_provided[EMAIL_COLUMN], 
								   EMAIL_SUBJECT,
								   get_email_data(some_row_provided[NAME_COLUMN]), 
								   some_row_provided[ATTACHMENTS_COLUMN].split(",")))
		

read_csv_file(filename_provided, process_row_from_file_provided)

print('Sent to recipients in file: ' + filename_provided)