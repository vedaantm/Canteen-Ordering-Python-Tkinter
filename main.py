from tkinter import*
from snacks import *
from beverages import *
from dessert import *
from PIL import Image, ImageTk
def menu():
    root = Tk()
    root.geometry("1000x700")
    root.title("College Canteen")

    IMAGE_PATH = "background.jpg"
    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1000,700)))
    lbl = Label(root, image=img)
    lbl.img = img  # Keep a reference in case this code put is in a function.
    lbl.place(relx=0.5, rely=0.5, anchor='center')

    Tops = Frame(root,bg="grey",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)
    
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Canteen",bg="darkblue",fg="white",bd=10)
    lblinfo.grid(row=0,column=0)

    f1 = Frame(root,bg="red",width = 900,height=700,relief=SUNKEN)
    f1.pack(side=TOP)

    btnSnacks=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="SNACKS", bg="yellow",command=snacksfunc)
    btnSnacks.grid(row=1, column=1)

    btnBeverages=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="BEVERAGES", bg="green",command=beveragesfunc)
    btnBeverages.grid(row=1, column=17)

    btnDessert=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="DESSERT", bg="red",command=dessertfunc)
    btnDessert.grid(row=1, column=18) 

    root.mainloop()