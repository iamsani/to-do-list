import tkinter
import tkinter.messagebox
import pickle

window=tkinter.Tk()
window.title("To-Do-List")

def task1():
    todo= task_add.get()
    if todo!="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention!!",message="To Add a task plz Enter some task")
        
def task2():
    try:
        index= list_frame.curselection()[0]
        list_frame.delete(index)
    except:
        tkinter.messagebox.showwarning(title="Attention!!",message="To delete a task you must select a task")
    
def task3():
    try:
        todo_list=pickle.load(open("Tasks,dat","rb"))
        list_frame.delete(0,tkinter,END)
        for todo in tasks:
            list_frame.inset(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="Attention",message="Cannot find task.dat")

def task4():
    todo_list = list_frame.get(0,list_frame.size())
    pickle.dump(todo_list,open("task.dat","wb"))



list_frame= tkinter.Frame(window)
list_frame.pack()

todo_box=tkinter.Listbox(list_frame,height=30,width=50)
todo_box.pack(side=tkinter.LEFT)

scroller=tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)

task_add=tkinter.Entry(window,width=70)
task_add.pack()

add_task_button=tkinter.Button(window,text="Click to add task",font=("arial",20,"bold"),background="red",width=40,command=task1)
add_task_button.pack()

remove=tkinter.Button(window,text="Click To Delete Task",font=("arial",20,"bold"),background="Blue",width=40,command=task2)
remove.pack()

load=tkinter.Button(window,text="Click to load task",font=("arial",20,"bold"),background="yellow",width=40,command=task3)
load.pack()

#save=tkinter.Button(window,text="Click to save Task",font=("arial",20,"bold"),background="green",width=40,command=task4)
#save.pack()

window.mainloop()
