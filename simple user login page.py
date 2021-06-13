from tkinter import *
from tkinter import messagebox
import smtplib

global root
global root1

# _________________________________________________________________________________________________________________________________

##  METHODS


def Login_page():
    def Login():

        uname = e1.get()
        password = e2.get()

        if uname == "abcd" and password == "1234":
            messagebox.showinfo("Login", "Login Success")
        else:
            messagebox.showinfo("Login", "please enter valid username and password")

    def Forgotpassword():
        messagebox.showinfo(
            "Forgot Password",
            "Your registered Password has been sent to your registered Email-ID. Please check your Email.",
        )

        mail = "19MH1A0523@acoe.edu.in"

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("userlogin803@gmail.com", "abcd@1234")
        server.sendmail("userlogin803@gmail.com", mail, "hello")

        server.quit()

    def go_to_createaccount():
        root.destroy()
        create_new_account()

    # _______________________________________________________________________________________________________________________________

    # LOGIN PAGE MAIN WINDOW

    root = Tk()
    root.title("USER LOGIN ")
    width = root.winfo_screenwidth()

    height = root.winfo_screenheight()

    root.geometry("%dx%d" % (width, height))
    global e1
    global e2

    e1 = StringVar()
    e2 = StringVar()

    # labels

    Label(
        root,
        text="Login or Sign in",
        bg="blue",
        fg="black",
        font=("Times new Roman Bold", 20),
    ).place(x=550, y=50)
    Label(root, text="Username", fg="black", font=("Times new Roman", 10)).place(
        x=510, y=190
    )
    Label(root, text="Password", fg="black", font=("Times new Roman", 10)).place(
        x=510, y=220
    )

    # Entry

    num1 = Entry(root, width=20, textvariable=e1).place(x=650, y=190)
    num2 = Entry(root, width=20, show="*", textvariable=e2).place(x=650, y=220)

    # buttons

    LB = Button(
        root,
        text="Login",
        command=Login,
        bg="orange",
        fg="white",
        font=("Times new Roman", 12),
    ).place(x=625, y=270)
    Button(
        root,
        text="Forgot Password",
        command=Forgotpassword,
        font=("Times new Roman", 9),
        fg="white",
        bg="red",
    ).place(x=600, y=310)
    Button(
        root, text="create new account", command=go_to_createaccount, bg="grey"
    ).place(x=590, y=360)

    root.mainloop()


# _________________________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________________________

##  METHODS


def create_new_account():
    def create_account():

        user_name = name.get()
        pass_word = Password.get()
        confirm_password = confirmpass.get()
        user_mail = email.get()

        if (
            len(user_name) == 0
            or len(pass_word) == 0
            or len(confirm_password) == 0
            or len(user_mail) == 0
        ):
            messagebox.showinfo("Create account", "please enter your details")

        elif ("@gmail.com" not in user_mail) and ("@acoe.edu.in" not in user_mail):
            messagebox.showinfo("EMAIL ERROR", "Please enter a valid Email Address")
        elif len(user_name) < 5:
            messagebox.showinfo(
                "USER NAME", "Your username should contain atleast 5 characters"
            )
        elif len(pass_word) < 6:
            messagebox.showinfo(
                "PASSWORD", "Your password should contain atleast 6 characters"
            )
        elif pass_word != confirm_password:
            messagebox.showinfo(
                "confirm password", "passwords not matched, please re-enter password"
            )

        else:
            messagebox.showinfo(
                "create new account", "Your Account Created Successfully"
            )
            root1.destroy()
            Login_page()

    def go_to_login():

        root1.destroy()
        Login_page()

    # ________________________________________________________________________________________________________________________________
    #### CREATE NEW ACCOUNT MAIN WINDOW

    root1 = Tk()
    root1.title("create new account")

    # geometry
    width = root1.winfo_screenwidth()
    height = root1.winfo_screenheight()
    root1.geometry("%dx%d" % (width, height))

    name = StringVar()
    email = StringVar()
    Password = StringVar()
    confirmpass = StringVar()

    #  labels
    Label(
        root1,
        text="CREATE NEW ACCOUNT",
        bg="blue",
        fg="black",
        font=("Times new Roman Bold", 20),
    ).place(x=450, y=80)

    lablename = Label(
        root1, text="Enter your name", font=("Times new Roman", 10), fg="black"
    ).place(x=500, y=190)

    entryname = Entry(root1, textvariable=name).place(x=625, y=190)

    lablepass = Label(
        root1, text="password", font=("Times new Roman", 10), fg="black"
    ).place(x=500, y=230)

    entrypass = Entry(root1, show="*", textvariable=Password).place(x=625, y=230)

    lablecpass = Label(
        root1, text="confirm password", font=("Times new Roman", 10), fg="black"
    ).place(x=500, y=270)

    entrycpass = Entry(root1, show="*", textvariable=confirmpass).place(x=625, y=270)

    lableemail = Label(
        root1, text="Enter your mail", font=("Times new Roman", 10), fg="black"
    ).place(x=500, y=300)

    entryemail = Entry(root1, textvariable=email).place(x=625, y=300)

    # button

    Button(root1, text="Create Account", command=create_account, bg="blue").place(
        x=550, y=400
    )
    Button(
        root1, text="already have an account", command=go_to_login, bg="yellow"
    ).place(x=525, y=440)

    root1.mainloop()


create_new_account()
