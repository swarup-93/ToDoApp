import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("700x650")  # Window size
        self.root.configure(bg="#2c3e50")

        # Set the app's favicon (make sure 'favicon.png' is in the same directory)
        self.root.iconphoto(False, tk.PhotoImage(file="favicon.png"))  # Adjust the file name and path if necessary

        # Create the main frame
        frame = tk.Frame(self.root, bg="#2c3e50")
        frame.pack(fill="both", expand=True)

        # Title label
        title_label = tk.Label(frame, text="To-Do List", font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
        title_label.pack(pady=10)

        # Input field frame
        input_frame = tk.Frame(frame, bg="#2c3e50")
        input_frame.pack(pady=10)

        # Text widget for task input with increased height
        self.task_input = tk.Text(input_frame, height=3, width=25, font=("Arial", 16), wrap="word")  # Use Text widget with height property
        self.task_input.grid(row=0, column=0, padx=5, pady=10)  # Adjust padding for more height

        # Add button with rounded corners (manually created)
        self.add_button = self.create_rounded_button(input_frame, "Add", self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        # Task list box with increased height
        self.task_listbox = tk.Listbox(frame, width=50, height=10, font=("Arial", 14), bg="#34495e", fg="white", selectbackground="#2980b9", selectforeground="white")  # Increased height
        self.task_listbox.pack(pady=10)

        # Delete Selected and Clear All buttons
        button_frame = tk.Frame(frame, bg="#2c3e50")
        button_frame.pack(pady=10)

        # Create Delete Selected button with rounded corners (manually created)
        self.delete_button = self.create_rounded_button(button_frame, "Delete Selected Task", self.delete_selected_task)
        self.delete_button.grid(row=0, column=0, padx=45, pady=20)

        # Create Clear All button with rounded corners (manually created)
        self.clear_button = self.create_rounded_button(button_frame, "Clear All Tasks", self.clear_all_tasks)
        self.clear_button.grid(row=0, column=1, padx=45, pady=10)

        # Task list to hold tasks
        self.tasks = []

    def create_rounded_button(self, parent, text, command):
        """Creates a rounded button."""
        button = tk.Button(parent, text=text, font=("Arial", 14), fg="white", bg="#28a745", relief="flat", command=command)
        button.config(width=18, height=2)  # Adjust width and height for a more reasonable button size
        button.grid_propagate(False)  # Prevent the button from resizing
        button.configure(borderwidth=0, padx=15, pady=10)  # Add internal padding to make text look centered
        return button

    def add_task(self):
        task = self.task_input.get("1.0", "end-1c").strip()  # Get text from the Text widget
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete("1.0", "end")  # Clear the input after adding the task

    def delete_selected_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            pass  # Handle case if no task is selected

    def clear_all_tasks(self):
        self.tasks.clear()
        self.task_listbox.delete(0, tk.END)

# Create the root window
root = tb.Window(themename="darkly")  # Use the 'darkly' theme from ttkbootstrap
app = TodoApp(root)
root.mainloop()
