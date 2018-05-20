import csv
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.resizable(False, False)
root.title('CSV Mailto')

class csvoutputfunctions:
	def __del__ (self):
		self.OUTPUT_FILE.close()

	def __init__(self, some_filename_provided):
		self.OUTPUT_FILENAME = some_filename_provided

		self.OUTPUT_FILE = open(self.OUTPUT_FILENAME, 'a')

		self.OUTPUT_FILE_WRITE = csv.writer(self.OUTPUT_FILE, delimiter = ',')

		self.OUTPUT_FILE_ROW = []

		self.OUTPUT_LOG_RECIPIENT_LIST = globals()['root'].nametowidget('outputloglistframe.list')

		self.OUTPUT_LOG_RECIPIENT_LIST.pack(fill=tk.BOTH)

		self.outputlogcallback = {"OUTPUT_LOG_LOGGING_IN" : self.outputlog_logging_in, 
								  "OUTPUT_LOG_LOGGED_IN" : self.outputlog_logged_in,
								  "OUTPUT_LOG_LOGIN_ERROR" : self.outputlog_login_error,
								  "OUTPUT_LOG_ATTACHING_FILE" : self.outputlog_attaching_file,
								  "OUTPUT_LOG_ATTACHED_FILE" : self.outputlog_attached_file,
								  "OUTPUT_LOG_ATTACHING_FILE_ERROR" : self.outputlog_attaching_file_error,
								  "OUTPUT_LOG_SENDING_RECIPIENT_EMAIL" : self.outputlog_sending_recipient_email,
								  "OUTPUT_LOG_EMAIL_SEND" : self.outputlog_email_send,
								  "OUTPUT_LOG_EMAIL_SEND_ERROR" : self.outputlog_email_send_error}


	def outputlog_start_window():
		print("kskdjnf")
		
	def outputlog_logging_in(self, sender_email_provided):
		print("Logging in: " + sender_email_provided)

		self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, "Logging in: " + sender_email_provided)


	def outputlog_logged_in(self):
			print("Logged in")
			self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, "Logged in")

	def outputlog_login_error(self):
			print("Could not login with credentials provided")
			messagebox.showerror("Error", "Could not login with credentials provided")

	def outputlog_attaching_file(self, filename_provided, recipient_email_provided):
			print("Attaching file: " + filename_provided + " for recipient: " + recipient_email_provided)
			#self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, "Attaching file: " + filename_provided + " for recipient: " + recipient_email_provided)

	def outputlog_attached_file(self, filename_provided, recipient_email_provided):
			print("Attached file: " + filename_provided + " for recipient: " + recipient_email_provided)
			#self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, "Attached file: " + filename_provided + " for recipient: " + recipient_email_provided)
			self.OUTPUT_FILE_ROW.append('Attached file')

	def outputlog_attaching_file_error(self, filename_provided, recipient_email_provided):
			print("Did not attach file: " + filename_provided + " for recipient: " + recipient_email_provided)
			#self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, "Did not attach file: " + filename_provided + " for recipient: " + recipient_email_provided)
			self.OUTPUT_FILE_ROW.append('Did not attach file: ' + filename_provided)

	def outputlog_sending_recipient_email(self, recipient_email_provided):
			print("Sending email to: " + recipient_email_provided)
			#self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, "Sending email to: " + recipient_email_provided)
			self.OUTPUT_FILE_ROW.append(recipient_email_provided)

	def outputlog_email_send(self, recipient_email_provided):
			print("Sent email to: " + recipient_email_provided)
			#self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, "Sent email to: " + recipient_email_provided)
			self.OUTPUT_FILE_ROW.append('Sent')
			print(self.OUTPUT_FILE_ROW)
			self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, '   '.join(self.OUTPUT_FILE_ROW))
			self.OUTPUT_FILE_WRITE.writerow(self.OUTPUT_FILE_ROW)
			self.OUTPUT_FILE.flush()
			self.OUTPUT_FILE_ROW = []

	def outputlog_email_send_error(self, recipient_email_provided):
			print("Could not send email to: " + recipient_email_provided)
			#self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, "Could not send email to: " + recipient_email_provided)
			self.OUTPUT_FILE_ROW.append('Not sent')
			print(self.OUTPUT_FILE_ROW)
			self.OUTPUT_LOG_RECIPIENT_LIST.insert(tk.END, '   '.join(self.OUTPUT_FILE_ROW))
			self.OUTPUT_FILE_WRITE.writerow(self.OUTPUT_FILE_ROW)
			self.OUTPUT_FILE.flush()
			self.OUTPUT_FILE_ROW = []



