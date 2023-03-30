import tkinter as tk
import time,functions,threading,mysql.connector

updateSpeed=500         #in milliseconds
spaces=[" "*x for x in range(100)]

users={}

displayed=[(" "," "," ")]

usedSpaces=1

def renderMessage(a):
    a=a.replace(":smile:","☺")
    a=a.replace(":frown:","🙁")
    a=a.replace("%date%",str(time.ctime(time.time())))
    return a

def DisplayMessage(user, message, Time):
    global displayed,usedSpaces
    #print(message)

    displayed.append((user,renderMessage(message),Time))

    if(displayed[-1][0]==displayed[-2][0]):

        message = tk.Label(frame_widgets, text=renderMessage(message),bg='#36393f', fg="#d1ddde", wraplength=window.winfo_width(), justify='left', font='Calibri 14')
        message.grid(row=usedSpaces+1, column=0, columnspan=3, sticky=(tk.N,tk.W))
        message.columnconfigure(0,weight=1)
        message.rowconfigure(1,weight=1)
        usedSpaces+=1

    else:

        Name = tk.Label(frame_widgets, text=user,bg='#36393f', fg='#ffffff', font='Calibri 16 bold')
        Name.grid(row=usedSpaces+1, column=0, columnspan=1, sticky=(tk.S,tk.W))
        Name.columnconfigure(0,weight=1)
        Name.rowconfigure(1,weight=1)
        usedSpaces+=1

        Time_Widget = tk.Label(frame_widgets, text=str(time.ctime(Time)),bg='#36393f', fg="#a3a6aa", font='Calibri 10')
        Time_Widget.grid(row=usedSpaces, column=1, columnspan=3, sticky=(tk.E))
        Time_Widget.columnconfigure(0,weight=1)
        Time_Widget.rowconfigure(1,weight=1)

        message = tk.Label(frame_widgets, text=renderMessage(message), wraplength=window.winfo_width(),justify='left',bg='#36393f', fg="#d1ddde", font='Calibri 14')
        message.grid(row=usedSpaces+1, column=0, columnspan=3, sticky=(tk.N,tk.W))
        message.columnconfigure(0,weight=1)
        message.rowconfigure(1,weight=1)
        usedSpaces+=1
    frame_widgets.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def NewlyAdded():
    global LastChecked, room
    con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="rooms")
    cur=con.cursor()
    command="select * from "+room+" where time>="+str(LastChecked)
    LastChecked=time.time()
    cur.execute(command)
    output=[]
    for x in cur:
        output.append(x)
    con.close()
    return output

def sendMessage(token):
    global spaces, room, textbox
    con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="rooms")
    cur=con.cursor()
    if textbox.get() in spaces:
        pass
    else:
        command="insert into "+room+" values ('"+token+"','"+str('"'.join(str(textbox.get()).split("'")))+"',"+str(time.time())+");"
        cur.execute(command)
        con.commit()
        con.close()
        textbox.delete(0, tk.END)

def update():
    try:
        global updateSpeed, empty
        def newMsgs():
            a=NewlyAdded()
            if a==[]:
                pass
            else:
                for i in a:
                    users[i[0]]=functions.getName(i[0])
                    DisplayMessage(users[i[0]],i[1],i[2])
        canvas.config(width=window.winfo_width()-vsb.winfo_width() ,height=window.winfo_height()-100)
        threading.Thread(target=newMsgs).start()
        window.after(updateSpeed,update)
    except:
        pass
    
def buildWindow(ConnectTo, token):

    global textbox,empty,window,LastChecked,room,spaces,frame_widgets,canvas,vsb,frame_canvas
    LastChecked=0.0

    if ConnectTo in spaces:
        room="global"
    else:
        room=ConnectTo

    window=tk.Tk()
    window.title("ChatRoom")
    window.geometry("710x600")
    window.iconbitmap("assets/icon.ico")
    window.columnconfigure(0,weight=1)
    window.rowconfigure(1,weight=1)
    window.config(bg="#36393f")

    UNameLabel=tk.Label(window, text="Room ID: "+ConnectTo,bg='#36393f', fg= "#ffffff", font='System 20')
    UNameLabel.grid(row=0, column=0, sticky=(tk.N,tk.W))

    frame_canvas=tk.Frame(window, width=window.winfo_width(), bg="#36393f")
    frame_canvas.grid(row=1, column=0, columnspan=3,sticky=(tk.W,tk.E,tk.S))

    canvas = tk.Canvas(frame_canvas, bg="#36393f", highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="news")

    vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)

    frame_widgets = tk.Frame(canvas, bg="#36393f", borderwidth=0)
    canvas.create_window((0, 0), window=frame_widgets, anchor='nw')



    frame_widgets.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    send = tk.Button(window, text="Send", font="Sans 12 bold", bg="#5865f2",fg="WHITE",command=lambda e: sendMessage(token))
    send.grid(row=2, column=2, sticky=(tk.E))
    window.bind('<Return>',lambda e:sendMessage(token)) 
    
    textbox = tk.Entry(window, bg="#40444b", fg="#d7d7d7", font="Calibri 17")
    textbox.grid(row=2, column=0, columnspan=2, sticky=(tk.E,tk.W))
    textbox.columnconfigure(0,weight=1)
    window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
    update()

    window.mainloop()

