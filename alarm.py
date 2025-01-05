
#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound
import threading

# Object
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x250")

# Color themes
light_mode = {
    "bg": "lightblue",
    "fg": "black",
    "entry_bg": "white",
    "button_bg": "blue",
    "button_fg": "white",
    "title_bg": "white",
}
dark_mode = {
    "bg": "#2e2e2e",
    "fg": "white",
    "entry_bg": "#444444",
    "button_bg": "#555555",
    "button_fg": "white",
    "title_bg": "#444444",
}
current_mode = light_mode

def apply_theme(theme):
    """Apply the selected theme to all widgets."""
    clock.configure(bg=theme["bg"])
    current_time_label.configure(bg=theme["bg"], fg=theme["fg"])
    title_label.configure(bg=theme["bg"], fg=theme["fg"])
    instruction_label.configure(bg=theme["bg"], fg="red")
    for widget in time_frame.winfo_children():
        widget.configure(bg=theme["bg"], fg=theme["fg"])
    hour_label.configure(bg=theme["title_bg"], fg=theme["fg"])
    minute_label.configure(bg=theme["title_bg"], fg=theme["fg"])
    second_label.configure(bg=theme["title_bg"], fg=theme["fg"])

    hour_entry.configure(bg=theme["entry_bg"], fg=theme["fg"])
    minute_entry.configure(bg=theme["entry_bg"], fg=theme["fg"])
    second_entry.configure(bg=theme["entry_bg"], fg=theme["fg"])
    
    status_label.configure(bg=theme["bg"], fg=theme["fg"])
    toggle_button.configure(bg=theme["button_bg"], fg=theme["button_fg"], activebackground=theme["button_bg"])
    toggle_button.config(text="Light Mode" if theme == dark_mode else "Dark Mode")

def toggle_mode():
    """Toggle between light and dark modes."""
    global current_mode
    current_mode = dark_mode if current_mode == light_mode else light_mode
    apply_theme(current_mode)



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break


def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    if validate_input(alarm_time):
        threading.Thread(target=alarm, args=(alarm_time,)).start()
        status_label.config(text=f"Alarm set for {alarm_time}", fg="green")
    else:
        status_label.config(text="Invalid time format. Try again!", fg="red")


def validate_input(time_str):
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
        return True
    except ValueError:
        return False


def update_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_time_label.config(text=f"Current Time: {current_time}")
    clock.after(1000, update_current_time)


# Labels
title_label = Label(clock, text="Alarm Clock", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

current_time_label = Label(clock, text="", font=("Helvetica", 12))
current_time_label.pack()
update_current_time()

instruction_label = Label(clock, text="Enter Time in 24-hour Format", font=("Arial", 10))
instruction_label.pack(pady=5)

time_frame = Frame(clock)
time_frame.pack(pady=5)

hour_label = Label(time_frame, text="Hour", width=5)
hour_label.grid(row=0, column=0, padx=5)

minute_label = Label(time_frame, text="Minute", width=5)
minute_label.grid(row=0, column=1, padx=5)

second_label = Label(time_frame, text="Second", width=5)
second_label.grid(row=0, column=2, padx=5)


hour = StringVar()
minute = StringVar()
second = StringVar()

hour_entry = Entry(time_frame, textvariable=hour, width=5)
hour_entry.grid(row=1, column=0, padx=5)

minute_entry = Entry(time_frame, textvariable=minute, width=5)
minute_entry.grid(row=1, column=1, padx=5)

second_entry = Entry(time_frame, textvariable=second, width=5)
second_entry.grid(row=1, column=2, padx=5)

# Button
Button(clock, text="Set Alarm", command=set_alarm, fg="black", bg="white", width=10).pack(pady=10)

# Toggle Mode Button
toggle_button = Button(clock, text="Toggle Dark Mode", command=toggle_mode)
toggle_button.pack(pady=10)

# Status Label
status_label = Label(clock, text="", font=("Arial", 10))
status_label.pack()

# Apply the initial theme
apply_theme(current_mode)

clock.mainloop()