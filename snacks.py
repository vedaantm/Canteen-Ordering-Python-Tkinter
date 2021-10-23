from tkinter import *
from beverages import beveragesfunc
global Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, sum1, order1

def calc():
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, sum1, order1
    sum1 = 0
    order = {}
    order1 = {}
    prices = {Button1:("Samosa", 15), Button2:("Vadapav",20), Button3:("Toast Sandwich",50), Button4:("Cheese Sandwich",30), Button5:("Steam Momos",60), Button6:("Fried Momos",70), Button7:("Pav Bhaji",100), Button8:("Maggi",40)}
    for spinbox, details_tuple in prices.items():
        quantity = int(spinbox.get())
        price = quantity*details_tuple[1]
        sum1 += price
        if quantity > 0:
            order1[details_tuple[0]] = (quantity, price)
    order["Snacks"] = (order1, sum1)
    beveragesfunc(order)
    
def snacksfunc():
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, sum1, order1
    newWindow = Tk()
    newWindow.title("Canteen/Snacks")
    newWindow.geometry("500x500")

    Tops = Frame(newWindow,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack()
    Frame1 = Frame(newWindow,bg="white")
    Frame1.pack()
    
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Snacks",bg="darkblue",fg="white",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)

    for i in range(8):
        Frame1.rowconfigure(i, weight=1)

    for i in range(2):
        Frame1.columnconfigure(i, weight=1)
    
    w = Label(Frame1, text ='Samosa -> ₹15', font = "50")
    w.grid(row=0,column=0)
    Button1 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button1.grid(row=0,column=1,pady=10)

    w = Label(Frame1, text ='Vada-pav -> ₹20', font = "50") 
    w.grid(row=1,column=0)
    Button2 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button2.grid(row=1,column=1,pady=10)

    w = Label(Frame1, text ='Toast Sandwich -> ₹50', font = "50") 
    w.grid(row=2,column=0)
    Button3 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button3.grid(row=2,column=1,pady=10)

    w = Label(Frame1, text ='Cheese Sandwich -> ₹30', font = "50") 
    w.grid(row=3,column=0)
    Button4 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button4.grid(row=3,column=1,pady=10)
    
    w = Label(Frame1, text ='Steam Momos(6 pcs) -> ₹60 ', font = "50") 
    w.grid(row=4,column=0)
    Button5 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button5 .grid(row=4,column=1,pady=10)

    w = Label(Frame1, text ='Fried Momos(6 pcs) -> ₹70', font = "50") 
    w.grid(row=5,column=0)
    Button6 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button6.grid(row=5,column=1,pady=10)

    w = Label(Frame1, text ='Pav Bhaji -> ₹100', font = "50") 
    w.grid(row=6,column=0)
    Button7 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button7.grid(row=6,column=1,pady=10)

    w = Label(Frame1, text ='Maggi -> ₹40', font = "50") 
    w.grid(row=7,column=0)
    Button8 = Spinbox(Frame1,
                    from_ = 0,
                    to = 20,
                    state="readonly",
                    wrap=True)
    Button8.grid(row=7,column=1,pady=10)

    # placeorder = Button(newWindow, text = "Place Order" ,font='Verdana 10 bold',command = calc, relief=SUNKEN)
    # placeorder.place(x=200, y=450)

    checkout = Button(newWindow, text = "Proceed to beverages?" ,font='Verdana 10 bold',command = calc, relief=SUNKEN)
    checkout.place(x=200, y=450)
        
    newWindow.mainloop()