import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from time import strftime
from threading import Thread
import csv
from simplea import *

OUTPUT_LOG_DISPLAY = False

def check_error_input_provided():
	if globals()['USER_EMAIL_ENTRY_TEXT'].get() == '':
		messagebox.showerror("Error", 
							 "No email provided")
		return True
	
	if globals()['USER_PASSWORD_ENTRY_TEXT'].get() == '':
	   messagebox.showerror("Error", 
							 "No password provided")
	   return True

	if globals()['EMAIL_SMTP_ENTRY_TEXT'].get() == '':
		messagebox.showerror("Error", 
							 "No SMTP server provided")
		return True

	if globals()['CSV_FILENAME_SELECTED'].get() == 'No file selected' or globals()['CSV_FILENAME_SELECTED'].get() == '':
		messagebox.showerror("Error", 
							 "No CSV file with employee details selected")
		return True

	if globals()['EMAIL_SUBJECT_ENTRY_TEXT'].get() == '':
		messagebox.showerror("Error", 
							 "No email subject provided")
		return True

	if globals()['EMAIL_FILENAME_SELECTED'].get() == 'No file selected' or globals()['EMAIL_FILENAME_SELECTED'].get() == '':
		messagebox.showerror("Error", 
							 "No file with email content selected")
		return True

	if globals()['ATTACHMENT_PATH_SELECTED'].get() == 'No location selected' or globals()['ATTACHMENT_PATH_SELECTED'].get() == '':
		messagebox.showerror("Error", 
							 "No attachment directory selected")
		return True

	if globals()['LOG_OUTPUT_FILE_SELECTED'].get() == 'No location selected' or globals()['LOG_OUTPUT_FILE_SELECTED'].get() == '':
		messagebox.showerror("Error", 
							 "No output log filename selected")
		return True

	COLUMNS_PROVIDED = ''
	try:
		FILE_DETAILS = open(globals()['CSV_FILENAME_SELECTED'].get(), 'r')
		CSV_DETAILS = csv.reader(FILE_DETAILS)

		for row in CSV_DETAILS:
			COLUMNS_PROVIDED = len(row)
			break

		FILE_DETAILS.close()

	except:
		messagebox.showerror("Error", "Invalid CSV file: " + globals()['CSV_FILENAME_SELECTED'].get())
		return True

	if int(globals()['FILE_ATTACHMENTS_ENTRY_TEXT'].get()) < 0 or int(globals()['FILE_ATTACHMENTS_ENTRY_TEXT'].get()) >= COLUMNS_PROVIDED:
		messagebox.showerror("Error", "Invalid column number provided for file attachments")
		return True

	if int(globals()['EMAIL_ID_COLUMN_ENTRY_TEXT'].get()) < 0 or int(globals()['EMAIL_ID_COLUMN_ENTRY_TEXT'].get()) >= COLUMNS_PROVIDED:
		messagebox.showerror("Error", "Invalid column number provided for email addresses")
		return True

	for i in globals()['SUBSTITUTION_IN_COLUMN']:
		try:
			if int(i[1].get()) < 0 or int(i[1].get()) >= COLUMNS_PROVIDED:
				messagebox.showerror("Error", "Invalid column number " + i[1].get() + " provided in substitution: " + i[0].get())
				return True
		except:
			messagebox.showerror("Error", "Invalid column number " + i[1].get() + " provided in substitution: " + i[0].get())
			return True

	return False

