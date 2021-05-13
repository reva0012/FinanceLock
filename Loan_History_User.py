from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

def view_det():
	global bg_vd

	top_vd = Toplevel()
	top_vd.title("View Loan History")
	top_vd.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	#top_ca.attributes('-topmost', 'true')

	bg_vd = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_vd, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_vd, anchor = "nw")
	my_canvas.create_text(635, 125, text = "View Loan History", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	#After installing backend
