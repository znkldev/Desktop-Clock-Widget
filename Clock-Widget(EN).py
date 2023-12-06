from tkinter import *
from time import strftime

import win32gui
import win32con

root = Tk() # Creating a Tkinter window
root.title('Clock - Widget Python') # Setting tkinter window title (only applicable in Windows window management)
screen_height = root.winfo_screenheight() # Get screen height
screen_width = root.winfo_screenwidth() # Set window width and height, place it at the bottom left corner
root.geometry("110x75+{}+{}".format(screen_width - 110, screen_height - 115)) 
root.overrideredirect(True) # Removing window frame
root.configure(background="black") # Setting background color
root.resizable(0, 0) # Making the window size fixed
root.wm_attributes('-topmost', True) # Setting the window to always stay on top
root.grab_set() # Redirecting keyboard and mouse inputs to this window
root.lift() # Setting the window to stay in front of other windows
root.attributes("-toolwindow", 1) # Removing window title and frame
root.attributes("-alpha", 0.50) # Setting window transparency

hwnd = win32gui.GetForegroundWindow() # Get the current active window
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TRANSPARENT) # Set window transparency

def clock():
    text = strftime("%H:%M")
    date_text = strftime("%d/%m/%Y")  # Set the date format (day/month/year)
    time_label.config(text=text)
    date_label.config(text=date_text)
    time_label.after(1000, clock)

# Function to close the window
def close_window():
    root.destroy()

# To close after 10 seconds
# root.after(10000, close_window)

time_label = Label(root, font=("Montserrat", 23, "bold"), background="black", foreground="white", anchor="n")
time_label.pack(anchor="nw", padx=10, pady=0)

date_label = Label(root, font=("Montserrat", 12,),  background="black", foreground="white")
date_label.pack(anchor="nw", padx=7, pady=3)

clock()

root.mainloop()
