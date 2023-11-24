import tkinter
from tkinter import *
import mysql.connector

with open("variables.txt", "r") as file:
    variables = file.read().split()
hostogo, usertogo, passwtogo, basetogo = variables

print("Received variables:", hostogo, usertogo, passwtogo, basetogo)

db = mysql.connector.connect(
    host=hostogo,
    user=usertogo,
    passwd=passwtogo,
    database=basetogo
)

kurzor = db.cursor()

booking=tkinter.Tk()
booking.title("Booking Menu")
booking.geometry("500x350")
booking.resizable(False,False)
booking.configure(bg="#777777")

def trybooking():
    try:
        nameD = nameins.get()
        dayD = click1.get()
        timeD = click2.get()
        sizeD = click3.get()

        namecheck = """select name from storeroom where name = %s""" % (nameD)
        limit = """select amount from storeroom where bootsize = %s""" % (sizeD)
        kurzor.execute(limit)
        limitRes = kurzor.fetchone()
        amount = """select count(*) from bookers where feet = '%s' and datum = '%s' and ido = '%s'""" % (sizeD, dayD, timeD)
        kurzor.execute(amount)
        amountRes = kurzor.fetchone()

        if amountRes < limitRes:
            executebook.place(x=300, y=250)
            nameshow.config(text="" + nameD)
            timeshow.config(text="" + timeD)
            dayshow.config(text="" + dayD)
            sizeshow.config(text="" + sizeD)
            notify.config(text="Kérem ellenőrizze a megadott adatokat!" , fg="#aa0000")
        else:
            executebook.place(x=3000, y=2500)
            nameshow.config(text="err")
            dayshow.config(text="err")
            timeshow.config(text="err")
            sizeshow.config(text="err")
            notify.config(text="A megadott méret az adott időpontban nem elérhető!", fg="#aa0000")

    except ValueError:
        nameshow.config(text="err")
        dayshow.config(text="err")
        timeshow.config(text="err")
        sizeshow.config(text="err")

def executebooking():
    nameD = nameins.get()
    dayD = click1.get()
    timeD = click2.get()
    sizeD = click3.get()

    nameins.delete(0, END)
    click1.set("Nap")
    click2.set("Idő")
    click3.set("Méret")
    executebook.place(x=3000, y=2500)

    nameshow.config(text="")
    dayshow.config(text="")
    timeshow.config(text="")
    sizeshow.config(text="")
    notify.config(text="Sikeres Foglalás!", fg="#00ff00")

    try:
        kurzor.execute("INSERT INTO bookers VALUES (%s, %s, %s, %s)", (nameD, dayD, timeD, sizeD))
        db.commit()

    except ValueError:
        nameshow.config(text="err")
        dayshow.config(text="err")
        timeshow.config(text="err")
        sizeshow.config(text="err")

title= Label(booking,text="Cipőfoglalás",font=("arial",40),bg="#777777",fg="#000000")
title.place(x=20,y=10)

name= Label(booking,text="Név: ",font=("arial",0),bg="#777777",fg="#000000")
name.place(x=0,y=90)
nameshow= Label(booking,text=" ",font=("arial",0),bg="#777777",fg="#000000")
nameshow.place(x=300,y=90)
nameins = Entry(booking, width=20, font=("Arial",12),bg="#444444",fg="#fff")
nameins.place(x=90,y=90)

day= Label(booking,text="Időpont: ",font=("arial",0),bg="#777777",fg="#000000")
day.place(x=0,y=140)
dayshow= Label(booking,text=" ",font=("arial",0),bg="#777777",fg="#000000")
dayshow.place(x=300,y=140)
click1 = StringVar()
click1.set("Nap")
dayins = OptionMenu(booking, click1, "2023-12-10", "2023-12-11", "2023-12-12", "2023-12-13", "2023-12-14")
dayins.place(x=90,y=140)

timeshow= Label(booking,text=" ",font=("arial",0),bg="#777777",fg="#000000")
timeshow.place(x=400,y=140)
click2 = StringVar()
click2.set("Idő")
timeins = OptionMenu(booking, click2, "12:30", "15:30", "18:30")
timeins.place(x=200,y=140)

size= Label(booking,text="Méret: ",font=("arial",0),bg="#777777",fg="#000000")
size.place(x=0,y=190)
sizeshow= Label(booking,text=" ",font=("arial",0),bg="#777777",fg="#000000")
sizeshow.place(x=300,y=190)
click3 = StringVar()
click3.set("Méret")
sizeins = OptionMenu(booking, click3, "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45")
sizeins.place(x=90,y=190)

executeOrd = Button(booking, text="Foglalok", height=1, width=22,fg="#fff",bg="#535353", font=("arial",10),command=trybooking)
executeOrd.place(x=90,y=250)

executebook = Button(booking, text="Megerősítés", height=1, width=22, fg="#fff", bg="#ff0000",font=("arial", 10), command=executebooking)

notify = Label(booking,text="",font=("arial",13),bg="#777777",fg="#aa0000")
notify.place(x=50,y=310)

booking.mainloop()
