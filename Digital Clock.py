from tkinter import *
import time
from time import strftime

root = Tk()
root.title("Clock")
root.geometry("500x100")
root.resizable(False, False)

def present_time():
	display_time = time.strftime("%I:%M:%S %p")
	digi_clock.config(text = display_time)
	digi_clock.after(200, present_time)

digi_clock = Label(root, font = ("Lucida Console", 50), fg = "black", bg = "gray")
digi_clock.pack()

present_time()
root.mainloop()
