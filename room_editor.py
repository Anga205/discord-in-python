import tkinter as tk
import mysql.connector, functions,homepage
def buildWindow(token,room_id):
    root=tk.Tk()
    grey="#36393f"
    root.title("Private Room Editor")
    root.geometry("1000x300")
    root.iconbitmap("assets/icon.ico")
    root.config(bg=grey)

    tk.Label(root,bg=grey,fg='WHITE',text='Private Room editor for: '+room_id,font='Calibri 32').pack()

    con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
    cur=con.cursor()
    cur.execute("select users from rooms where name='"+room_id+"'")
    users=[x for x in cur][0][0].split()
    usernames=[]

    for i in range(0,7):
        try:
            usernames.append(functions.getName(users[i]))
        except:
            usernames.append("")
    
    user1,user2,user3,user4,user5,user6,user7,privacy,error1,error2,error3,error4,error5,error6,error7,username1,username2,username3,username4,username5,username6,username7=tk.Frame(root,bg=grey),tk.Frame(root,bg=grey),tk.Frame(root,bg=grey),tk.Frame(root,bg=grey),tk.Frame(root,bg=grey),tk.Frame(root,bg=grey),tk.Frame(root,bg=grey),tk.IntVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
    user1.pack(),user2.pack(),user3.pack(),user4.pack(),user5.pack(),user6.pack(),user7.pack()
    
    
    tk.Label(user1,fg='WHITE',bg=grey,text="Enter Username of user 1 - ").pack(side=tk.LEFT),tk.Label(user2,fg='WHITE',bg=grey,text="Enter Username of user 2 - ").pack(side=tk.LEFT),tk.Label(user3,fg='WHITE',bg=grey,text="Enter Username of user 3 - ").pack(side=tk.LEFT),tk.Label(user4,fg='WHITE',bg=grey,text="Enter Username of user 4 - ").pack(side=tk.LEFT),tk.Label(user5,fg='WHITE',bg=grey,text="Enter Username of user 5 - ").pack(side=tk.LEFT),tk.Label(user6,fg='WHITE',bg=grey,text="Enter Username of user 6 - ").pack(side=tk.LEFT),tk.Label(user7,fg='WHITE',bg=grey,text="Enter Username of user 7 - ").pack(side=tk.LEFT)

    tk.Entry(user1,bg=grey,fg='WHITE',textvariable=username1).pack(side=tk.RIGHT),tk.Entry(user2,bg=grey,fg='WHITE',textvariable=username2).pack(side=tk.RIGHT),tk.Entry(user3,bg=grey,fg='WHITE',textvariable=username3).pack(side=tk.RIGHT),tk.Entry(user4,bg=grey,fg='WHITE',textvariable=username4).pack(side=tk.RIGHT),tk.Entry(user5,bg=grey,fg='WHITE',textvariable=username5).pack(side=tk.RIGHT),tk.Entry(user6,bg=grey,fg='WHITE',textvariable=username6).pack(side=tk.RIGHT),tk.Entry(user7,bg=grey,fg='WHITE',textvariable=username7).pack(side=tk.RIGHT),tk.Label(user1,bg=grey,fg='RED',textvariable=error1).pack(),tk.Label(user2,bg=grey,fg='RED',textvariable=error2).pack(),tk.Label(user3,bg=grey,fg='RED',textvariable=error3).pack(),tk.Label(user4,bg=grey,fg='RED',textvariable=error4).pack(),tk.Label(user5,bg=grey,fg='RED',textvariable=error5).pack(),tk.Label(user6,bg=grey,fg='RED',textvariable=error6).pack(),tk.Label(user7,bg=grey,fg='RED',textvariable=error7).pack()
    privacy.set(3)
    privacy_row=tk.Frame(root,bg=grey)
    privacy_row.pack()
    tk.Label(privacy_row,bg=grey,fg="WHITE",font="Calibri 12 bold", text="Change Privacy Settings - ").pack(side=tk.LEFT)
    tk.Checkbutton(privacy_row, text='Global Room',bg=grey,fg='BLUE',variable=privacy, onvalue=1, offvalue=3, command=lambda: print("public")).pack(side=tk.LEFT)
    tk.Checkbutton(privacy_row, text='Unlisted Room',bg=grey,fg='PURPLE',variable=privacy, onvalue=2, offvalue=3, command=lambda: print("unlisted")).pack(side=tk.LEFT)
    bottom_row=tk.Frame(root,bg=grey)
    bottom_row.pack()
    tk.Button(bottom_row,text="Save",fg='WHITE',bg="#5865f2",command=lambda: Submit()).pack(side=tk.LEFT)
    tk.Button(bottom_row,text="Delete Room",fg='WHITE',bg="RED",command=lambda: delete()).pack(side=tk.RIGHT)

    username1.set(usernames[0]),username2.set(usernames[1]),username3.set(usernames[2]),username4.set(usernames[3]),username5.set(usernames[4]),username6.set(usernames[5]),username7.set(usernames[6])

    def delete():
        con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
        cur=con.cursor()
        cur.execute("delete from rooms where name='"+room_id+"'")
        con.commit()
        con.close()
        con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="rooms")
        cur=con.cursor()
        cur.execute("drop table "+room_id)
        con.commit()
        con.close()
        root.destroy()
        homepage.buildWindow(token)

    def Submit():
        users=[username1.get(),username2.get(),username3.get(),username4.get(),username5.get(),username6.get(),username7.get()]
        tokens=[]
        spaces=[" "*x for x in range(0,32)]
        if username1.get() in spaces:
            pass
        else:
            try:
                tokens.append(functions.getToken(username1.get()))
            except:
                error1.set("Invalid Username (not found)")
                return False
        if username2.get() in spaces:
            pass
        else:
            try:
                tokens.append(functions.getToken(username2.get()))
            except:
                error2.set("Invalid Username (not found)")
                return False
        if username3.get() in spaces:
            pass
        else:
            try:
                tokens.append(functions.getToken(username3.get()))
            except:
                error3.set("Invalid Username (not found)")
                return False
        if username4.get() in spaces:
            pass
        else:
            try:
                tokens.append(functions.getToken(username4.get()))
            except:
                error4.set("Invalid Username (not found)")
                return False
        if username5.get() in spaces:
            pass
        else:
            try:
                tokens.append(functions.getToken(username5.get()))
            except:
                error5.set("Invalid Username (not found)")
                return False
        if username6.get() in spaces:
            pass
        else:
            try:
                tokens.append(functions.getToken(username6.get()))
            except:
                error6.set("Invalid Username (not found)")
                return False
        if username7.get() in spaces:
            pass
        else:
            try:
                tokens.append(functions.getToken(username7.get()))
            except:
                error7.set("Invalid Username (not found)")
                return False
        tokens=" ".join(tokens)
        cur.execute("update rooms set privacy="+str(privacy.get())+", users ='"+tokens+"' where name='"+room_id+"'")
        con.commit()
        root.destroy()
        homepage.buildWindow(token)
    def closing():
        root.destroy()
        homepage.buildWindow(token)
    root.protocol("WM_DELETE_WINDOW", lambda: closing())
    root.mainloop()
