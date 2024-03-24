import tkinter as tk
from tkinter import messagebox

def default(task):
    if task_entry.get()=="Enter your task here":
        task_entry.delete(0,"end")
        task_entry.config(fg="black")

def event(task):
    if task_entry.get()=="":
        task_entry.insert(0,"Enter your task here")
        task_entry.config(fg="grey")
        

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showerror("Error","Select the task which you wanted to remove.")

        
        
# Create the main application window
root = tk.Tk()
root.title("To-Do List")

#creting a temporary text in textbox as message
task_entry=tk.Entry(root,fg="grey",width=30)
task_entry.insert(0,"Enter your task here")
task_entry.bind('<FocusIn>',default)
task_entry.bind('<FocusOut>',event)
task_entry.pack(pady=10)

# Create and configure the task listbox widget
task_listbox=tk.Listbox(root,width=30)
task_listbox.insert(0,"The to do list:")
task_listbox.bind('<FocusIn>',default)
task_listbox.bind('<FocusOut>',event)
task_listbox.pack(pady=50)

# Create and configure the "Add" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create and configure the "Remove" button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

#main loop
root.mainloop()
