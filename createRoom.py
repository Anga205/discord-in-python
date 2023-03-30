import tkinter as tk
import functions,mysql.connector, homepage
def buildWindow(token,givenID=""):
    grey="#36393f"

    root=tk.Tk()
    root.title("Create A new room")
    root.geometry("500x400")
    root.iconbitmap("assets/icon.ico")
    root.config(bg=grey)

    tk.Label(root,text="Create a new room",bg=grey,fg='WHITE',font="Calibri 30",highlightthickness=30,highlightbackground=grey).pack()

    name=tk.Frame(root, bg=grey)
    name.pack()

    room_id=tk.Entry(name, bg=grey, fg="WHITE")
    room_id.pack(side=tk.RIGHT)
    room_id.insert(0,givenID)

    tk.Label(name, text="Enter a room ID", bg=grey, fg="WHITE",highlightbackground=grey,highlightthickness=25).pack(side=tk.LEFT)  

    privacy=tk.Frame(root, bg=grey)
    privacy.pack()


    var=tk.IntVar()
    var.set(1)
    public=tk.Checkbutton(privacy, text='Global Room',bg=grey,fg='BLUE',variable=var, onvalue=1, offvalue=0, command=lambda: print("public"))
    unlisted=tk.Checkbutton(privacy, text='Unlisted Room',bg=grey,fg='PURPLE',variable=var, onvalue=2, offvalue=0, command=lambda: print("unlisted"))
    private1=tk.Checkbutton(privacy, text='Private Room',bg=grey,fg='RED',variable=var,onvalue=3,offvalue=0,command=lambda: print("private"))
    tk.Label(privacy, text="Select a privacy level for your room - ",fg='WHITE',bg=grey).pack(side=tk.LEFT)
    public.pack(side=tk.LEFT)
    unlisted.pack(side=tk.LEFT)
    private1.pack(side=tk.LEFT)

    def BasicChecks():
        if room_id.get()=="":
            errorMSG.set("Please Enter a valid room ID")
            return False
        elif len(room_id.get())>32:
            errorMSG.set("Room id too long (max 32 charectors)")
            return False
        elif not functions.isAlphaNumeric(room_id.get()):
            errorMSG.set("Room ID must be alphanumeric")
            return False
        elif len(room_id.get())<3:
            errorMSG.set("Room ID too short (min 3 charectors)")
            return False
        elif var.get()==0:
            errorMSG.set("Please select a privacy setting.")
            return False
        else:
            return True

    def AdvancedChecks():
        if not BasicChecks():
            return False
        else:
            print("passed basic checks")
            con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
            cur=con.cursor()
            cur.execute("select * from rooms where name='"+room_id.get()+"'")
            rooms=[x for x in cur]
            con.close()
            if not rooms==[]:
                errorMSG.set("Room name already exists!")
                return False
            else:
                return True
    
    def CreateRoom():
        if AdvancedChecks():
            print("passed all checks")
            con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
            cur=con.cursor()
            if var.get()==3:
                users="'"+token+"'"
            else:
                users="NULL"
            cur.execute("insert into rooms values('"+room_id.get()+"',"+str(var.get())+","+users+")")
            con.commit()
            con.close()
            con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="rooms")
            cur=con.cursor()
            cur.execute("create table "+room_id.get()+" (token varchar(32),message mediumtext, time double);")
            con.commit()
            con.close()
            root.destroy()
            homepage.buildWindow(token)

    finish=tk.Frame(root,bg=grey)
    finish.pack(side=tk.BOTTOM)

    errorMSG=tk.StringVar()
    tk.Button(finish,text="Create Room",bg='#5865f2',fg='WHITE',font='Calibri 12 bold',command=lambda: CreateRoom()).pack()
    tk.Label(finish,textvariable=errorMSG,bg=grey,fg="RED").pack(side=tk.BOTTOM)

    root.mainloop()
