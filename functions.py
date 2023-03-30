import mysql.connector
con=mysql.connector.connect(host="152.67.5.116", user="chat", password="sql123", database="info")
cur=con.cursor()
def getName(token):
    cur.execute("select username from users where token='"+token+"'")
    output=[x[0] for x in cur]
    return output[0]

def isAlphaNumeric(string):
    output=True
    for i in string.lower():
        if i in list("qwertyuiopasdfghjklzxcvbnm0123456789_"):
            pass
        else:
            output=False
            break
    return output

def getToken(name):
    cur.execute("select token from users where username='"+name+"'")
    output=[x[0] for x in cur]
    return output[0]