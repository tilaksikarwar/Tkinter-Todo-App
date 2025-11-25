import tkinter as tk
from tkinter import messagebox
import os

# basic config
FILE_NAME = "todo_list.txt"
tasks = []

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                for line in f:
                    clean_line = line.strip()
                    if clean_line: # check if line is not empty
                        tasks.append(clean_line)
        except:
            print("Could not load file.")

def save_data():
    try:
        with open(FILE_NAME, "w") as f:
            for t in tasks:
                f.write(t + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't save: {e}")

def refresh_list():
    # listbox is defined in global scope at bottom
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, t)

# --- Button Functions ---

def add_task():
    val = task_entry.get()
    if val != "":
        new_task = f"[ ] {val}"
        tasks.append(new_task)
        save_data()
        refresh_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task name can't be empty!")

def mark_done():
    try:
        idx = listbox.curselection()[0]
        current = tasks[idx]
        
        if "[ ]" in current:
            # FIX: only replace the first instance so we don't mess up task text
            tasks[idx] = current.replace("[ ]", "[x]", 1)
            save_data()
            refresh_list()
        else:
            messagebox.showinfo("Info", "Already done.")
            
    except IndexError:
        messagebox.showerror("Error", "Select a task first.")

def delete_task():
    try:
        idx = listbox.curselection()[0]
        removed = tasks.pop(idx)
        save_data()
        refresh_list()
    except IndexError:
        messagebox.showerror("Error", "Select a task to delete.")

def edit_task():
    try:
        idx = listbox.curselection()[0]
        curr_text = tasks[idx]
        
        # assumes format "[ ] text" (4 chars prefix)
        desc = curr_text[4:] 

        top = tk.Toplevel(root)
        top.title("Edit Task")
        top.geometry("300x100")

        tk.Label(top, text="Edit name:").pack()
        
        e_edit = tk.Entry(top, width=30)
        e_edit.insert(0, desc)
        e_edit.pack(pady=5)

        def save_edit():
            new_desc = e_edit.get()
            if new_desc:
                prefix = curr_text[:4] 
                tasks[idx] = prefix + new_desc
                save_data()
                refresh_list()
                top.destroy()
            else:
                messagebox.showwarning("Warning", "Empty task!")

        tk.Button(top, text="Save", command=save_edit).pack()

    except IndexError:
        messagebox.showerror("Error", "Select something to edit.")

# --- Main GUI Setup ---

if __name__ == "__main__":
    load_data()

    root = tk.Tk()
    root.title("My To-Do List")
    root.geometry("400x500")

    tk.Label(root, text="Daily Tasks", font=("Helvetica", 16, "bold")).pack(pady=10)

    task_entry = tk.Entry(root, width=40)
    task_entry.pack(pady=5)

    btn_add = tk.Button(root, text="Add Task", bg="#d1e7dd", command=add_task)
    btn_add.pack(pady=5)

    frame = tk.Frame(root)
    frame.pack(pady=10)
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # listbox needs to be global for functions to see it
    listbox = tk.Listbox(frame, width=45, height=15, yscrollcommand=scrollbar.set)
    listbox.pack(side=tk.LEFT)
    
    scrollbar.config(command=listbox.yview)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Done", width=10, command=mark_done).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Edit", width=10, command=edit_task).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Delete", width=10, fg="red", command=delete_task).pack(side=tk.LEFT, padx=5)

    # Load initial list
    refresh_list()
    
    root.mainloop()