def mailfromfileprovided():

	if check_error_input_provided():
		return

	disable_select()

	if not OUTPUT_LOG_DISPLAY:
		OUTPUT_LOG_LIST_FRAME = tk.Frame(globals()['root'], 
										 name = 'outputloglistframe')
		OUTPUT_LOG_LIST_FRAME.pack()
		OUTPUT_LOG_LIST = tk.Listbox(OUTPUT_LOG_LIST_FRAME, name = 'list', width = 95)
		OUTPUT_LOG_LIST.pack(fill = tk.BOTH, side=tk.LEFT)
		OUTPUT_LOG_SCROLL = tk.Scrollbar(OUTPUT_LOG_LIST_FRAME, orient = tk.VERTICAL, command=OUTPUT_LOG_LIST.yview)
		OUTPUT_LOG_SCROLL.pack(side = tk.LEFT, fill = tk.Y)
		OUTPUT_LOG_LIST.config(yscrollcommand=OUTPUT_LOG_SCROLL.set)

		globals()['OUTPUT_LOG_DISPLAY'] = True 
		
	Thread(target = csvmail, args = (globals()['USER_EMAIL_ENTRY_TEXT'].get(),
									 globals()['USER_PASSWORD_ENTRY_TEXT'].get(),
									 globals()['EMAIL_SMTP_ENTRY_TEXT'].get(), 
									 globals()['CSV_FILENAME_SELECTED'].get(), 
									 globals()['EMAIL_SUBJECT_ENTRY_TEXT'].get(), 
									 globals()['EMAIL_FILENAME_SELECTED'].get(), 
									 int(globals()['EMAIL_ID_COLUMN_ENTRY_TEXT'].get()),
									 globals()['ATTACHMENT_PATH_SELECTED'].get(), 
									 int(globals()['FILE_ATTACHMENTS_ENTRY_TEXT'].get()),
									 globals()['SUBSTITUTION_IN_COLUMN'],
									 globals()['LOG_OUTPUT_FILE_SELECTED'].get())).start()

def get_substitution_input():
	SUBSTITUTION_BUTTON_FRAME = tk.Frame(globals()['SUBSTITUTIONS_FRAME'], height = 4, 
						  width = 5, 
						  bd = 1, 
						  padx=4, 
						  pady=4)

	SUBSTITUTION_LABEL = tk.Label(SUBSTITUTION_BUTTON_FRAME, 
						  text='Substitute: ')

	SUBSTITUTION_LABEL.pack(side=tk.LEFT)

	SUBSTITUTION_ENTRY_TEXT = tk.StringVar()

	SUBSTITUTION_ENTRY = tk.Entry(SUBSTITUTION_BUTTON_FRAME, textvariable=SUBSTITUTION_ENTRY_TEXT, width=10)

	SUBSTITUTION_ENTRY.pack(side=tk.LEFT)


	CSV_COLUMN_LABEL = tk.Label(SUBSTITUTION_BUTTON_FRAME, 
								text='with text from column: ')

	CSV_COLUMN_LABEL.pack(side=tk.LEFT)

	
	CSV_COLUMN_ENTRY_TEXT = tk.StringVar()

	CSV_COLUMN_ENTRY = tk.Entry(SUBSTITUTION_BUTTON_FRAME, textvariable=CSV_COLUMN_ENTRY_TEXT, width=4)

	CSV_COLUMN_ENTRY.pack(side=tk.LEFT)

	globals()['SUBSTITUTION_IN_COLUMN'].append((SUBSTITUTION_ENTRY_TEXT, CSV_COLUMN_ENTRY_TEXT))

	SUBSTITUTION_BUTTON_FRAME.pack(fill=tk.BOTH)
	
def email_file_select(some_filename_provided):
	globals()['EMAIL_FILENAME_SELECTED'].set(some_filename_provided)

def csv_file_select(some_filename_provided):
	globals()['CSV_FILENAME_SELECTED'].set(some_filename_provided)

def select_filename(some_callback_provided, filetypes_provided):
	some_callback_provided(filedialog.askopenfilename(initialdir = "/",
													  title = "Select file",
													  filetypes = filetypes_provided))



#########################################################################################
####################################USER EMAIL###########################################
USER_EMAIL_FRAME = tk.Frame(height = 4, 
							width = 5, 
							bd = 1, 
							padx=4, 
							pady=4)

USER_EMAIL_LABEL = tk.Label(USER_EMAIL_FRAME, 
						  text='Email: ')

USER_EMAIL_ENTRY_TEXT = tk.StringVar()

USER_EMAIL_ENTRY = tk.Entry(USER_EMAIL_FRAME, textvariable=USER_EMAIL_ENTRY_TEXT, width=25)

USER_EMAIL_FRAME.pack(fill=tk.BOTH)

USER_EMAIL_LABEL.pack(side=tk.LEFT)

USER_EMAIL_ENTRY.pack(side=tk.LEFT)

#########################################################################################
####################################USER PASSSWORD#######################################

USER_PASSWORD_FRAME = tk.Frame(height = 4, 
							width = 5, 
							bd = 1, 
							padx=4, 
							pady=4)

USER_PASSWORD_LABEL = tk.Label(USER_PASSWORD_FRAME, 
						  text='Password: ')

USER_PASSWORD_ENTRY_TEXT = tk.StringVar()

