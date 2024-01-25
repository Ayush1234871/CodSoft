import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bd=0, bg="#f0f0f0")
listbox.pack()

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#a6a6a6")
add_button.pack(side=tk.LEFT, padx=5)
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#a6a6a6")
remove_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()
