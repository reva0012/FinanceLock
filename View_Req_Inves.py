from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

def view_req():

	global bg_vd

	top_vd = Toplevel()
	top_vd.title("View Loan Requests")
	top_vd.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	#top_ca.attributes('-topmost', 'true')

	bg_vd = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_vd, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_vd, anchor = "nw")
	my_canvas.create_text(635, 125, text = "View Loan Requests", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_rectangle(430, 275, 830, 420, outline = "black", fill = "white")

	my_canvas.create_text(480, 300, text = "Loan ID: ", font = ("Helvetica", 14), fill = "steel blue")
	record = ["LN0001", "LN00002", "LN0004"]
	click_gen = StringVar()
	click_gen.set(record[0])
	e_gen = OptionMenu(top_vd, click_gen, *record)
	e_gen_win = my_canvas.create_window(600, 300, window = e_gen)

	accept_button = Button(top_vd, text = "Accept", background = "white", highlightbackground = "black", highlightthickness = 2)
	accept_button_win = my_canvas.create_window(750, 380, window = accept_button)

	reject_button = Button(top_vd, text = "Reject", background = "white", highlightbackground = "black", highlightthickness = 2)# command = back)
	reject_button_win = my_canvas.create_window(625, 380, window = reject_button)

	goback_button = Button(top_vd, text = "Go back", command = top_vd.destroy, background = "white", highlightbackground = "black", highlightthickness = 2)# command = back)
	goback_button_win = my_canvas.create_window(500, 380, window = goback_button)