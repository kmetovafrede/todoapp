# Simple todo-app where you can add task, remove task, input information and add end date

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk 

# adding a task 
def add_task():

    line_frame = ttk.Frame(root, style="Custom.TFrame")
    line_frame.pack(fill=tk.X, padx=5, pady=5)

    unchecked_image = Image.open("img/unchecked.png")
    checked_image = Image.open("img/checked.png")
    unchecked_image = unchecked_image.resize((15, 15))
    checked_image = checked_image.resize((15, 15))

    unchecked_icon = ImageTk.PhotoImage(unchecked_image)
    checked_icon = ImageTk.PhotoImage(checked_image)

    checkbox_state = tk.BooleanVar()
    checkbox_state.set(False)  

    def toggle_checkbox():
        if checkbox_state.get():
            checkbox.config(image=unchecked_icon)
            checkbox_state.set(False)
        else:
            checkbox.config(image=checked_icon)
            checkbox_state.set(True)

    checkbox_style = ttk.Style()
    checkbox_style.configure("Custom.TButton", padding=(3, 2, 0, 0), width=1.5)  

    checkbox = ttk.Button(line_frame, style="Custom.TButton", command=toggle_checkbox, image=unchecked_icon, compound=tk.LEFT)
    checkbox.pack(side=tk.LEFT, padx=(30, 5))

    entry = ttk.Entry(line_frame, style="Custom.TEntry")
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    date_entry = DateEntry(line_frame, width=10, background="#9279BA", foreground='white', borderwidth=2, date_pattern="dd.mm.yyyy")
    date_entry.pack(side=tk.LEFT, padx=(5, 10)) 

    remove_button = ttk.Button(line_frame, text="Remove", image=remove_icon, command=lambda frame=line_frame: remove_task(frame))
    remove_button.pack(side=tk.RIGHT, padx=(5, 30)) 

# removing a task
def remove_task(frame):
    frame.destroy() 

# root settings
root = tk.Tk()
root.title("To-do list")
root.geometry("450x500")
root.configure(background="#D1C1F2")

# styles 
style = ttk.Style()
style.configure("Custom.TFrame", background="#D1C1F2")
style.configure("Custom.TCheckbutton", background="#D1C1F2")
style.configure("Custom.TEntry", background="#B9D1C1F2A5E2")
style.configure("Custom.TLabel", background="#D1C1F2")

# top frame style
top_frame = ttk.Frame(root, style="Custom.TFrame")
top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# label style
tasks_img = Image.open("img/tasks.png")
tasks_img = tasks_img.resize((30, 30))
tasks_icon = ImageTk.PhotoImage(tasks_img)
label = ttk.Label(top_frame, text="Tasks", font=("Helvetica", 30, "bold"), style="Custom.TLabel", foreground="#745E96", image=tasks_icon, compound=tk.LEFT)
label.pack(side=tk.TOP, pady=25)

# button style
button = ttk.Button(top_frame, text="+", command=add_task)
button.pack(side=tk.TOP)

# trash style
remove_img = Image.open("img/remove.png")
remove_img.thumbnail((15, 15))
remove_icon = ImageTk.PhotoImage(remove_img)
remove_button = ttk.Button(top_frame, text="Remove", image=remove_icon, compound=tk.LEFT, command=lambda frame=top_frame: remove_task(frame))

# executing
root.mainloop()