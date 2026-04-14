import tkinter as tk
import json

# Load tasks
try:
    with open('tasks.json','r') as f:
        tasks = json.load(f)
except:
    tasks = []

# Save function
def save_tasks():
    with open('tasks.json','w') as f:
        json.dump(tasks, f)

# Update list display
def update_list():
    listbox.delete(0, tk.END)
    for i, t in enumerate(tasks):
        status = "✔️" if t['done'] else " "
        listbox.insert(tk.END, f"{i}. [{status}] {t['task']}")

# Add task
def add_task():
    task = entry.get()
    if not task.strip():
        return
    tasks.append({"task": task, "done": False})
    save_tasks()
    update_list()
    entry.delete(0, tk.END)

# Delete task
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks()
        update_list()
    except:
        pass

# Mark done (toggle)
def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]['done'] = not tasks[index]['done']
        save_tasks()
        update_list()
    except:
        pass

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.configure(bg='#1e1e1e')

title=tk.Label(root,text='my-to-do-list', font=("Arial", 16, 'bold'), bg="#1e1e1e", fg="#ffffff")
title.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task,bg="#aCAF50", fg="#ffffff",width=20)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40,height=10,font=("Arial",11))
listbox.pack(pady=10)

frame=tk.Frame(root,bg="#1e1e1e")
frame.pack(pady=10)

done_btn = tk.Button(frame, text="Mark Done", command=mark_done,bg="#2196F3", fg="#ffffff",width=12)
done_btn.grid(row=0,column=0,padx=5)

del_btn = tk.Button(frame, text="Delete Task", command=delete_task, bg="#f44336", fg="#ffffff", width=12)
del_btn.grid(row=0,column=1,padx=5)

# Initial load
update_list()

root.mainloop()