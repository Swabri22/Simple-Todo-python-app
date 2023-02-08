import tkinter as tk
//identifying the variables
def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)

app = tk.Tk()
app.title("To-Do App")

task_label = tk.Label(text="Task:")
task_label.grid(row=0, column=0)

task_entry = tk.Entry()
task_entry.grid(row=0, column=1)

add_task_button = tk.Button(text="Add Task", command=add_task)
add_task_button.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=40)

tasks = []
task_list = tk.Listbox(height=8, width=50)
task_list.grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()
