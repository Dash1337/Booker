import tkinter
import subprocess
from tkinter import *
import mysql.connector

def csomag_install():
    try:
        subprocess.run(["pip", "install", "mysql-connector-python"])

        infolabel.config(text="A csomag már telepítve", fg="green")
        import mysql.connector

    except Exception as e:
        infolabel.config(text=f"Error: {e}", fg="red")

def checkuser():

    hostV = hostins.get()
    userV = userins.get()
    passwV = passwins.get()
    baseV = baseins.get()

    try:
        db = mysql.connector.connect(
            host=hostV,
            user=userV,
            passwd=passwV,
            database=baseV
        )
        if db.is_connected():
            login.config(state=NORMAL)
            connectlabel.config(text="Sikeres Csatlakozás", fg="green")
        else:
            connectlabel.config(text="Sikertelen Csatlakozás", fg="red")
    except mysql.connector.Error as err:
        connectlabel.config(text="Sikertelen Csatlakozás", fg="#ff0000")


def launch_script():
    with open("variables.txt", "w") as file:
        file.write(f"{hostins.get()} {userins.get()} {passwins.get()} {baseins.get()}")

    subprocess.Popen(["python", "main.py"])
    menu.after(5000, menu.destroy())

menu=tkinter.Tk()
menu.title("Bejelentkezés")
menu.geometry("350x350")
menu.resizable(False,False)
menu.configure(bg="#777777")

welcometext = Label(menu,text="Foglalórendszer ",font=("arial",20),bg="#777777",fg="#000000")
welcometext.place(x=0,y=5)

# Hostnév vagy IP-cím
host= Label(menu,text="Host: ",font=("arial",0),bg="#777777",fg="#000000")
host.place(x=0,y=60)
hostins = Entry(menu, width=20, font=("Arial",12),bg="#444444",fg="#fff")
hostins.place(x=100,y=60)

# Felhasználónév
user= Label(menu,text="Felhasználó: ",font=("arial",0),bg="#777777",fg="#000000")
user.place(x=0,y=100)
userins = Entry(menu, width=20, font=("Arial",12),bg="#444444",fg="#fff")
userins.place(x=100,y=100)

# Jelszó
passw= Label(menu,text="Jelszó: ",font=("arial",0),bg="#777777",fg="#000000")
passw.place(x=0,y=140)
passwins = Entry(menu, width=20,show="*", font=("Arial",12),bg="#444444",fg="#fff")
passwins.place(x=100,y=140)

# Adatbázisnév
base= Label(menu,text="Adatbázis: ",font=("arial",0),bg="#777777",fg="#000000")
base.place(x=0,y=180)
baseins = Entry(menu, width=20, font=("Arial",12),bg="#444444",fg="#fff")
baseins.place(x=100,y=180)

infolabel= Label(menu,text=" ",font=("arial",0),bg="#777777",fg="#000000")
infolabel.place(x=120,y=230)

connectchk = Button(menu, text="Ellenőrzés", command=checkuser)
connectchk.place(x=10,y=270)

login = Button(menu, text="Bejelentkezés", state=DISABLED, command=launch_script)
login.place(x=200,y=270)

packcheck = Button(menu, text="Csomag Telepítés:", command=csomag_install)
packcheck.place(x=10,y=230)

connectlabel= Label(menu,text="",font=("arial",10),bg="#777777",fg="#000000")
connectlabel.place(x=120,y=230)

infolabel= Label(menu,text="Kérem telepítse a MySQL csomagot a gomb használatával",font=("arial",10),bg="#777777",fg="#000000")
infolabel.place(x=0,y=300)

menu.mainloop()