USER_PASSWORD_ENTRY_TEXT.set('')

USER_PASSWORD_ENTRY = tk.Entry(USER_PASSWORD_FRAME, 
							   textvariable=USER_PASSWORD_ENTRY_TEXT, 
							   show='*', 
							   width=25)

USER_PASSWORD_FRAME.pack(fill=tk.BOTH)

USER_PASSWORD_LABEL.pack(side= tk.LEFT)

USER_PASSWORD_ENTRY.pack(side=tk.LEFT)

#########################################################################################
########################################EMAIL SMTP#######################################

EMAIL_SMTP_FRAME = tk.Frame(height = 4, 
							width = 5, 
							bd = 1, 
							padx=4, 
							pady=4)

EMAIL_SMTP_LABEL = tk.Label(EMAIL_SMTP_FRAME, 
						  text='SMTP server: ')

EMAIL_SMTP_ENTRY_TEXT = tk.StringVar()

EMAIL_SMTP_ENTRY_TEXT.set('mail.ults.in:25')

EMAIL_SMTP_ENTRY = tk.Entry(EMAIL_SMTP_FRAME, 
							textvariable=EMAIL_SMTP_ENTRY_TEXT, 
							width=25)

EMAIL_SMTP_FRAME.pack(fill=tk.BOTH)

EMAIL_SMTP_LABEL.pack(side= tk.LEFT)

EMAIL_SMTP_ENTRY.pack(side=tk.LEFT)

#########################################################################################
##########################################CSV FILE#######################################

CSV_FILE_FRAME = tk.Frame(globals()['root'],
						  height = 4, 
						  width = 5, 
						  name='csvfileselectframe',
						  bd = 1, 
						  padx=4, 
						  pady=4)

CSV_FILE_LABEL = tk.Label(CSV_FILE_FRAME, 
						  text='Select the CSV file containing employee data: ')

CSV_FILE_SELECTOR = tk.Button(CSV_FILE_FRAME, 
							  name='csvfileselect',
							  text='Select File', 
							  command= lambda: select_filename(csv_file_select, 
															   (("CSV files","*.csv"),
																("all files","*.*"))))

CSV_FILENAME_SELECTED = tk.StringVar()
CSV_FILENAME_SELECTED.set('No file selected')
CSV_FILENAME_LABEL = tk.Label(CSV_FILE_FRAME, 
							  textvariable=CSV_FILENAME_SELECTED)

CSV_FILE_FRAME.pack(fill=tk.BOTH)
CSV_FILE_LABEL.pack(side = tk.LEFT)
CSV_FILE_SELECTOR.pack(side = tk.LEFT)
CSV_FILENAME_LABEL.pack(side= tk.LEFT)

#########################################################################################
######################################HORIZONTAL PADDING#################################

HORIZONTAL_PADDING_FRAME = tk.Frame(height = 3, 
						  width = 5, 
						  bd = 1, 
						  padx= 4, 
						  pady= 4)

HORIZONTAL_PADDING_FRAME.pack()

#########################################################################################
####################################EMAIL SUBJECT#######################################

EMAIL_SUBJECT_FRAME = tk.Frame(height = 4, 
							width = 5, 
							bd = 1, 
							padx=4, 
							pady=4)

EMAIL_SUBJECT_LABEL = tk.Label(EMAIL_SUBJECT_FRAME, 
						  text='Email subject: ')

EMAIL_SUBJECT_ENTRY_TEXT = tk.StringVar()

EMAIL_SUBJECT_ENTRY_TEXT.set('This is something in text')

EMAIL_SUBJECT_ENTRY = tk.Entry(EMAIL_SUBJECT_FRAME, 
							   textvariable=EMAIL_SUBJECT_ENTRY_TEXT, 
							   width=25)

EMAIL_SUBJECT_FRAME.pack(fill=tk.BOTH)

EMAIL_SUBJECT_LABEL.pack(side= tk.LEFT)

EMAIL_SUBJECT_ENTRY.pack(side=tk.LEFT)

#########################################################################################
########################################EMAIL CONTENT FILE###############################

EMAIL_FILE_FRAME = tk.Frame(globals()['root'],
							height = 4, 
							width = 5, 
							name = 'emaildataframe',
							bd = 1, 
							padx=4, 
							pady=4)

