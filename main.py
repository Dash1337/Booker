from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
import tkinter
import pymysql
from tkinter import *

connector = Connector()

def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "winged-metric-403908:europe-central2:shoebook",
        "pymysql",
        user="root",
        password="shoebook",
        db="FEETBOOKER"
    )
    return conn

pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

booking=tkinter.Tk()
booking.title("Booking Menu")
booking.geometry("900x300+100+200")
booking.resizable(False,False)
booking.configure(bg="#777777")

def trybooking():
    try:
        nameD = nameins.get()
        dayD = click1.get()
        timeD = click2.get()
        sizeD = click3.get()

        amount_check = sqlalchemy.text(
            "select count(*) from bookers where feet = :feet"
        )
        limit_check = sqlalchemy.text(
            "select amount from storeroom where bootsize = :bootsize"
        )
        with pool.connect() as db_conn:
            limited = db_conn.execute(limit_check, parameters={"bootsize": sizeD}).fetchone()
            amounted = db_conn.execute(amount_check, parameters={"feet": sizeD}).fetchone()

        if amounted < limited:
            executebook.place(x=300, y=250)
            nameshow.config(text="" + nameD)
            timeshow.config(text="" + timeD)
            dayshow.config(text="" + dayD)
            sizeshow.config(text="" + sizeD)
        if amounted >= limited:
            executebook.place(x=3000, y=2500)
            nameshow.config(text="err")
            dayshow.config(text="err")
            timeshow.config(text="err")
            sizeshow.config(text="err")

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

    nameshow.config(text="")
    dayshow.config(text="")
    timeshow.config(text="")
    sizeshow.config(text="")

    nameins.delete(0, END)
    click1.set("Nap")
    click2.set("Idő")
    click3.set("Méret")
    executebook.place(x=3000, y=2500)

    try:
        insert_stmt = sqlalchemy.text(
            "INSERT INTO bookers (nev, datum, ido, feet) VALUES (:nev, :datum, :ido, :feet)",
        )

        with pool.connect() as db_conn:

            db_conn.execute(insert_stmt, parameters={"nev": nameD, "datum": dayD, "ido": timeD, "feet": sizeD})

            result = db_conn.execute(sqlalchemy.text("SELECT * from bookers")).fetchall()

            db_conn.commit()

            booking.mainloop()

    except ValueError:
        nameshow.config(text="err")
        dayshow.config(text="err")
        timeshow.config(text="err")
        sizeshow.config(text="err")

title= Label(booking,text="Online Cipőfoglalás",font=("arial",25),bg="#777777",fg="#000000")
title.place(x=0,y=20)

name= Label(booking,text="Név: ",font=("arial",0),bg="#777777",fg="#000000")
name.place(x=0,y=90)
nameshow= Label(booking,text=" ",font=("arial",0),bg="#777777",fg="#000000")
nameshow.place(x=600,y=90)
nameins = Entry(booking, width=20, font=("Arial",12),bg="#444444",fg="#fff")
nameins.place(x=90,y=90)

day= Label(booking,text="Időpont: ",font=("arial",0),bg="#777777",fg="#000000")
day.place(x=0,y=140)
dayshow= Label(booking,text=" ",font=("arial",0),bg="#777777",fg="#000000")
dayshow.place(x=600,y=140)
click1 = StringVar()
click1.set("Nap")
dayins = OptionMenu(booking, click1, "2023-12-10", "2023-12-11", "2023-12-12", "2023-12-13", "2023-12-14")
dayins.place(x=90,y=140)

timeshow= Label(booking,text=" ",font=("arial",0),bg="#777777",fg="#000000")
timeshow.place(x=700,y=140)
click2 = StringVar()
click2.set("Idő")
timeins = OptionMenu(booking, click2, "12:30", "15:30", "18:30")
timeins.place(x=200,y=140)

size= Label(booking,text="Méret: ",font=("arial",0),bg="#777777",fg="#000000")
size.place(x=0,y=190)
sizeshow= Label(booking,text=" ",font=("arial",0),bg="#777777",fg="#000000")
sizeshow.place(x=600,y=190)
click3 = StringVar()
click3.set("Méret")
sizeins = OptionMenu(booking, click3, "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45")
sizeins.place(x=90,y=190)

executeOrd = Button(booking, text="Foglalok", height=1, width=22,fg="#fff",bg="#535353", font=("arial",10),command=trybooking)
executeOrd.place(x=90,y=250)

executebook = Button(booking, text="Megerősítés", height=1, width=22, fg="#fff", bg="#ff0000",font=("arial", 10), command=executebooking)

booking.mainloop()
