from tkinter import *
from time import strftime
import win32gui
import win32con
import keyboard

# Creating a Tkinter window
root = Tk()
root.title('Clock - Widget Python')  # Setting the title of the tkinter window

# Getting screen height and width, setting window size, positioning it at the bottom left corner
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
root.geometry("110x75+{}+{}".format(screen_width - 110, screen_height - 115))

# Removing window frame and making the window transparent
root.overrideredirect(True)
root.configure(background="black")  # Setting the background color
root.resizable(0, 0)  # Making the window size fixed
root.wm_attributes('-topmost', True)  # Setting the window to always stay on top
root.grab_set()  # Redirecting keyboard and mouse inputs to this window
root.lift()  # Setting the window to stay in front of other windows
root.attributes("-toolwindow", 1)  # Removing window title and frame
root.attributes("-alpha", 0.50)  # Setting window transparency

# Making the window transparent and click-through using Win32 API
hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TRANSPARENT)

def clock():
    text = strftime("%H:%M")
    date_text = strftime("%d/%m/%Y")  # Setting the date format (day/month/year)
    time_label.config(text=text)
    date_label.config(text=date_text)
    time_label.after(1000, clock)

def toggle_window_visibility():
    if root.state() == "withdrawn":  # If the window is hidden
        root.deiconify()  # Show the window
    else:
        root.withdraw()  # Hide the window

# Listen for Win+H key combination to show/hide the window
keyboard.add_hotkey('win+h', toggle_window_visibility)

time_label = Label(root, font=("Montserrat", 23, "bold"), background="black", foreground="white", anchor="n")
time_label.pack(anchor="nw", padx=10, pady=0)

date_label = Label(root, font=("Montserrat", 12,),  background="black", foreground="white")
date_label.pack(anchor="nw", padx=7, pady=3)

clock()

root.mainloop()
