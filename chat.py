import tkinter as tk
import random,time

try:
    import tkhtmlview as tkh
except:
    import sys,subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','tkhtmlview'])

updateSpeed=500         #in milliseconds
BG_GRAY = "#36393f"
BG_COLOR = "#36393f"
TEXT_COLOR = "#d7d7d7"
spaces=[" "*x for x in range(100)]

try:
    open("messages.txt","r")
except:
    open("messages.txt","w").write(str({5937293492: [43, 'Hello, World!', 1666617000.272839]}))

displayed={5937293492: [43, 'Hello, World!', 1666617000.272839]}

usedSpaces=1

def uniqueID(list1=list(displayed.keys()),digits=9):
    a="".join([str(random.randint(0,9))for x in range(digits)])
    if a not in list1:
        return a
    else:
        return NewID(list1, digits)

def renderMessage(a):
    a=a.replace(":smile:","☺")
    a=a.replace(":frown:","🙁")
    a=a.replace("%date%",str(time.ctime(time.time())))
    return a


window=tk.Tk()
window.title("ChatRoom")
window.geometry("710x710")
window.iconbitmap("discord.ico")
window.columnconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.config(bg=BG_GRAY)


UNameLabel=tk.Label(window, text="Enter your Username:",bg='#36393f', fg= "#ffffff", font='System 20')
UNameLabel.grid(row=0, column=0, sticky=(tk.N,tk.W))


UName = tk.Entry(window, bg="#36393f", fg=TEXT_COLOR, font="System 20")
UName.grid(row=0, column=1, sticky=(tk.W))
UName.columnconfigure(0,weight=1)   


frame=tk.Frame(window, width=window.winfo_width(), bg="#36393f")
frame.grid(row=1, column=0, columnspan=3,sticky=(tk.W,tk.E,tk.S))


def DisplayMessage(ID, user, message, time):
    global displayed,usedSpaces
    #print(message)

    displayed[ID]=[user,renderMessage(message),time]
    exec(str("global message"+list(displayed.keys())[-1]))

    if(displayed[list(displayed.keys())[-1]][0]==displayed[list(displayed.keys())[-2]][0]):

        exec(str("message"+list(displayed.keys())[-1]+" = tk.Label(frame, text=displayed[list(displayed.keys())[-1]][1],bg='#36393f', fg=TEXT_COLOR, wraplength=window.winfo_width(), justify='left', font='Calibri 14')"))
        exec(str("message"+list(displayed.keys())[-1]+".grid(row=usedSpaces+1, column=0, columnspan=3, sticky=(tk.N,tk.W))"))
        exec(str("message"+list(displayed.keys())[-1]+".columnconfigure(0,weight=1)"))
        exec(str("message"+list(displayed.keys())[-1]+".rowconfigure(1,weight=1)"))
        usedSpaces+=1

    else:

        exec(str("Name"+list(displayed.keys())[-1]+" = tk.Label(frame, text=displayed[list(displayed.keys())[-1]][0],bg='#36393f', fg='#ffffff', font='Calibri 16')"))
        exec(str("Name"+list(displayed.keys())[-1]+".grid(row=usedSpaces+1, column=0, columnspan=1, sticky=(tk.S,tk.W))"))
        exec(str("Name"+list(displayed.keys())[-1]+".columnconfigure(0,weight=1)"))
        exec(str("Name"+list(displayed.keys())[-1]+".rowconfigure(1,weight=1)"))
        usedSpaces+=1

        exec(str("time"+list(displayed.keys())[-1]+" = tk.Label(frame, text=displayed[list(displayed.keys())[-1]][2],bg='#36393f', fg=TEXT_COLOR, font='Calibri 10')"))
        exec(str("time"+list(displayed.keys())[-1]+".grid(row=usedSpaces, column=1, columnspan=2, sticky=(tk.E))"))
        exec(str("time"+list(displayed.keys())[-1]+".columnconfigure(0,weight=1)"))
        exec(str("time"+list(displayed.keys())[-1]+".rowconfigure(1,weight=1)"))

        exec(str("message"+list(displayed.keys())[-1]+" = tk.Label(frame, text=displayed[list(displayed.keys())[-1]][1], wraplength=window.winfo_width(),justify='left',bg='#36393f', fg=TEXT_COLOR, font='Calibri 14')"))
        exec(str("message"+list(displayed.keys())[-1]+".grid(row=usedSpaces+1, column=0, columnspan=3, sticky=(tk.N,tk.W))"))
        exec(str("message"+list(displayed.keys())[-1]+".columnconfigure(0,weight=1)"))
        exec(str("message"+list(displayed.keys())[-1]+".rowconfigure(1,weight=1)"))
        usedSpaces+=1


def NewlyAdded():
    global displayed
    new=eval(open("messages.txt","r").read())
    for i in displayed:
        del new[i]
    return new        

def sendMessage(a=""):
    global spaces
    if textbox.get() in spaces:
        pass
    else:
        temp=eval(open("messages.txt","r").read())
        ID=uniqueID(list(displayed.keys()))
        if UName.get()=="":
            temp[ID]=["Anonymous User",textbox.get(),time.ctime(time.time())]
        else:
            temp[ID]=[UName.get(),textbox.get(),time.ctime(time.time())]
        open("messages.txt","w").write(str(temp))
        textbox.delete(0, tk.END)

def update():
    global updateSpeed, textbox, empty, displayed
    a=NewlyAdded()
    if a=={}:
        pass
    else:
        for i in a:
            DisplayMessage(i,a[i][0],a[i][1],a[i][2])
    empty.set("".join([" " for x in range(int(window.winfo_width()/4.01))]))    
    window.after(updateSpeed,update)

window.bind('<Return>',sendMessage)


empty=tk.StringVar()
empty.set("".join([" " for x in range(int(window.winfo_width()/4.01))]))


message0 = tk.Label(frame, textvariable=empty,bg='#36393f', fg=TEXT_COLOR, justify='right', font='Calibri 14')
message0.grid(row=1, column=0, columnspan=3, sticky=(tk.N,tk.W))
message0.columnconfigure(0,weight=1)
message0.rowconfigure(1,weight=1)


send = tk.Button(window, text="Send", font="Calibri 12 bold", bg="WHITE",command=sendMessage).grid(row=2, column=2, sticky=(tk.E))
textbox = tk.Entry(window, bg="#36393f", fg=TEXT_COLOR, font="Calibri 17")
textbox.grid(row=2, column=0, columnspan=2, sticky=(tk.E,tk.W))
textbox.columnconfigure(0,weight=1)

update()
window.mainloop()
