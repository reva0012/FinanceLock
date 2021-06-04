from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from View_Req_Inves import *
from View_Cust_Det import *
from tkinter import messagebox
import pyrebase

def home_pg_inves(Uid):

	firebase_config = {
		"apiKey" : "AIzaSyCvuNFssXW4k1cHifCRH_-KP6IPuxJHzqk",
	    "authDomain" : "financelock-c6ea8.firebaseapp.com",
	    "databaseURL" : "https://financelock-c6ea8-default-rtdb.firebaseio.com",
	    "projectId" : "financelock-c6ea8",
	    "storageBucket" : "financelock-c6ea8.appspot.com",
	    "messagingSenderId" : "523873568466",
	    "appId" : "1:523873568466:web:b4259e5cb0e1c85059cf0b",
	    "measurementId" : "Gender-R1R8CZD552"
	}

	firebase = pyrebase.initialize_app(firebase_config)

	db = firebase.database()

	def logout():
		person = db.child('People').child('Investor').child(Uid).get()
		name = person.val()['name']
		response = messagebox.askyesno("Are You Sure?", name + ", are you sure you want to logout? ")
		if response == 1:
			root2.destroy()

	def next_but():
		if i.get() == 1:
			view_req(Uid)
		else:
			view_cust_det(Uid)

	global bg_hpi

	root2 = Toplevel()
	root2.title("Home Page Investor")
	root2.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')

	bg_hpi = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(root2, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_hpi, anchor = "nw")
	my_canvas.create_text(635, 150, text = "Choose your Services", font = ("Helvetica", 25, "bold"), fill = "steel blue")
	my_canvas.create_rectangle(450, 275, 830, 400, outline = "black", fill = "white")

	i = IntVar()
	i.set("1")
	r1 = Radiobutton(root2, text = "View Loan Requests", value = 1, variable = i, background = 'white')
	r2 = Radiobutton(root2, text = "View Customer Details", value = 2, variable = i, background = 'white')
	r1_win = my_canvas.create_window(520, 310, window = r1)
	r2_win = my_canvas.create_window(526, 340, window = r2)

	next_button = Button (root2, text = "Next", command = next_but, background = "white", highlightbackground = "black", highlightthickness = 2)
	next_button_win = my_canvas.create_window(750, 380, window = next_button)

	goback_button = Button (root2, text = "Log Out", command = logout, background = "white", highlightbackground = "black", highlightthickness = 2)# command = back)
	goback_button_win = my_canvas.create_window(525, 380, window = goback_button)
	root2.grab_set()
	#my_canvas.create_line(0, 400, 1300, 400, fill = "steel blue")