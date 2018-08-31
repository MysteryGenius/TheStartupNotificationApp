
import re
from tkinter import *
from tkinter import ttk
import shutil
import os

 
def create_file(temp):

	filename = "TSNA.vbs"
	f = open(filename,"w+")
	f.write(temp)
	f.close()

class tempApp:
	def __init__(self, master):
		event_name = StringVar()
		subject_date = StringVar()


		title_name = ttk.Label(master, text="The Startup Notification App", font=("Garamond", 18, "bold"), foreground="#1D3557", padding="10")
		title_name.grid(row=0, column=0,columnspan=2)
		notebook = ttk.Notebook(master)
		notebook.grid(row=1, column=0, columnspan=2)

		frame1 = ttk.Frame(notebook, padding=(5, 5))
		frame2 = ttk.Frame(notebook, padding=(5, 5))
		frame3 = ttk.Frame(notebook, padding=(5, 5))
		# frame4 = ttk.Frame(notebook, padding=(5, 5))

		notebook.add(frame1, text="Date Countdown")
		notebook.add(frame2, text="Surprise")
		notebook.add(frame3, text="Daily")
		# notebook.add(frame4, text="Removal")


		style = ttk.Style()                     
		current_theme =style.theme_use()
		style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": {"padding": [10, 5]}}}) 

		# Options 1
		count_entry_prompt_1 = ttk.Label(frame1, text="Enter your special day :")
		count_entry_prompt_1.pack(fill=X,pady=10)
		count_date_entry = ttk.Entry(frame1)
		count_date_entry.pack(fill=X,pady=10)
		self.count_date_entry = count_date_entry
		count_entry_prompt_2 = ttk.Label(frame1, text="Name of your event :")
		count_entry_prompt_2.pack(fill=X,pady=10)
		count_event_entry = ttk.Entry(frame1)
		count_event_entry.pack(fill=X,pady=10)
		self.count_event_entry = count_event_entry
		count_button = ttk.Button(frame1, text="Convert", command=self.callback_countdown)
		count_button.pack(fill=X,pady=10)
		validation_label_1 = ttk.Label(frame1, text="")
		validation_label_1.pack(fill=X,pady=10)
		self.validation_label_1 = validation_label_1

		# Options 2
		surprise_entry_prompt_1 = ttk.Label(frame2, text="Enter your special day (dd/):")
		surprise_entry_prompt_1.pack(fill=X,pady=10)
		surprise_date_entry = ttk.Entry(frame2)
		surprise_date_entry.pack(fill=X,pady=10)
		self.surprise_date_entry = surprise_date_entry
		surprise_entry_prompt_2 = ttk.Label(frame2, text="Enter your message :")
		surprise_entry_prompt_2.pack(fill=X,pady=10)
		surprise_event_entry = ttk.Entry(frame2)
		surprise_event_entry.pack(fill=X,pady=10)
		self.surprise_event_entry = surprise_event_entry
		surprise_button = ttk.Button(frame2, text="Convert", command=self.callback_surprise)
		surprise_button.pack(fill=X,pady=10)
		validation_label_2 = ttk.Label(frame2, text="")
		validation_label_2.pack(fill=X,pady=10)
		self.validation_label_2 = validation_label_2

		# Options 3
		message_entry_prompt = ttk.Label(frame3, text="Enter your message")
		message_entry_prompt.pack(fill=X,pady=10)
		message_entry = ttk.Entry(frame3)
		message_entry.pack(fill=X,pady=10)
		self.message_entry = message_entry
		message_button = ttk.Button(frame3, text="Convert", command=self.callback_message)
		message_button.pack(fill=X,pady=10)
		validation_label_3 = ttk.Label(frame3, text="")
		validation_label_3.pack(fill=X,pady=10)
		self.validation_label_3 = validation_label_3

		# # Options 4 (Removal)
		# removal_prompt = ttk.Label(frame4, text="Enter your message")
		# removal_prompt.pack(fill=X,pady=10)
		# removal_button = ttk.Button(frame4, text="Convert", command=self.callback_message)
		# removal_button.pack(fill=X,pady=10)
		# validation_label_4 = ttk.Label(frame4, text="")
		# validation_label_4.pack(fill=X,pady=10)
		# self.validation_label_4 = validation_label_4

		self.p = re.compile('^((0|1|2)\d{1})/((0|1)\d{1})/')
	def callback_countdown(self):

		subject_date = self.count_date_entry.get()
		if self.p.match(subject_date)!=None:
			event_name = self.count_event_entry.get()
			create_file(self.backend_countdown(subject_date, event_name))

			self.validation_label_1.config(text="Done")
		else:
			self.validation_label_1.config(text="Format for the date is dd/mm/ ")


	def callback_surprise(self):
		subject_date = self.surprise_date_entry.get()
		if self.p.match(subject_date)!=None:
			event_name = self.surprise_event_entry.get()
			create_file(self.backend_surprise(subject_date, event_name))
			self.validation_label_1.config(text="Done")
		else:
			self.validation_label_1.config(text="Format for the date is dd/mm/ ")


	def callback_message(self):
		event_name = self.message_entry.get()
		create_file(self.backend_message(event_name))
		#shutil.copyfile('./TSNA.vbs', 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/')  
		self.validation_label_3.config(text="Done")

	# def removal_tool(self):
	# 	temp = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/TSNA.vbs"
	# 	if os.path.exists(temp):
 #  			os.remove(temp)
 #  			self.validation_label_1.config(text="Done")
	# 	else:
	# 		self.validation_label_1.config(text="Done")
			

	def backend_countdown(self, subject_date, event_name):
		return ("fromDate = Date\ntoDate = \"{}\" & Year(Date)\ntotalDate = DateDiff(\"d\",fromDate, toDate)\nevent_name = \"{}\"\nIf (totalDate > 1) Then\ntoPrint = event_name & \" is in \" & totalDate & \" days\"\nElseIf (totalDate = 1) Then\ntoPrint = event_name & \" is tomorrow!\"\nElseIf (totalDate = 0) Then\ntoPrint = event_name & \" is today!\"\nElse\ntotalDate = 365 + totalDate\ntoPrint = event_name  & \" is in \" & totalDate & \" days\"\nEnd If\nmessage=msgbox(toPrint, 1+64, \"A virus\")").format(subject_date,event_name)


	def backend_surprise(self, subject_date, event_name):
		return ("fromDate = Date\ntoDate = \"{}\" & Year(Date)\ntotalDate = DateDiff(\"d\",fromDate, toDate)\nevent_name = \"{}\"\nIf (totalDate = 0) Then\ntoPrint = event_name & \" is today!!\"\nmessage=msgbox(toPrint, 1+64, \"A virus\")").format(subject_date,event_name)

	def backend_message(self, event_name):
		return ("event_name = \"{}\"\nmessage=msgbox(event_name, 1+64, \"A virus\")").format(event_name)


root = Tk()
root.title("TSNA")

frame = ttk.Frame(root, height=450, width=250, relief=RIDGE, padding=(25, 25))
frame.pack()
app = tempApp(frame)
root.mainloop()

