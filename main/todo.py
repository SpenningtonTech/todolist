import tkinter as tk
from tkinter import *


class ToDoList(tk.Tk):

    def __init__(self):
        self.task_list = []

        tk.Tk.__init__(self)
        self.v = StringVar()

        self.title('ToDo List')
        self.text = tk.Text(height=10, width=30)
        self.entry = tk.Entry(self)
        self.add_button = tk.Button(text='add', command=self.add_task)
        self.remove_button = tk.Button(text='remove', command=self.remove_task)
        self.save_button = tk.Button(text='Save', command=self.save_file)

        self.save_button.grid(row=3)
        self.text.grid(row=1, column=0, sticky=N)
        self.entry.grid(row=2, column=0, sticky=W)
        self.add_button.grid(row=3, column=0, sticky=W)
        self.remove_button.grid(row=3, column=1, sticky=E)

        self.load_file()

    def update_task(self):

        self.text.delete(1.0, tk.END)
        self.text.insert(INSERT, self.task_list)

    def add_task(self):

        self.task_list.append(self.entry.get())
        self.entry.delete('0', '20')
        self.update_task()
        return self.task_list

    def remove_task(self):

        self.task_list.remove(self.entry.get())
        self.update_task()
        return self.task_list

    def save_file(self):
        file = open('save.txt', 'w')
        file.write(self.text.get(1.0, END))
        file.close()

    def load_file(self):
        with open('save.txt', 'r') as f:
            self.text.insert(INSERT, f.read())


app = ToDoList()
app.mainloop()
