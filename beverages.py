from tkinter import *

from dessert import dessertfunc
global Button1, Button2, Button3, Button4, Button5, Button6, Button7, sum2, order2

def calc(order):
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, sum2, order2
    sum2 = 0
    order2 = {}
    prices = {Button1:("Tea", 15), Button2:("Coffee",15), Button3:("Diet Pepsi",25), Button4:("Red bull",95), Button5:("Chocolate Milkshake",50), Button6:("Iced Tea",30), Button7:("Cold Coffee",40)}
    for spinbox, details_tuple in prices.items():
        quantity = int(spinbox.get())
        price = quantity*details_tuple[1]
        sum2 += price
        if quantity > 0:
            order2[details_tuple[0]] = (quantity, price)
    order["beverages"] = (order2, sum2)
    dessertfunc(order)

def beveragesfunc(order):
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, sum2, order2    
    newWindow = Tk()
    newWindow.title("Canteen/Beverages")
    newWindow.geometry("500x500")

    Tops = Frame(newWindow,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack()
    Frame1 = Frame(newWindow,bg="white")
    Frame1.pack()
    #-----------------INFO TOP------------
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Beverages",bg="darkblue",fg="white",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)

    for i in range(7):
        Frame1.rowconfigure(i, weight=1)

    for i in range(2):
        Frame1.columnconfigure(i, weight=1)

    w = Label(Frame1, text ='Tea -> ₹15', font = "50")
    w.grid(row=0,column=0)
    Button1 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button1.grid(row=0,column=1,pady=10)

    w = Label(Frame1, text ='Coffee -> ₹15', font = "50")
    w.grid(row=1,column=0)
    Button2 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button2.grid(row=1,column=1,pady=10)

    w = Label(Frame1, text ='Diet Pepsi -> ₹25', font = "50")
    w.grid(row=2,column=0)
    Button3 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button3.grid(row=2,column=1,pady=10)
    
    w = Label(Frame1, text ='Red Bull -> ₹95', font = "50")
    w.grid(row=3,column=0)
    Button4 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button4.grid(row=3,column=1,pady=10)

    w = Label(Frame1, text ='Chocolate Milkshake -> ₹50', font = "50")
    w.grid(row=4,column=0)
    Button5 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button5.grid(row=4,column=1,pady=10)

    w = Label(Frame1, text ='Iced Tea -> ₹30', font = "50")
    w.grid(row=5,column=0)
    Button6 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button6.grid(row=5,column=1,pady=10)

    w = Label(Frame1, text ='Cold coffee -> ₹40', font = "50")
    w.grid(row=6,column=0)
    Button7 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button7.grid(row=6,column=1,pady=10)

    checkout = Button(newWindow, text = "Proceed to Dessert?" ,font='Verdana 10 bold',command = lambda: calc(order), relief=SUNKEN)
    checkout.place(x=200, y=450)

    newWindow.mainloop()