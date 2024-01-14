from tkinter import *
from time import strftime
import keyboard

# Create a Tkinter window
root = Tk()
root.title('Clock - Python Widget')

# Get screen height and width
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# Set the size and position of the window
root.geometry("120x75+{}+{}".format(screen_width - 120, screen_height - 115))

# Configure window attributes for appearance and visibility
root.overrideredirect(True)
root.configure(background="black")
root.resizable(0, 0)
root.wm_attributes('-topmost', True)
root.grab_set()
root.lift()
root.attributes("-toolwindow", 1)
root.attributes("-alpha", 0.50)

# Default font for the clock label
default_font = ("Montserrat", 23, "bold")

# Font to be used when creating clock labels
current_font = default_font

# Create clock label
clock_label = Label(root, font=current_font, background="black", foreground="white", anchor="n")
clock_label.pack(anchor="nw", padx=10, pady=0)

# Date label
date_label = Label(root, font=("montserrat", 13,),  background="black", foreground="white")
date_label.pack(anchor="nw", padx=7, pady=3)

# Initially, show clock mode is active
is_clock_mode = True
is_running = False
stopwatch_seconds = 0
is_blinking = False
is_stopwatch_mode = False

# Function to update time
def update_time():
    global stopwatch_seconds, is_blinking, is_stopwatch_mode
    if is_clock_mode:
        # Update clock and date information
        time_str = strftime("%H:%M")
        date_str = strftime("%d/%m/%Y")
        clock_label.config(text=time_str)
        date_label.config(text=date_str)
    else:
        if is_running:
            # If in stopwatch mode, update the time
            stopwatch_seconds += 1
            clock_label.config(text=format_seconds(stopwatch_seconds))
        else:
            # If in stopwatch mode, control blinking
            if stopwatch_seconds == 0:
                clock_label.config(text="00:00" if is_blinking else "")
                is_blinking = not is_blinking
            else:
                if stopwatch_seconds % 2 == 0:
                    clock_label.config(text=format_seconds(stopwatch_seconds))
                else:
                    clock_label.config(text="00:00")
    # Update every second
    root.after(1000, update_time)

# Function to format seconds (minute:second)
def format_seconds(seconds):
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes:02d}:{seconds:02d}"

# Function to toggle between clock and stopwatch modes
def toggle_mode():
    global is_clock_mode, stopwatch_seconds, is_blinking, is_stopwatch_mode, current_font
    is_clock_mode = not is_clock_mode
    stopwatch_seconds = 0 if is_clock_mode else 0
    is_blinking = False
    if is_clock_mode:
        # If switching to clock mode, use the default font
        current_font = default_font
        clock_label.config(font=current_font)
    else:
        # If switching to stopwatch mode, use DS-Digital font and start the stopwatch
        current_font = ("DS-Digital", 29, "bold")
        clock_label.config(font=current_font)
        start_stopwatch()
        is_stopwatch_mode = True

# Function to start the stopwatch
def start_stopwatch():
    global is_running, stopwatch_seconds
    if not is_running:
        is_running = True
        stopwatch_seconds = 0  # Reset the stopwatch
        is_blinking = True  # Start blinking
        is_stopwatch_mode = True  # Activate stopwatch mode

# Function to stop the stopwatch
def stop_stopwatch():
    global is_running
    is_running = False

# Function to reset the stopwatch and start blinking
def reset_and_blink():
    global stopwatch_seconds, is_blinking, is_running
    stopwatch_seconds = 0
    is_blinking = True
    is_running = False

# Function to toggle window visibility
def toggle_window_visibility():
    if root.state() == "withdrawn":  # If the window is hidden
        root.deiconify()  # Show the window
    else:
        root.withdraw()  # Hide the window

# Add keyboard shortcuts
keyboard.add_hotkey('alt+m', toggle_mode)
keyboard.add_hotkey('alt+0', reset_and_blink)
keyboard.add_hotkey('alt+1', start_stopwatch)
keyboard.add_hotkey('win+h', toggle_window_visibility)

# Call the function to update the time
update_time()

# Run the Tkinter window
root.mainloop()
