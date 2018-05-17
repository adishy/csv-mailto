import csv

from threading import Thread

from module1 import *



filename_provided = 'cnaj.csv'

email_subject = 'Some text here'

text = 'Hello {}, Some text'

email_sender = Emailer("aditya.shylesh@hotmail.com", 
				"1123581321345589_$RRs")

send_emails_from_details = Thread(target = email_sender.send_emails, 
			   args = ())

send_emails_from_details.start()

def get_email_data(some_given_text):
	return str.format(text, some_given_text)

def process_row_from_file_provided(some_row_provided):
	email_sender.add_email(EmailDetails(some_row_provided[0], 
										email_subject, 
										get_email_data(some_row_provided[1]), 
										[some_row_provided[2]]))

def read_csv_file(filename_provided, some_callback_provided):
	try:
		somefile = open(filename_provided, 'r')

		read_csv_provided = csv.reader(somefile)

		for some_row in read_csv_provided:
			some_callback_provided(some_row)

	except FileNotFoundError:
		print("File not found in specified path");
		



#jsnvdjks = EmailProvided("aditya.shylesh@hotmail.com", 
#					     "1123581321345589_$RRs", 
#					     "aditya.manjushashylesh@gmail.com", 
#					     "bksdjf", 
#					     "kjdsgbskdjgb", 
#					     "")

#jsnvdjks.sendEmail()

#fnjds.add_email(EmailDetails("aditya.manjushashylesh@gmail.com", "jndskfnsd", "fknskdjfnksjd", ['kjsdv.pdf']))

read_csv_file(filename_provided, process_row_from_file_provided)
