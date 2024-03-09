import tkinter
import tkinter.messagebox
import pickle
window=tkinter.Tk()
window.title("My to do list")
def task_adding():
    todo=task_add.get()
    if todo !="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="ATTENTION !",message="to add a task,enter some task")
def task_removing():
    try:
        index_todo=list_frame.curselection()[0]
        list_frame.delete(index_todo)

    except:
        tkinter.messagebox.showwarning(title="ATTENTION !   ",message="to delete a task ,you select a task")

def task_load():
    try:
        todo_list=pickle.load(open("tasks.dat","rb"))
        list_frame.delete(0,tkinter.END)
        for todo in todo_list:
            list_frame.insert(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION !",message="can not find task.dat")
def task_save():
    todo_list=list_frame.get(0,list_frame.size())
    pickle.dump(todo_list,open("tasks.dat","wb"))      

list_frame=tkinter.Frame(window)
list_frame.pack()
todo_box=tkinter.Listbox(list_frame,height=20,width=50)
todo_box.pack(side=tkinter.LEFT)
scroller=tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)
todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview)
task_add=tkinter.Entry(window,width=70)
task_add.pack()
add_task_button=tkinter.Button(window,text="CLICK TO ADD TASK",font=("arial",20,"bold"),background="orange",width=40,command=task_adding)
add_task_button.pack()

remove_task_button=tkinter.Button(window,text="CLICK TO DELETE TASK",font=("arial",20,"bold"),background="white",width=40,command=task_removing)
remove_task_button.pack()

load_task_button=tkinter.Button(window,text="CLICK TO LOAD TASK",font=("arial",20,"bold"),background="green",width=40,command=task_load)
load_task_button.pack()

save_task_button=tkinter.Button(window,text="click to save",font=("arial",20,"bold"),background="brown",width=40,command=task_save)
save_task_button.pack()
window.mainloop()