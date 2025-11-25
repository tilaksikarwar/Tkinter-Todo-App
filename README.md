📝 Daily Tasks GUI

A Python Tkinter interface for a Daily Task Manager application. This script sets up the graphical user interface (GUI) layout, including input fields, a scrollable list for tasks, and control buttons.

📖 Overview

This code generates the frontend layout for a To-Do List application. It utilizes Python's built-in tkinter library to construct a user-friendly window where users can manage their daily activities.

✨ GUI Features

The interface includes the following components:

Task Input: A text entry field to type in new tasks.

Add Button: A stylized button (#d1e7dd) to submit new entries.

Task List: A scrollable Listbox capable of holding numerous items, paired with a vertical Scrollbar.

Action Buttons:

Done: To mark tasks as complete.

Edit: To modify existing entries.

Delete: To remove tasks (styled with red text for emphasis).

🛠️ Requirements

Python 3.x

Tkinter (Included with standard Python installations)

🚀 How to Run

Ensure you have Python installed.

Save the script to a file (e.g., main.py).

Run the script using the command line:

python main.py


🧩 Code Structure

The layout is organized using the .pack() geometry manager:

Root Window: Fixed size of 400x500.

Top Section: Header label and input entry.

Middle Section: A frame containing the Listbox and Scrollbar packed side-by-side.

Bottom Section: A button frame housing the operational buttons (Done, Edit, Delete).

⚠️ Note

This code provides the GUI layout and widget configuration. Ensure that the callback functions (add_task, mark_done, edit_task, delete_task, refresh_list) are defined in your script before running the mainloop, or the code will raise a NameError.
