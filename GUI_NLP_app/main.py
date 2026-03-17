from http.client import responses
from tkinter import Button

from db_methods import Database
import tkinter

db1 = Database()

class Layout:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.root.resizable(width=True, height=True)
        self.root.title("RohitDudi")
        self.root.configure(background="blue")
        self.root.mainloop()

    def login(self):
        self.clear()
        top_title = Lable(self.root,text="NLP App")
        top_title.pack(pady=10)

        email_label = Label(self.root,text="Enter Email")
        email_label.pack(pady=10)

        email_entry = Entry(self.root, text="Enter Email")
        email_entry.pack(pady=10)

        password_label = Label(self.root, text="Enter Password")
        password_label.pack(pady=10)

        password_entry = Entry(self.root, text="Enter Password")
        password_entry.pack(pady=10)

        login_button = Button(self.root,text="Login",command=self.do_login(email,password))
        login_button.pack(pady=10)

    def signup(self):
        self.clear()
        top_title = Lable(self.root,text="NLP App")
        top_title.pack(pady=10)

        name_label = Label(self.root, text="Enter Name")
        name_label.pack(pady=10)

        name_entry = Entry(self.root, text="Enter Email")
        name_entry.pack(pady=10)

        email_label = Label(self.root,text="Enter Email")
        email_label.pack(pady=10)

        email_entry = Entry(self.root, text="Enter Email")
        email_entry.pack(pady=10)

        password_label = Label(self.root, text="Enter Password")
        password_label.pack(pady=10)

        password_entry = Entry(self.root, text="Enter Password")
        password_entry.pack(pady=10)

        signup_button = Button(self.root,text="Login",command=self.do_signup(name,email,password))
        signup_button.pack(pady=10)
    def clear(self):
        ui = self.pack_slaves()
        ui.destroy()


    async def do_login(self,email,password):
        response = await db1.search(email,password)
        if response == 200:
            home()
        elif response == 201:
            print("wrong password")
        elif response == 404:
            print("Email does not exist")


    async def do_signup(self, name, email, password):
           response = await db1.create(name, email, password)
           if  await response == 200:
               login()
           elif await response == 409:
               print("Email already exists")
           else:
               print("Error while creating user")

    def home(self):
        self.clear()


app1 = Layout()