EMAIL_FILE_LABEL = tk.Label(EMAIL_FILE_FRAME, 
						  text='Select the file containing the email content: ', 
						  anchor=tk.W, 
						  justify=tk.LEFT)

EMAIL_FILE_SELECTOR = tk.Button(EMAIL_FILE_FRAME, 
								name = 'emaildatafileselect',
								text='Select File', 
								command= lambda: select_filename(email_file_select, 
															   (("HTML files","*.html"),
																("RTF files","*.rtf"),
																("all files","*.*"))), 
								anchor=tk.W, 
								justify=tk.LEFT)

EMAIL_FILENAME_SELECTED = tk.StringVar()
EMAIL_FILENAME_SELECTED.set('No file selected')
EMAIL_FILENAME_LABEL = tk.Label(EMAIL_FILE_FRAME, 
								textvariable=EMAIL_FILENAME_SELECTED)

EMAIL_FILE_FRAME.pack(fill= tk.BOTH)
EMAIL_FILE_LABEL.pack(side = tk.LEFT)
EMAIL_FILE_SELECTOR.pack(side = tk.LEFT)
EMAIL_FILENAME_LABEL.pack(side= tk.LEFT)

#########################################################################################
########################################EMAIL ID COLUMN##################################

EMAIL_ID_COLUMN_FRAME = tk.Frame(height = 4, 
							width = 5, 
							bd = 1, 
							padx=4, 
							pady=4)

EMAIL_ID_COLUMN_LABEL = tk.Label(EMAIL_ID_COLUMN_FRAME, 
						  text='Email addresses in column: ', 
						  anchor=tk.W, 
						  justify=tk.LEFT)

EMAIL_ID_COLUMN_ENTRY_TEXT = tk.StringVar()

EMAIL_ID_COLUMN_ENTRY_TEXT.set('0')

EMAIL_ID_COLUMN_ENTRY = tk.Entry(EMAIL_ID_COLUMN_FRAME, 
								  textvariable=EMAIL_ID_COLUMN_ENTRY_TEXT, 
								  width=4)

EMAIL_ID_COLUMN_FRAME.pack(fill=tk.BOTH)
EMAIL_ID_COLUMN_LABEL.pack(side=tk.LEFT)
EMAIL_ID_COLUMN_ENTRY.pack(side=tk.LEFT)

#########################################################################################
########################################ATTACHMENT PATH##################################

ATTACHMENT_PATH_FRAME = tk.Frame(globals()['root'],
								 height = 4, 
								 width = 5, 
								 name = 'attachmentfilenameframe',
								 bd = 1, 
								 padx=4, 
								 pady=4)

ATTACHMENT_PATH_LABEL = tk.Label(ATTACHMENT_PATH_FRAME, 
								 text='Select the directory with attachments: ', 
								 anchor=tk.W, 
								 justify=tk.LEFT)

ATTACHMENT_PATH_SELECTED = tk.StringVar()
ATTACHMENT_PATH_SELECTED.set('No location selected')

ATTACHMENT_PATH_FILE_SELECTOR = tk.Button(ATTACHMENT_PATH_FRAME, 
										  name = 'attachmentfilenameselect',
										  text='Select Directory', 
										  command= lambda: ATTACHMENT_PATH_SELECTED.set(filedialog.askdirectory()), 
										  anchor=tk.W, 
										  justify=tk.LEFT)


ATTACHMENT_PATH_SELECTED_LABEL = tk.Label(ATTACHMENT_PATH_FRAME, 
										  textvariable=ATTACHMENT_PATH_SELECTED)

ATTACHMENT_PATH_FRAME.pack(fill= tk.BOTH)
ATTACHMENT_PATH_LABEL.pack(side = tk.LEFT)
ATTACHMENT_PATH_FILE_SELECTOR.pack(side = tk.LEFT)
ATTACHMENT_PATH_SELECTED_LABEL.pack(side= tk.LEFT)

#########################################################################################
########################################ATTACHMENT FILENAME COLUMN#######################

FILE_ATTACHMENTS_FRAME = tk.Frame(height = 4, 
							width = 5, 
							bd = 1, 
							padx=4, 
							pady=4)

FILE_ATTACHMENTS_LABEL = tk.Label(FILE_ATTACHMENTS_FRAME, 
						  text='Attachment filepaths in column: ', 
						  anchor=tk.W, 
						  justify=tk.LEFT)

