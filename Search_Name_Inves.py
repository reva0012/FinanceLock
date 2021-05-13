from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

def search_name_inves():

	global bg_sni

	top_sni = Toplevel()
	top_sni.title("Search Customers by Name")
	top_sni.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	top_sni.grab_set()

	bg_sni = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_sni, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_sni, anchor = "nw")
	my_canvas.create_text(635, 125, text = "Search Customers by Name", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_rectangle(400, 250, 925, 600, outline = "black", fill = "white")

	my_canvas.create_text(470, 200, text = "Enter the name: ", font = ("Helvetica", 15), fill = "steel blue")
	sni_name = Entry(top_sni, width = 50, borderwidth = 1)
	sni_name_win = my_canvas.create_window(705, 200, window = sni_name)

	sub_but = Button (top_sni, text = "Submit", background = "white", highlightbackground = "black", highlightthickness = 2)
	sub_but_win = my_canvas.create_window(900, 200, window = sub_but)

	

