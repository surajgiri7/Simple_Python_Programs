import tkinter
from tkinter.constants import END
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do_List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")
    # pass

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
    # pass

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="No datafile tasks.dat")

    # pass

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
    # print(tasks)
    # pass

#Creating GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

#Creating a scroll bar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#Creating list
listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack()

#configuring scrollbar on the left side of the task list
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

#Creating the task entry box
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

#Creating add task button
button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

#Creating delete task button
button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

#Creating load task button
button_load_task = tkinter.Button(root, text="Load task", width=48, command=load_task)
button_load_task.pack()

#Creating save task button
button_save_task = tkinter.Button(root, text="Save task", width=48, command=save_task)
button_save_task.pack()

root.mainloop()