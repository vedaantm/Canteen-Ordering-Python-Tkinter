from tkinter import *

def finalbill(orders):
    root=Tk()
    root.title("Canteen/Bill")
    root.geometry("500x500")

    Tops = Frame(root,width = 1600,height=50,relief=SUNKEN)
    Tops.pack()
    Frame1 = Frame(root,bg="white")
    Frame1.pack()
    
    billlabel = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Bill",bg="darkblue",fg="white",bd=10,anchor='w')
    billlabel.grid(row=0,column=0)

    Label(Frame1, text=f"┌{'─'*25}┬{'─'*4}┬{'─'*5}┐").pack()
    Label(Frame1, text=f"│{'Item Name'.center(25)}│{'Quantity'.center(4)}│{'Price'.center(5)}│").pack()
    Label(Frame1, text=f"├{'─'*25}┼{'─'*4}┼{'─'*5}│").pack()

    for name, order in orders.items():
        for item, (quan, price) in order[0].items():
            # order[0] = {"Samosa" : (2, 30), ..."}
            to_print = f"│{item.center(25)}│{str(quan).center(4)}│Rs.{str(price).center(5)}│"
            lb1=Label(Frame1,text=to_print)
            lb1.pack()

    Label(Frame1, text=f"└{'─'*25}┴{'─'*4}┴{'─'*5}┘").pack()

    root.mainloop()
