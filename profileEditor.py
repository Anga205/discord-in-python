import tkinter as tk
import mysql.connector, functions,homepage

def buildWindow(token):
    root=tk.Tk()
    grey="#36393f"
    root.title("Profile Editor")
    root.geometry("1000x300")
    root.iconbitmap("assets/icon.ico")
    root.config(bg=grey)

    tk.Label(root,bg=grey,fg='WHITE',text="Edit Your Profile",font="Calibri 32 bold").pack()
    name,pswd,auth,nmerror,passerror,autherror=tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
    name.set(functions.getName(token))
    username=tk.Frame(root,bg=grey)
    username.pack()
    tk.Label(username,bg=grey,fg='WHITE',text="Edit your username - ").pack(side=tk.LEFT)
    tk.Entry(username,bg=grey,fg="WHITE",textvariable=name).pack(side=tk.LEFT)
    tk.Label(username,bg=grey,fg='RED',textvariable=nmerror).pack()

    def BasicChecks():
        output=True
        if name.get() == functions.getName(token) and pswd.get()=="":
            autherror.set("What do you even want to update?")
            output=False
        if name.get()=="":
            nmerror.set("Username cant be empty")
            output=False
        if len(name.get())>32:
            nmerror.set("Username too long (max 32 charectors)")
            output=False
        if len(name.get())<3:
            nmerror.set("Username too short! (min. 3 charectors)")
            output=False
        if not functions.isAlphaNumeric(name.get()):
            nmerror.set("Username must be alphanumeric!")
            output=False
        if len(pswd.get())<8:
            passerror.set("Password must be at least 8 long")
            output=False
        if len(pswd.get())>32:
            passerror.set("Password too long (max 32 charectors)")
            output=False
        if auth.get() in [" "*x for x in range(32)]:
            autherror.set("Password cannot be blank")
            output=False
        return output

    def AuthCheck():
        if BasicChecks():
            con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
            cur=con.cursor()
            cur.execute("select password from users where token='"+token+"'")
            password=[x for x in cur][0][0]
            cur.execute("select name from users")
            names=[x[0] for x in cur]
            con.close()
            if password==auth.get():
                if name.get() in names:
                    nmerror("username is taken")
                    return False
                else:
                    return True
            else:
                autherror.set("Password is incorrect.")
                return False
        else:
            return False
    
    def Change():
        if AuthCheck():
            if pswd.get()=="":
                con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
                cur=con.cursor()
                cur.execute("select password from users where token='"+token+"'")
                password=[x for x in cur][0][0]
            else:
                password=pswd.get()
            username=name.get()
            cur.execute("update users set username='"+username+"', password='"+password+"' where token='"+token+"'")
            con.commit()
            con.close()
            root.destroy()
            homepage.buildWindow(token)
        else:
            pass

    password=tk.Frame(root,bg=grey)
    password.pack()
    tk.Label(password,bg=grey,text="Edit your password - ",fg="WHITE").pack(side=tk.LEFT)
    tk.Entry(password,bg=grey,fg="WHITE",textvariable=pswd,show="*").pack(side=tk.LEFT)
    tk.Label(password,bg=grey,fg='RED',textvariable=passerror).pack()

    finalising=tk.Frame(root,bg=grey)
    finalising.pack()
    tk.Label(finalising,bg=grey,text="Type your original password (auth) - ",fg="WHITE").pack(side=tk.LEFT)
    tk.Entry(finalising,textvariable=auth,show="*",fg='WHITE',bg=grey).pack(side=tk.LEFT)
    tk.Label(username,bg=grey,fg='RED',textvariable=autherror).pack()

    actions=tk.Frame(root,bg=grey)
    actions.pack()
    tk.Button(actions,text="Save",fg="WHITE",bg="#5865f2",command= lambda: Change()).pack(side=tk.LEFT)
    tk.Button(actions,text="Delete",fg="WHITE",bg="RED",command= lambda: print("Deleting is currently not enabled yet")).pack(side=tk.LEFT)
    
    def closing():
        root.destroy()
        homepage.buildWindow(token)
    root.protocol("WM_DELETE_WINDOW", lambda: closing())
    root.mainloop()