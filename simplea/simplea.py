import sys

import getpass 

from csvemail import *

#EXAMPLE: <executable_path> somedetails.csv email_content.html "Some text" aditya.shylesh@hotmail.com 0 1 2

if len(sys.argv) != 8:
	print('Usage: <executable> \
				  <CSV-FILE> \
				  <EMAIL-CONTENT-FILE> \
				  <EMAIL-SUBJECT-STRING> \
				  <EMAIL-SENDER-ADDRESS> \
				  <RECIPIENT-EMAIL-COLUMN> \
				  <RECIPIENT-NAME-COLUMN> \
				  <RECIPIENT-ATTACHMENT-PATH-COLUMN>')


filename_provided = sys.argv[1]

EMAIL_TEXT_FILENAME = sys.argv[2]

EMAIL_SUBJECT = sys.argv[3]

EMAIL_SENDER_ADDRESS = sys.argv[4]

EMAIL_TEXT = 'Text'

try:
	EMAIL_TEXT_FILE = open(EMAIL_TEXT_FILENAME, 'r')
	EMAIL_TEXT = EMAIL_TEXT_FILE.read()

except:
	print('Could not open file: ' + EMAIL_TEXT_FILENAME)
	exit(1)

print("Login for: "  + EMAIL_SENDER_ADDRESS)

EMAIL_SENDER_PASSWORD = getpass.getpass()

email_sender = Emailer(EMAIL_SENDER_ADDRESS, 
					   EMAIL_SENDER_PASSWORD)

EMAIL_COLUMN = int(sys.argv[5])

NAME_COLUMN = int(sys.argv[6])

ATTACHMENTS_COLUMN = int(sys.argv[7])

COLUMN_SUBSTITUTION = '<employee-name>'

ROWS_IN_FILE_PROVIDED = 0

def process_row_from_file_provided(some_row_provided):
	globals()['ROWS_IN_FILE_PROVIDED'] = globals()['ROWS_IN_FILE_PROVIDED'] + 1

	email_sender.send(EmailDetails(some_row_provided[EMAIL_COLUMN], 
								   EMAIL_SUBJECT,
								   EMAIL_TEXT.replace(COLUMN_SUBSTITUTION, some_row_provided[NAME_COLUMN]), 
								   some_row_provided[ATTACHMENTS_COLUMN].split(",")))
		

read_csv_file(filename_provided, process_row_from_file_provided)

print('Sent to: ' + str(ROWS_IN_FILE_PROVIDED) + ' recipients in file: ' + filename_provided)