FILE_ATTACHMENTS_ENTRY_TEXT = tk.StringVar()

FILE_ATTACHMENTS_ENTRY_TEXT.set('2')

FILE_ATTACHMENTS_ENTRY = tk.Entry(FILE_ATTACHMENTS_FRAME, 
								  textvariable=FILE_ATTACHMENTS_ENTRY_TEXT, 
								  width=4)

FILE_ATTACHMENTS_FRAME.pack(fill=tk.BOTH)
FILE_ATTACHMENTS_LABEL.pack(side=tk.LEFT)
FILE_ATTACHMENTS_ENTRY.pack(side=tk.LEFT)

#########################################################################################
#######################################SUBSTITUTIONS LABEL###############################

OPTIONS_FRAME = tk.Frame(globals()['root'],
						 height = 4, 
							width = 5, 
							name = 'substitutionsframe',
							bd = 1, 
							padx=4, 
							pady=4)

OPTIONS_LABEL = tk.Label(OPTIONS_FRAME, 
						  text='Substitutions', 
						  anchor=tk.W, 
						  justify=tk.LEFT)

OPTIONS_FRAME.pack(fill=tk.BOTH)
OPTIONS_LABEL.pack(side=tk.LEFT)

#########################################################################################
##################################SUBSTITUTION TEXT AND COLUMN###########################

SUBSTITUTION_IN_COLUMN = []

SUBSTITUTIONS_ADD = tk.Button(OPTIONS_FRAME, 
							  text='Add substitution',  
							  name = 'substitutions',
							  anchor=tk.W,
							  command= lambda: get_substitution_input(),
							  justify=tk.LEFT)

SUBSTITUTIONS_ADD.pack(side=tk.LEFT)

SUBSTITUTIONS_FRAME = tk.Frame(height = 4, 
							width = 5, 
							bd = 1, 
							padx=4, 
							pady=4)


SUBSTITUTIONS_FRAME.pack(fill=tk.BOTH)

#########################################################################################
#########################################LOG OUTPUT FILE#################################

LOG_OUTPUT_FILE_FRAME = tk.Frame(globals()['root'],
								 height = 4, 
								 width = 5, 
								 name = 'outputlogframe',
								 bd = 1, 
								 padx=4, 
								 pady=4)

LOG_OUTPUT_LABEL = tk.Label(LOG_OUTPUT_FILE_FRAME, 
						  text='Output log CSV saved in: ', 
						  anchor=tk.W, 
						  justify=tk.LEFT)

LOG_OUTPUT_FILE_SELECTED = tk.StringVar()
LOG_OUTPUT_FILE_SELECTED.set('No location selected')

LOG_OUTPUT_FILE_SELECTOR = tk.Button(LOG_OUTPUT_FILE_FRAME, 
							  name = 'outputlogfilenameselect',
							  text='Select Location', 
							  command= lambda: LOG_OUTPUT_FILE_SELECTED.set(
											   filedialog.asksaveasfilename(
											   filetypes=(("CSV files","*.csv"),
														  ("all files","*.*")))), 
							  anchor=tk.W, 
							  justify=tk.LEFT)


LOG_OUTPUT_FILE_LABEL = tk.Label(LOG_OUTPUT_FILE_FRAME, 
									textvariable=LOG_OUTPUT_FILE_SELECTED)

LOG_OUTPUT_FILE_FRAME.pack(fill= tk.BOTH)
LOG_OUTPUT_LABEL.pack(side = tk.LEFT)
LOG_OUTPUT_FILE_SELECTOR.pack(side = tk.LEFT)
LOG_OUTPUT_FILE_LABEL.pack(side= tk.LEFT)

#########################################################################################
########################################SEND EMAIL#######################################

EMAIL_SENDER_FRAME = tk.Frame(globals()['root'],
							  height = 4, 
							  width = 5,
							  name = 'emailsend',
							  bd = 1, 
							  padx=4,
							  pady=4)

EMAIL_SENDER = tk.Button(EMAIL_SENDER_FRAME, 
							  text='Send to all recipients',  
							  name = 'email',
							  command= mailfromfileprovided,
							  justify=tk.CENTER)

EMAIL_SENDER_FRAME.pack(fill=tk.BOTH)
EMAIL_SENDER.pack(side=tk.BOTTOM)

#########################################################################################
#########################################################################################

globals()['root'].mainloop()