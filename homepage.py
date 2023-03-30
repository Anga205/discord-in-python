import tkinter as tk
import mysql.connector, chat, functions, createRoom, room_editor, profileEditor
from PIL import ImageTk, Image
users={}
def buildWindow(token):
    root=tk.Tk()
    root.title("Home Page")
    root.geometry("710x600")
    root.iconbitmap("assets/icon.ico")
    root.columnconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.config(bg="#36393f")
    
    def Connect(room_id):
        if RoomNameCheck(room_id):
            con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
            cur=con.cursor()
            cur.execute("select privacy,users from rooms where name='"+room_id+"'")
            output=[x for x in cur][0]

            if output[0] in [1,2]:
                root.destroy()
                chat.buildWindow(room_id,token)
                buildWindow(token)
            else:
                if token in output[1].split():
                    root.destroy()
                    chat.buildWindow(room_id,token)
                else:
                    RoomNameError("You do not have access to this private room.")

    tk.Label(root,text="Welcome, "+functions.getName(token)+"! Select a room to join - ", bg="#36393f",fg="WHITE", font="Calibri 25 bold").grid(row=0,column=0,sticky=(tk.W))

    def Settings():
        root.destroy()
        profileEditor.buildWindow(token)


    settings_img=ImageTk.PhotoImage(Image.open("assets/settings.png"))
    settings=tk.Label(root,image=settings_img,bg="#36393f", cursor='hand2')
    settings.grid(row=0,column=1,sticky=(tk.E))
    settings.bind('<Button-1>', lambda a: Settings())

    con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
    cur=con.cursor()
    cur.execute("select * from rooms where privacy=1")
    publicrooms=[x[0] for x in cur]

    cur.execute("select * from rooms where privacy=3 and users like '%"+token+"%'")
    privaterooms=[x[0] for x in cur]
    con.close()
    usedSpaces=1

    rooms_frame=tk.Frame(root,bg="#36393f")
    rooms_frame.grid(row=usedSpaces, column=0, sticky=(tk.N,tk.W))

    def newRoomDisplay(name):
        nonlocal rooms_frame,usedSpaces
        label=tk.Label(rooms_frame,text=name,cursor='hand2',bg="#36393f",fg="#0067d6", font="Calibri 13 underline")
        label.grid(row=usedSpaces, column=0, columnspan=2, sticky=(tk.W,tk.N))
        label.bind('<Button-1>', lambda a:  Connect(name))

    def privRoomDisplay(name):
        nonlocal rooms_frame,usedSpaces
        label=tk.Label(rooms_frame,text=name,cursor='hand2',bg="#36393f",fg="RED", font="Calibri 13 underline")
        label.grid(row=usedSpaces, column=0, columnspan=2, sticky=(tk.W,tk.N))
        label.bind('<Button-1>', lambda a: Connect(name))
        label.bind('<Button-2>', lambda a: edit(name))
        label.bind('<Button-3>', lambda a: edit(name))

    for i in publicrooms:
        newRoomDisplay(i)
        usedSpaces+=1

    def edit(room_id):
        root.destroy()
        room_editor.buildWindow(token,room_id)


    for i in privaterooms:
        privRoomDisplay(i)
        usedSpaces+=1

    def RoomNameError(error):
        try:
            global roomError
            roomError.set(error)
        except:
            roomError=tk.StringVar()
            roomError.set(error)
            tk.Label(root, textvariable=roomError, bg="#36393f", fg="RED",wraplength=room_id.winfo_width()).grid(row=usedSpaces,column=0, sticky=(tk.E))

    def RoomNameCheck(name):
        output=True
        if name=="" or name in " ".join([" " for x in range(32)]):
            output=False
            RoomNameError("please enter a room id")
        elif not functions.isAlphaNumeric(name):
            output=False
            RoomNameError("room names must be alphanumeric")
        elif len(name)>32:
            output=False
            RoomNameError("room names cannot be more than 32 charectors")
        elif len(name)<3:
            output=False
            RoomNameError("room names cannot be less than 3 charectors")
        elif not RoomExists(name):
            output=False
            RoomNameError("room does not exist, try creating instead?")
        return output

    room_id=tk.Entry(root, bg="#36393f", fg="WHITE", font="Calibri 13")
    room_id.grid(row=usedSpaces, column=0, sticky=(tk.E,tk.S))

    connect_img=ImageTk.PhotoImage(Image.open("assets/connect.png"))
    ConnectTo=tk.Label(root,image=connect_img,cursor='hand2',bg="#36393f")
    ConnectTo.bind('<Button-1>', lambda a: Connect(room_id.get()))
    ConnectTo.grid(row=usedSpaces, column=1, sticky=(tk.W,tk.S))

    def builder():
        abc=room_id.get()
        root.destroy()
        createRoom.buildWindow(token, abc)

    plus_img=ImageTk.PhotoImage(Image.open("assets/plus.png"))
    addNew=tk.Label(root,image=plus_img,cursor='hand2',bg="#36393f")
    addNew.bind('<Button-1>', lambda a: builder())
    addNew.grid(row=usedSpaces, column=1, sticky=(tk.E,tk.S))
    
    tk.Label(root, text="Or enter a custom room ID to connect to/create -",bg="#36393f",fg="WHITE", font="Calibri 13").grid(row=usedSpaces, column=0, sticky=(tk.W,tk.S))
    usedSpaces+=1

    def RoomExists(name):
        con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="rooms")
        cur=con.cursor()
        cur.execute("show tables")
        rooms=[x[0].lower() for x in cur]
        con.close()
        if name.lower() in rooms:
            return True
        else:
            return False
    root.mainloop()
