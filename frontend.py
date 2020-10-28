from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

# indexerror occurs when try and except is not their and our listbox in window is empty and clicked on it

def view_command():
    list1.delete(0,END)   
    # start from index 0 of the listbox
    for row in backend.view():
        list1.insert(END,row)
    # here end is because to insert at the end of the already existing line 

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),jsbn_text.get()):
        list1.insert(END,row) 

def add_command():
    # print(title_text.get(),author_text.get(),year_text.get(),jsbn_text.get())
    if (title_text.get()!="" and author_text.get()!="" and year_text.get()!="" and jsbn_text.get()!= ""):
        backend.insert(title_text.get(),author_text.get(),year_text.get(),jsbn_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),jsbn_text.get()))
        # to insert in the listbox
    else:
        pass

def delete_command():
    try:
        backend.delete(selected_tuple[0])
        list1.delete(0,END)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        for row in backend.view():
            list1.insert(END,row)
    except NameError:
        pass        

def update_command():
    try:
        backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),jsbn_text.get())
        # to known the parameters for update see backend.py
        list1.delete(0,END)
        for row in backend.view():
            list1.insert(END,row)
    except NameError:
        pass

window = Tk()
window.wm_title("BookStore")


l1 = Label(window,text="Title")
l1.grid(row=0,column=0)


l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="jsbn")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

jsbn_text = StringVar()
e4 = Entry(window,textvariable=jsbn_text)
e4.grid(row=1,column=3)



list1 = Listbox(window,height=10,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",get_selected_row)

b1 = Button(window,text="View all",command=view_command,width=12)
b1.grid(row=2,column=3)


b2 = Button(window,text="Search Entry",command=search_command,width=12)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add Entry",command=add_command,width=12)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update Selected",command=update_command,width=12)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete Selected",command=delete_command,width=12)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()



















