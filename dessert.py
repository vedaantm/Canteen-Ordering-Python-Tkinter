from tkinter import *
from typing import NewType
from bill import *
global Button1, Button2, Button3, Button4, Button5, Button6, Button7, sum3, order3

def calc(order):
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, sum3, order3
    sum3 = 0
    order3 = {}
    prices = {Button1:("Blackforest Pastry", 40), Button2:("Red Velvet Pastry",50), Button3:("Chocolate Chip waffle",60), Button4:("Vanilla Ice cream",20), Button5:("Chocolate Ice cream",20), Button6:("Chocolate Brownie",20), Button7:("Blueberry Muffin",30)}
    for spinbox, details_tuple in prices.items():
        quantity = int(spinbox.get())
        price = quantity*details_tuple[1]
        sum3 += price
        if quantity > 0:
            order3[details_tuple[0]] = (quantity, price)
    order["dessert"] = (order3, sum3)
    finalbill(order)

def dessertfunc(order):
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, sum3, order3   
    newWindow = Tk()
    newWindow.title("Canteen/Dessert")
    newWindow.geometry("500x500")

    Tops = Frame(newWindow,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack()
    Frame1 = Frame(newWindow,bg="white")
    Frame1.pack()
    #-----------------INFO TOP------------
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Dessert",bg="darkblue",fg="white",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)

    for i in range(7):
        Frame1.rowconfigure(i, weight=1)

    for i in range(2):
        Frame1.columnconfigure(i, weight=1)

    w = Label(Frame1, text ='Blackforest Pastry -> ₹40', font = "50") 
    w.grid(row=0,column=0)
    Button1 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button1.grid(row=0,column=1,pady=10)

    w = Label(Frame1, text ='Red Velvet Pastry -> ₹50', font = "50") 
    w.grid(row=1,column=0)
    Button2 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button2.grid(row=1,column=1,pady=10)

    w = Label(Frame1, text ='Chocolate Chip waffle -> ₹60', font = "50") 
    w.grid(row=2,column=0)
    Button3 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button3.grid(row=2,column=1,pady=10)

    w = Label(Frame1, text ='Vanilla Ice Cream cone -> ₹20', font = "50") 
    w.grid(row=3,column=0)
    Button4 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button4.grid(row=3,column=1,pady=10)
    
    w = Label(Frame1, text ='Chocolate Ice Cream cone -> ₹20', font = "50") 
    w.grid(row=4,column=0)
    Button5 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button5.grid(row=4,column=1,pady=10)

    w = Label(Frame1, text ='Chocolate Brownie -> ₹20', font = "50") 
    w.grid(row=5,column=0)
    Button6 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button6.grid(row=5,column=1,pady=10)

    w = Label(Frame1, text ='Blueberry Muffin -> ₹30', font = "50") 
    w.grid(row=6,column=0)
    Button7 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button7.grid(row=6,column=1,pady=10)

    placeorder = Button(newWindow, text = "Place Order" ,font='Verdana 10 bold',command = lambda: calc(order), relief=SUNKEN)
    placeorder.place(x=200, y=450)

    newWindow.mainloop()