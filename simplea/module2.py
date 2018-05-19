import tkinter as tk
from tkinter import messagebox
OUTPUT_LOG_WINDOW = ''

OUTPUT_LOG_FRAME = ''

OUTPUT_LOG_RECIPIENT_LIST = ''

def outputlog_start_window():
	globals()['OUTPUT_LOG_WINDOW'] = tk.Toplevel()
	globals()['OUTPUT_LOG_WINDOW'].grab_set()

	globals()['OUTPUT_LOG_FRAME'] = tk.Frame(globals()['OUTPUT_LOG_WINDOW'], 
											 height = 4, 
											 width = 5, 
											 bd = 1, 
											 padx=4, 
											 pady=4)

	globals()['OUTPUT_LOG_FRAME'].pack(fill=tk.BOTH)

	globals()['OUTPUT_LOG_RECIPIENT_LIST'] = tk.Listbox(globals()['OUTPUT_LOG_WINDOW'])

	globals()['OUTPUT_LOG_RECIPIENT_LIST'].pack(fill=tk.BOTH)


def outputlog_logging_in(sender_email_provided):
	#print("Logging in: " + sender_email_provided)

	OUTPUT_LOG_LOGGING_IN_FRAME = tk.Frame(globals()['OUTPUT_LOG_FRAME'], 
										   height = 4, 
										   width = 5, 
										   bd = 1, 
										   padx=4, 
										   pady=4)

	OUTPUT_LOG_LOGGING_IN_FRAME.pack(fill=tk.BOTH)

	tk.Label(OUTPUT_LOG_LOGGING_IN_FRAME, 
			 text= "Logging in " + sender_email_provided).pack(side = tk.LEFT)


def outputlog_logged_in():
	#print("Logged in")
	OUTPUT_LOG_LOGGED_IN_FRAME = tk.Frame(globals()['OUTPUT_LOG_FRAME'], 
										   height = 4, 
										   width = 5, 
										   bd = 1, 
										   padx=4, 
										   pady=4)

	OUTPUT_LOG_LOGGED_IN_FRAME.pack(fill=tk.BOTH)

	tk.Label(OUTPUT_LOG_LOGGED_IN_FRAME, 
			 text= "Logged in").pack(side = tk.LEFT)

def outputlog_login_error():
	#print("Could not login with credentials provided")
	messagebox.showerror("Error", "Could not login with credentials provided")

def outputlog_attaching_file(filename_provided, recipient_email_provided):
	#print("Attaching file: " + filename_provided + " for recipient: " + recipient_email_provided)
	globals()['OUTPUT_LOG_RECIPIENT_LIST'].insert(tk.END, "Attaching file: " + filename_provided + " for recipient: " + recipient_email_provided)

def outputlog_attached_file(filename_provided, recipient_email_provided):
	#print("Attached file: " + filename_provided + " for recipient: " + recipient_email_provided)
	globals()['OUTPUT_LOG_RECIPIENT_LIST'].insert(tk.END, "Attached file: " + filename_provided + " for recipient: " + recipient_email_provided)

def outputlog_attaching_file_error(filename_provided, recipient_email_provided):
	#print("Did not attach file: " + filename_provided + " for recipient: " + recipient_email_provided)
	globals()['OUTPUT_LOG_RECIPIENT_LIST'].insert(tk.END, "Did not attach file: " + filename_provided + " for recipient: " + recipient_email_provided)
	
def outputlog_sending_recipient_email(recipient_email_provided):
	#print("Sending email to: " + recipient_email_provided)
	globals()['OUTPUT_LOG_RECIPIENT_LIST'].insert(tk.END, "Sending email to: " + recipient_email_provided)

def outputlog_email_send(recipient_email_provided):
	#print("Sent email to: " + recipient_email_provided)
	globals()['OUTPUT_LOG_RECIPIENT_LIST'].insert(tk.END, "Sent email to: " + recipient_email_provided)

def outputlog_email_send_error(recipient_email_provided):
	#print("Could not send email to: " + recipient_email_provided)
	globals()['OUTPUT_LOG_RECIPIENT_LIST'].insert(tk.END, "Could not send email to: " + recipient_email_provided)

outputlogcallback = {"OUTPUT_LOG_START_WINDOW" : outputlog_start_window,
					 "OUTPUT_LOG_LOGGING_IN" : outputlog_logging_in, 
					 "OUTPUT_LOG_LOGGED_IN" : outputlog_logged_in,
					 "OUTPUT_LOG_LOGIN_ERROR" : outputlog_login_error,
					 "OUTPUT_LOG_ATTACHING_FILE" : outputlog_attaching_file,
					 "OUTPUT_LOG_ATTACHED_FILE" : outputlog_attached_file,
					 "OUTPUT_LOG_ATTACHING_FILE_ERROR" : outputlog_attaching_file_error,
					 "OUTPUT_LOG_SENDING_RECIPIENT_EMAIL" : outputlog_sending_recipient_email,
					 "OUTPUT_LOG_EMAIL_SEND" : outputlog_email_send,
					 "OUTPUT_LOG_EMAIL_SEND_ERROR" : outputlog_email_send_error}

