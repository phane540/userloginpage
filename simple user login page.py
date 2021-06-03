from tkinter import *
from tkinter import messagebox


#methods
def Login():
    e1=StringVar()
    e2=StringVar()
    uname=e1.get()
    password=e2.get()

      

    if (uname=='abcd' and password=='12345'):
        
        messagebox.showinfo('','Login success')
    
    else:
        messagebox.showinfo('','please enter valid username and password')

def Forgotpassword():
     messagebox.showinfo('forgot password','your password is :12345')




#LOGIN PAGE

root=Tk()
root.title("USER LOGIN ")
root.geometry('600x300')


global e1
global e2


#labels
bg=PhotoImage( file="F:/Sample-png-image-1mb1.png")

label_image=Label(root,image=bg)
label_image.pack()

Label(root,text='login or signup',bg='white',fg='black',font=("Times new Roman",20)).place(x=210,y=10)
Label(root,text='username or email',fg='black',font=('',10)).place(x=240,y=90)
Label(root,text='password',fg='black',font=('',10)).place(x=240,y=150)

e1=Entry(root,width=20).place(x=240,y=120)
e2=Entry(root,width=20)
e2.place(x=240,y=180)
e2.config(show="*")


#buttons

Button(root,text='Login', command =Login,bg='orange',fg='white',font=("Times new Roman",12)).place(x=270,y=200)


    
Button(root,text='Forgot Password',command=Forgotpassword,font=("Times new Roman",9),fg='white',bg='red').place(x=245,y=240)
    

   
root.mainloop()
