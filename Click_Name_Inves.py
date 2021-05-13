from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

def click_name_inves():

	global bg_cni

	def clear():
		my_canvas.delete("myrect")
		my_canvas.create_rectangle(400, 250, 925, 600, outline = "black", fill = "white", tag = "myrect")
		#my_canvas.create_text(635, 350, text = "Search Customers List", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	top_cni = Toplevel()
	top_cni.title("Search Customers from List")
	top_cni.iconbitmap('C:/Users/sidsu/Desktop/V.I.T/Project/SWE/Project/BG/icon.ico')
	top_cni.grab_set()

	bg_cni = ImageTk.PhotoImage(Image.open("BG/bgmain2.jpeg"))
	my_canvas = Canvas(top_cni, width = 1300, height = 733)
	my_canvas.pack(fill = "both", expand = True)
	my_canvas.create_image(0, 0, image = bg_cni, anchor = "nw")
	my_canvas.create_text(635, 125, text = "Search Customers from List", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_rectangle(400, 250, 925, 600, outline = "black", fill = "white", tag = "myrect")
	my_canvas.create_text(635, 350, text = "Search Customers from List", font = ("Helvetica", 25, "bold"), fill = "steel blue")

	my_canvas.create_text(510, 200, text = "Name: ", font = ("Helvetica", 14), fill = "steel blue")
	record = ["Raman Subramanian", "Siddharth Suresh Nair", "LN0004"]
	click_gen = StringVar()
	click_gen.set(record[0])
	e_gen = OptionMenu(top_cni, click_gen, *record)
	e_gen_win = my_canvas.create_window(650, 200, window = e_gen)

	sub_but = Button (top_cni, text = "Submit", background = "white", highlightbackground = "black", highlightthickness = 2)
	sub_but_win = my_canvas.create_window(800, 200, window = sub_but)

	clr_but = Button (top_cni, text = "Clear", command = clear, background = "white", highlightbackground = "black", highlightthickness = 2)
	clr_but_win = my_canvas.create_window(500, 650, window = clr_but)