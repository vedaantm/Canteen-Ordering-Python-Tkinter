from tkinter import *
import tkinter as tk
from main import *
from tkinter import ttk, messagebox
import pymysql

def close():
	win.destroy()	

def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And password",parent=win)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="canteen")
			cur = con.cursor()

			cur.execute("select * from userdata where username=%s and password = %s",(user_name.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And password", parent = win)

			else:
				messagebox.showinfo("Success" , "Successfully Login" , parent = win)
				close()
				menu() #menu finction calling
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error : {str(es)}", parent = win)
#----------------------------------------------------------- Signup Window --------------------------------------------------
def signup():
	# signup database connect 
	def action():
		if first_name.get()=="" or last_name.get()=="" or age.get()=="" or sapid.get()=="" or campus.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != very_pass.get():
			messagebox.showerror("Error" , "password & Confirm password Should Be Same" , parent = winsignup)
		else:
			try:
				con = pymysql.connect(host="localhost",user="root",password="",database="canteen")
				cur = con.cursor()
				cur.execute("select * from userdata where username=%s",user_name.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exists", parent = winsignup)
				else:
					cur.execute("insert into userdata(first_name,last_name,username,password) values(%s,%s,%s,%s)",
						(
						first_name.get(),
						last_name.get(),
						user_name.get(),
						password.get()
						))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Registration Successful" , parent = winsignup)
					clear()
					switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error : {str(es)}", parent = winsignup)
		
	def switch():
		winsignup.destroy()

	# clear data fu
	def clear():
		first_name.delete(0,END)
		last_name.delete(0,END)
		age.delete(0,END)
		var.set("Male")
		sapid.delete(0,END)
		campus.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		very_pass.delete(0,END)

		
	winsignup = Tk()
	winsignup.title("Canteen/Sign-Up")
	winsignup.maxsize(width=500 ,  height=600)
	winsignup.minsize(width=500 ,  height=600)

	
	heading = Label(winsignup , text = "Signup" , font = 'Helvetica 20 bold underline')
	heading.place(x=200 , y=60)

	first_name = Label(winsignup, text= "First Name :" , font='Helvetica 10 underline')
	first_name.place(x=80,y=130)

	last_name = Label(winsignup, text= "Last Name :" , font='Helvetica 10 underline')
	last_name.place(x=80,y=160)

	age = Label(winsignup, text= "Age :" , font='Helvetica 10 underline')
	age.place(x=80,y=190)

	Gender = Label(winsignup, text= "Gender :" , font='Helvetica 10 underline')
	Gender.place(x=80,y=220)

	sapid = Label(winsignup, text= "SAP ID : " , font='Helvetica 10 underline')
	sapid.place(x=80,y=260)

	campus = Label(winsignup, text= "Campus :" , font='Helvetica 10 underline')
	campus.place(x=80,y=290)

	user_name = Label(winsignup, text= "User Name :" , font='Helvetica 10 underline')
	user_name.place(x=80,y=320)

	password = Label(winsignup, text= "Password :" , font='Helvetica 10 underline')
	password.place(x=80,y=350)

	very_pass = Label(winsignup, text= "Verify password:" , font='Helvetica 10 underline')
	very_pass.place(x=80,y=380)

	# Entry Box ------------------------------------------------------------------
	first_name = StringVar()
	last_name = StringVar()
	age = IntVar(winsignup, value='0')
	var= StringVar()
	sapid= StringVar()
	campus = StringVar()
	user_name = StringVar()
	password = StringVar()
	very_pass = StringVar()


	first_name = Entry(winsignup, width=40 , textvariable = first_name)
	first_name.place(x=200 , y=133)

	last_name = Entry(winsignup, width=40 , textvariable = last_name)
	last_name.place(x=200 , y=163)
	
	age = Entry(winsignup, width=40, textvariable=age)
	age.place(x=200 , y=193)
	
	Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
	Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)

	sapid = Entry(winsignup, width=40, textvariable = sapid)
	sapid.place(x=200 , y=263)
	
	campus = Entry(winsignup, width=40 , textvariable = campus)
	campus.place(x=200 , y=293)
	
	user_name = Entry(winsignup, width=40,textvariable = user_name)
	user_name.place(x=200 , y=323)
	
	password = Entry(winsignup, width=40, show="*", textvariable = password)
	password.place(x=200 , y=353)
	
	very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
	very_pass.place(x=200 , y=383)

	# button login and clear
	btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
	btn_signup.place(x=200, y=413)

	btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
	btn_login.place(x=280, y=413)

	sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
	sign_up_btn.place(x=350 , y =20)

	winsignup.mainloop()
#-----------------------------------------------------------End Singup Window--------------------------------------	

#------------------------------------------------------------ Login Window ----------------------------------------
win = Tk()
win.title("Canteen/Log-In")

# window size
win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)

#heading label
heading = Label(win , text = "Login" , font = 'Helvetica 20 bold underline')
heading.place(x=80 , y=50)

username = Label(win, text= "User Name :" , font='Helvetica 10 underline')
username.place(x=80,y=110)

userpass = Label(win, text= "password :" , font='Helvetica 10 underline')
userpass.place(x=80,y=150)

# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=110)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=150)

# login button
btn_login = Button(win, text = "Login" ,font='Helvetica 10 underline',command = login, relief=FLAT)
btn_login.place(x=200, y=190)

# signup button
sign_up_btn = Button(win , text="New User? Sign up!" , command = signup )
sign_up_btn.place(x=350 , y =450)
win.mainloop()
#-------------------------------------------------------------------------- End Login Window ------------------------