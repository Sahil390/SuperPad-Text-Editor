import tkinter
from tkinter import *
from tkinter import messagebox
import csv
import os

def newtask(event=None):
    task = my_entry.get()
    if task != "":
        lb.insert(END, f"{len(task_list) + 1}. {task}")
        my_entry.delete(0, "end")
        task_list.append(task)
        save_tasks_to_csv()
    else:
        messagebox.showwarning("Warning", "Please enter some task")


def deletetask(event=None):
    try:
        selected_task = lb.get(lb.curselection())
        lb.delete(lb.curselection())

        task = selected_task.split(". ", 1)[1]

        task_list.remove(task)
        save_tasks_to_csv()
    except TclError:
        messagebox.showwarning("Warning", "No task selected")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def save_tasks_to_csv():
    if not os.path.exists('tasks.csv'):
        open('tasks.csv', 'w').close()  # Create an empty file if it doesn't exist
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Task'])
        for task in task_list:
            writer.writerow([task])


def close_app(event=None):
    ws.destroy()


ws = Tk()
ws.geometry('550x380')
ws.title('TODO List')
ws.resizable(width=False, height=False)
ws.iconbitmap('icons//todo.ico')

label = Label(
    ws,
    text="Todo List",
    font=('Times', 24),
)
label.pack(pady=10)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=38,
    height=8,
    font=('Times', 18),
    bd=0,
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none",
    bg='white',
)
lb.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)

task_list = []

if os.path.exists('tasks.csv'):
    with open('tasks.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader):
            task = row[0]
            lb.insert(END, f"{i + 1}. {task}")
            task_list.append(task)

my_entry = Entry(
    ws,
    width=38,
    font=('times', 18)
)

my_entry.pack(pady=0)
my_entry.focus_set()

ws.bind('<Return>', newtask)
ws.bind('<Delete>', deletetask)
ws.bind('<Escape>', close_app)

ws.mainloop()
