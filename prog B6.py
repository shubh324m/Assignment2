from tkinter import*
print("--MENU--")
print("1. Draw Rectangle")
print("2. Draw Oval")
print("3. Draw GUI controls - Label, Entry, Button")
print("4. Exit")

while(True):
    i=int(input("Enter your choice : "))
    if(i==1):
        top=Tk()
        top.geometry("400x400")
        c=Canvas(top,bg="blue",height=400,width=400)
        rec=c.create_rectangle(20,20,200,100, outline="red", fill="grey", width=2)
        c.pack()
        top.mainloop()
    elif(i==2):
        top=Tk()
        top.geometry("400x400")
        c=Canvas(top,bg="blue", height=400, width=400)
        oval=c.create_oval(10,10,200,100, outline="red", fill="yellow", width=2)
        c.pack()
        top.mainloop()
    elif(i==3):
        def show_entry_fields():
            print("First Name : ",e1.get())
            print("Last Name : ",e2.get())
            print("Course : ",e3.get())
        master=Tk()
        Label(master,text="First Name").grid(row=0)
        Label(master,text="Last Name").grid(row=0,column=2)
        Label(master,text="Course").grid(row=1)
        e1=Entry(master)
        e2=Entry(master)
        e3=Entry(master)
        e1.grid(row=0,column=1)
        e2.grid(row=0, column=3)
        e3.grid(row=1, column=1)
        Button(master, text="Quit", command=quit).grid(row=3, column=0, sticky=W, pady=4)
        Button(master, text="Show", command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
        mainloop()
    elif(i==4):
        break
    else:
        print("Invalid Choice")
    
