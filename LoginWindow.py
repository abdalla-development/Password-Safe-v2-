from tkinter import *
from tkinter import messagebox

import customtkinter

from Functions import connect_to_database
from PIL import Image, ImageTk


class Login:
    """Options Window Class"""
    def __init__(self, title):
        """This Page Will Allow The User To Login By Entering His Credentials"""

        """Define The General Used Variables Through The Class Functions"""
        self.goto = ""
        self.username_login_input = ""
        self.password_login_input = ""
        self.WIDTH = "800"
        self.HEIGHT = "500"
        ################################################################################################################
        """Initialize The Login Window"""
        self.login = Tk()
        self.login.title(f"{title}")
        self.login.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.login.config(bg="#1E849A")
        ################################################################################################################
        """Images"""
        app_logo = PhotoImage(file='Images/shield.png')
        self.login.tk.call('wm', 'iconphoto', self.login._w, app_logo)

        canvas = Canvas(highlightthickness=0, bg="#1E849A")
        safe_image = PhotoImage(file="Images/safe-lock.png")
        canvas.create_image(100, 55, image=safe_image)
        canvas.grid(column=0, row=0)

        login_image_icon = ImageTk.PhotoImage(
            Image.open("Buttons_Icon_Image/Account-Login-Button-PNG-Picture.png").resize((30, 30)))
        forget_my_password_image_icon = ImageTk.PhotoImage(Image.open("Buttons_Icon_Image/bell.png").resize((30, 30)))

        ################################################################################################################
        """Messages"""
        self.login_message = Label(text="Login Into Your Account", font=("Arial", 12, "normal"), bg="#1E849A")
        self.login_message.grid(row=0, column=1)
        ################################################################################################################
        """Inputs"""
        #  Username
        username_label_login = Label(text="Password Safe", font=("Arial", 16, "normal"), bg="#1E849A")
        # username_label_login = customtkinter.CTkLabel(master=self.login, corner_radius=6, width=200, height=40,
        #                                               fg_color=("gray70", "gray20"), text="Username")
        username_label_login.grid(row=3, column=0)
        # self.username_login_input = Entry(width=50)
        self.username_login_input = customtkinter.CTkEntry(master=self.login, corner_radius=20, width=300,
                                                           fg_color="#1A374D", placeholder_text="Username",
                                                           bg_color="#1E849A")
        self.username_login_input.focus()
        self.username_login_input.grid(row=1, column=1, columnspan=2, pady=5)

        # Password
        # self.password_label_login = Label(text="Password", font=("Arial", 16, "normal"))
        # self.password_label_login = customtkinter.CTkLabel(master=self.login, corner_radius=6, width=200, height=40,
        #                                                    fg_color=("gray70", "gray20"), text="Password")
        # self.password_label_login.grid(row=3, column=0)
        # self.password_login_input = Entry(width=50, show="*")
        self.password_login_input = customtkinter.CTkEntry(master=self.login, corner_radius=20, width=300,
                                                           fg_color="#1A374D", placeholder_text="Password", show="*",
                                                           bg_color="#1E849A")
        self.password_login_input.grid(row=2, column=1, columnspan=2, pady=5)
        ################################################################################################################
        """Buttons"""
        # login_button = Button(self.login, text="Login", command=self.login_to_my_account) , image=login_image_icon
        login_button = customtkinter.CTkButton(master=self.login, text="Login", width=100,
                                               height=50, corner_radius=10, compound="right",
                                               command=self.login_to_my_account, bg_color="#1E849A")
        login_button.grid(row=3, column=1, pady=5)

        # forget_password_button = Button(self.login, text="Forget Password", command=self.forget_my_password)
        forget_password_button = customtkinter.CTkButton(master=self.login, text="Forget Password", width=100,
                                                         height=50, corner_radius=10, compound="right",
                                                         command=self.forget_my_password, fg_color="orange",
                                                         bg_color="#1E849A")
        forget_password_button.grid(row=3, column=2, pady=5)
        ################################################################################################################
        """Enter Key To Login"""
        self.login.bind("<Return>", self.login_to_my_account)
        ################################################################################################################
        self.login.mainloop()

    def login_to_my_account(self, keypress=""):
        """This Function Will Check The Username And Password And if There Is A Match It Will Grant The User Access To
        The Data And Information"""
        # Defining Sqlite3 Connection
        connection, cursor = connect_to_database()

        # Getting Entered Data
        username_entered_login = self.username_login_input.get()
        password_entered_login = self.password_login_input.get()

        # Getting the username and password from the database
        cursor.execute('SELECT Username FROM UserInformation')
        username_saved_db = cursor.fetchall()[0][0]
        cursor.execute('SELECT Password FROM UserInformation')
        password_saved_db = cursor.fetchall()[0][0]

        if username_entered_login == username_saved_db and password_entered_login == password_saved_db:
            """Check If The User Credentials Entered Match With The Credential Saved In The Database"""
            # Close Login Page
            self.login.destroy()
            self.goto = "Options"
            return self.goto

        elif username_entered_login == "" or password_entered_login == "":
            """Check If The Username Field Or The Password Field Are Empty Display A Message To The User To Alert Him 
            To Provide Both Fields"""
            messagebox.showinfo("Error", "You Have To Enter Your Username And Password In Order To Login")
            if username_entered_login == "":
                """If The Username Field Is Empty Put The Cursor On It"""
                self.username_login_input.focus()
            else:
                """Else If The Password Field Is Empty Put The Cursor On It"""
                self.password_login_input.focus()
        else:
            """If The Username Or Password Is Not Correct Display A Message To The User To Notify Him That He Had 
            Entered Wrong Data"""
            messagebox.showinfo("Error", "The Credentials You Entered Don't Match With Our Database")

    def forget_my_password(self):
        """This Function Will Close The Login & Navigate The User To Forget Page"""
        self.login.destroy()
        self.goto = "Forget My Password"
        return self.goto
