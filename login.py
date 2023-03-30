import mysql.connector,requests,time,pickle,random,functions,homepage
import tkinter as tk
from PIL import ImageTk, Image
filename='user.info'

def sessionLogin():
    global filename
    try:
        credentials=pickle.load(open(filename,"rb"))
        con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
        cur=con.cursor()
        cur.execute("select * from users where token='"+credentials[0]+"'")
        info=[x for x in cur][0]
        if (credentials[1]==info[1]) and (credentials[2]==info[2]):
            con.close()
            loggedIn(credentials[0],credentials[1],credentials[2])
            return True
        else:
            return False
    except:
        try:
            con.close() 
            return False
        except:
            return False
    

def loginScreen():    
    def clearCredentials():
        username.delete(0,tk.END)
        password.delete(0,tk.END)
    def PassError(message):
        global passmessage
        try:
            passmessage.set(message)
        except:
            passmessage=tk.StringVar()
            tk.Label(root, textvariable=passmessage, bg="#36393f", fg="RED", wraplength=password.winfo_width()).grid(row=5, column=1)
            passmessage.set(message)

    def UNameError(message):
        global errormessage
        try:
            errormessage.set(message)
        except:
            errormessage=tk.StringVar()
            tk.Label(root, textvariable=errormessage, bg="#36393f", fg="RED", wraplength=username.winfo_width()).grid(row=3, column=1)
            errormessage.set(message)
    def BasicChecks():
        global errormessage,passmessage
        output=True
        if username.get()=="":
            UNameError("Please enter a username")
            output=False
        elif len(username.get())>32:
            UNameError("Username can not be more than 32 charectors long")
            output=False
        elif len(username.get())<3:
            UNameError("Username must be at least 3 charectors long")
            output=False
        elif not functions.isAlphaNumeric(username.get()):
            UNameError("Username must be alphanumeric")
            output=False
        else:
            pass
        if password.get()=="":
            PassError("Please enter a password")
            output=False
        elif len(password.get())<8:
            PassError("Password must be at least 8 charectors long")
            output=False
        elif len(password.get())>64:
            PassError("Password cannot be more than 32 charectors")
            output=False
        return output

    def registerChecks():
        if not BasicChecks():
            return False
        else:
            global con,cur
            con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
            cur=con.cursor()
            cur.execute("select * from users")
            users=[x[1].lower() for x in cur]
            if username.get().lower() in users:
                UNameError("This username is taken")
                return False
            else:
                return True

    def register():
        global con,cur
        if not registerChecks():
            try:
                con.close()
            except:
                pass
        else:
            cur.execute("insert into users values ('"+"".join([random.choice(list("QWERTYUIOPASDFGHJKLZXCVBNM1234567890")) for x in range(32)])+"','"+username.get()+"','"+password.get()+"','"+requests.get('https://api.ipify.org').text+"',"+str(time.time())+","+str(time.time())+",0.0)")
            con.commit()
            con.close()
            tk.Label(root, text=str("registered as "+username.get()+"! now re-enter your credentials to sign-in"), bg="#36393f", fg="WHITE", wraplength=150).grid(row=7, column=0, columnspan=2)
            clearCredentials()
            
    def loginChecks():
        if not BasicChecks():
            return False
        else:
            global con,cur
            con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
            cur=con.cursor()
            cur.execute("select * from users")
            users=[x[1] for x in cur]
            users2=[x.lower() for x in users]
            if username.get().lower() not in users2:
                UNameError("This username is not registered")
                con.close()
                return False
            elif username.get() not in users:
                UNameEError("Usernames are case-sensitive")
                con.close()
                return False
            else:
                return True
    def login():
        if loginChecks():
            global con,cur
            cur.execute("select * from users where username='"+username.get()+"'")
            info=[x for x in cur][0]
            if password.get()==info[2]:
                cur.execute("update users set lastjoin = "+str(time.time())+" where token='"+info[0]+"'")
                cur.execute("update users set ip = '"+requests.get('https://api.ipify.org').text+"' where token='"+info[0]+"'")
                con.commit()
                clearCredentials()
                root.destroy()
                loggedIn(info[0], info[1], info[2])
            else:
                PassError("Invalid Credentials, Username or password is wrong")
        else:
            pass
    root=tk.Tk()
    root.title("Login Or Register")
    root.geometry("500x500")
    root.iconbitmap("assets/icon.ico")
    root.config(bg="#36393f")

    ULabel=tk.StringVar()
    ULabel.set("Enter your username here - ")

    logo_img = ImageTk.PhotoImage(Image.open("assets/icon.png"))
    tk.Label(root, image = logo_img, bg="#36393f", borderwidth=10).grid(row=0, column=0, columnspan=2)

    text_img= ImageTk.PhotoImage(Image.open("assets/logintext.png"))
    tk.Label(root, image = text_img, bg="#36393f", borderwidth=20).grid(row=1, column=0, columnspan=2)

    tk.Label(root, textvariable=ULabel, bg="#36393f", fg="#d7d7d7", font="Terminal").grid(row=2, column=0)
    username=tk.Entry(root, bg="#40444b", fg="#d7d7d7", width=25)
    username.grid(row=2, column=1, sticky=(tk.W,tk.E))

    tk.Label(root, text="Enter your password here - ", bg="#36393f", fg="#d7d7d7", font="Terminal",borderwidth=10).grid(row=4, column=0)
    password=tk.Entry(root, bg="#40444b", fg="#d7d7d7", show="*")
    password.grid(row=4, column=1, sticky=(tk.W,tk.E))

    tk.Button(root, text="Sign in", font="Calibri 12 bold", bg="#5865f2", fg="WHITE",command=login).grid(row=6,column=0,columnspan=1)

    tk.Button(root, text="Register", bg="#36393f", fg="#d1ddde", font="Calibri 12 bold",command=register).grid(row=6,column=0, sticky=(tk.E),columnspan=1)
    
    root.mainloop()

def loggedIn(token, username, password):
    pickle.dump([token,username,password],open(filename,"wb"))
    homepage.buildWindow(token)

if not sessionLogin():
    loginScreen()
