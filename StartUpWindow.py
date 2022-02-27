from tkinter import *
from tkinter import messagebox

import customtkinter

from Functions import password_validate, email_validate, mobile_validate, connect_to_database


class StartUpWindow:
    """Start Up Window Class"""
    def __init__(self, title):
        """This Page Will Allow The User To Initialize The Program For The First Time And Bring Up The Start Up Window
        For The User To Set up His Account Information"""

        """Define The General Used Variables Through The Class Functions"""
        self.go_to = ""
        self.first_name_label_create_account_input = ""
        self.last_name_create_account_input = ""
        self.username_create_account_input = ""
        self.email_create_account_input = ""
        self.mobile_create_account_input = ""
        self.password_1_create_account_input = ""
        self.password_2_create_account_input = ""
        self.register_email_is_valid = False
        self.register_mobile_is_valid = False
        ################################################################################################################
        """Initialize The Start Up Window"""
        self.window = Tk()
        self.window.title(f"{title}")
        self.window.geometry("800x650")
        self.window.config(bg="#395B64")
        ################################################################################################################
        """Images"""
        app_logo = PhotoImage(file='Images/shield.png')
        self.window.tk.call('wm', 'iconphoto', self.window._w, app_logo)

        canvas = Canvas(highlightthickness=0, bg="#395B64")
        safe_image = PhotoImage(file="Images/safe-lock.png")
        canvas.create_image(200, 110, image=safe_image)
        canvas.grid(column=0, row=0, pady=5)  # , padx=200 , rowspan=2
        ################################################################################################################
        """Messages"""
        self.window_message = Label(text="Welcome To Password Safe Generator\nPlease Fill The Information Bellow",
                                    font=("Arial", 12, "normal"),
                                    bg="#395B64")
        self.window_message.grid(row=0, column=1, columnspan=3)
        application_title = Label(text="Password Safe", font=("Arial", 16, "normal"), bg="#395B64")
        application_title.grid(row=2, column=0)
        ################################################################################################################
        """Inputs"""
        # First Name
        # self.first_name_label_create_account = Label(text="First Name", font=("Arial", 16, "normal"))
        # self.first_name_label_create_account.grid(row=3, column=1)
        self.first_name_label_create_account_input = Entry(width=50)
        self.first_name_label_create_account_input = customtkinter.CTkEntry(master=self.window, corner_radius=20,
                                                                            width=300, fg_color="#1A374D",
                                                                            placeholder_text="First Name",
                                                                            bg_color="#395B64")
        self.first_name_label_create_account_input.focus()
        # self.first_name_label_create_account_input.config(ipady=5)
        self.first_name_label_create_account_input.grid(row=1, column=2, pady=5)

        # Last Name
        # self.last_name_label_create_account = Label(text="Last Name", font=("Arial", 16, "normal"))
        # self.last_name_label_create_account.grid(row=4, column=1)
        # self.last_name_create_account_input = Entry(width=50)
        self.last_name_create_account_input = customtkinter.CTkEntry(master=self.window, corner_radius=20, width=300,
                                                                     fg_color="#1A374D", placeholder_text="Last Name",
                                                                     bg_color="#395B64")
        self.last_name_create_account_input.grid(row=2, column=2, pady=5, padx=5)

        #  Username
        # self.username_label_create_account = Label(text="Username", font=("Arial", 16, "normal"))
        # self.username_label_create_account.grid(row=5, column=1)
        # self.username_create_account_input = Entry(width=50)
        self.username_create_account_input = customtkinter.CTkEntry(master=self.window, corner_radius=20, width=300,
                                                                    fg_color="#1A374D", placeholder_text="Username",
                                                                    bg_color="#395B64")
        self.username_create_account_input.grid(row=3, column=2, pady=5)

        # Email
        # self.email_label_create_account = Label(text="Email", font=("Arial", 16, "normal"))
        # self.email_label_create_account.grid(row=6, column=1)
        # self.email_create_account_input = Entry(width=50)
        self.email_create_account_input = customtkinter.CTkEntry(master=self.window, corner_radius=20, width=300,
                                                                 fg_color="#1A374D", placeholder_text="Email",
                                                                 bg_color="#395B64")
        self.email_create_account_input.grid(row=4, column=2, pady=5)

        # Mobile Number
        # self.mobile_label_create_account = Label(text="Mobile Number", font=("Arial", 16, "normal"))
        # self.mobile_label_create_account.grid(row=7, column=1)
        self.mobile_label_info_create_account = Label(text="Optional", font=("Arial", 16, "normal"))
        self.mobile_label_info_create_account.config(bg="#395B64")
        self.mobile_label_info_create_account.grid(row=5, column=3, pady=5)
        # self.mobile_create_account_input = Entry(width=50)
        self.mobile_create_account_input = customtkinter.CTkEntry(master=self.window, corner_radius=20, width=300,
                                                                  fg_color="#1A374D", placeholder_text="Mobile Number",
                                                                  bg_color="#395B64")
        self.mobile_create_account_input.grid(row=5, column=2, pady=5)

        # Password 1
        # self.password_1_label_create_account = Label(text="Password", font=("Arial", 16, "normal"))
        # self.password_1_label_create_account.grid(row=8, column=1)
        # self.password_1_create_account_input = Entry(width=50, show="*")
        self.password_1_create_account_input = customtkinter.CTkEntry(master=self.window, corner_radius=20, width=300,
                                                                      fg_color="#1A374D", placeholder_text="Password",
                                                                      bg_color="#395B64", show="*")
        self.password_1_create_account_input.grid(row=6, column=2, pady=5)

        # Password 2
        # self.password_2_label_create_account = Label(text="Re-Enter Password", font=("Arial", 16, "normal"))
        # self.password_2_label_create_account.grid(row=9, column=1)
        # self.password_2_create_account_input = Entry(width=50, show="*")
        self.password_2_create_account_input = customtkinter.CTkEntry(master=self.window, corner_radius=20, width=300,
                                                                      fg_color="#1A374D", show="*",
                                                                      placeholder_text="Re-Enter Password",
                                                                      bg_color="#395B64")
        self.password_2_create_account_input.grid(row=7, column=2, pady=5)
        ################################################################################################################
        """Buttons"""
        # self.create_account_button = Button(self.window, text="Create Account", command=c)
        self.create_account_button = customtkinter.CTkButton(master=self.window,
                                                             text="Create Account", width=100, height=50,
                                                             corner_radius=10, compound="right",
                                                             command=self.create_new_account, bg_color="#395B64")
        self.create_account_button.grid(row=10, column=2, pady=5)
        ################################################################################################################
        """Enter Key To Create An Account"""
        self.window.bind("<Return>", self.create_new_account)
        ################################################################################################################
        self.window.mainloop()

    def create_new_account(self, keypress=""):
        """This Function Will Check First If It is The First Time To Run The Application And No User Is Set Up It will
            Initialize The User Data and Information"""

        # Getting The Entered Data
        first_name = self.first_name_label_create_account_input.get()
        last_name = self.last_name_create_account_input.get()
        username = self.username_create_account_input.get()
        email = self.email_create_account_input.get()
        mobile = self.mobile_create_account_input.get()
        password = self.password_1_create_account_input.get()
        password_2 = self.password_2_create_account_input.get()

        # Validate The Email, Mobile & Password
        register_email_is_valid = email_validate(email)
        register_mobile_is_valid = mobile_validate(mobile)
        password_is_valid = password_validate(password)

        if username == "" or first_name == "" or last_name == "" or email == "" or password == "" or password_2 == "":
            """Checking If The Two Passwords Entered Are Matched And All Required Fields Are Filled"""
            if first_name == "":
                """If The First Name Is Empty Put The Cursor on It"""
                messagebox.showinfo("Missing Information", "Please Provide The First Name Field")
                self.first_name_label_create_account_input.focus()
            elif last_name == "":
                """If The Last Name Is Empty Put The Cursor on It"""
                messagebox.showinfo("Missing Information", "Please Provide The Last Name Field")
                self.last_name_create_account_input.focus()
            elif username == "":
                """If The Username Is Empty Put The Cursor on It"""
                messagebox.showinfo("Missing Information", "Please Provide The Username Field")
                self.username_create_account_input.focus()
            elif password == "":
                """If The First Password Field Is Empty Put The Cursor on It"""
                messagebox.showinfo("Missing Information", "Please Provide A Password Field")
                self.password_1_create_account_input.focus()
            elif password_2 == "":
                """If The Second Password Field Is Empty Put The Cursor on It"""
                messagebox.showinfo("Missing Information", "Please Re-Enter Password Field")
                self.password_2_create_account_input.focus()
        elif not register_email_is_valid:
            """Check If The Entered Email Validation Return & If It Is Not A Valid Email Address Display A Message To 
            The User To Provide A Valid Email Address"""
            messagebox.showinfo("Error", "Please Enter A Valid Email")
            self.email_create_account_input.focus()
        elif len(mobile) != 0 and not register_mobile_is_valid:
            """Regarding To The Mobile Number Field Is Optional If The user Provided A Number And It Was Not Valid 
            Mobile Number Display A Message To Provide A Valid Number"""
            messagebox.showinfo("Error", "Please Enter A Valid Mobile Number ")
        elif password != password_2:
            """If The Password First And Second Field Do Not Match Display A Message To The User To Provide The Same 
            Value For Both Fields"""
            messagebox.showinfo("Error", "The Passwords You Entered Don't Match")
        elif password == password_2 and password_is_valid:
            """If Everything Is Ok So Far And The Entered Password Has Passed The Validation Function, Only Then Proceed
             With The Account Creation"""
            # Defining Sqlite3 Connection
            connection, cursor = connect_to_database()

            # Creating Tables
            user_information = """CREATE TABLE IF NOT EXISTS
                    UserInformation(User_ID INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, Username TEXT, Email 
                    TEXT, Mobile TEXT, Password TEXT)"""
            cursor.execute(user_information)
            user_safe = """CREATE TABLE IF NOT EXISTS
                    UserSafe(Safe_ID INTEGER PRIMARY KEY, Platform TEXT, Username TEXT, Email TEXT, Mobile TEXT,
                     Password TEXT)"""
            cursor.execute(user_safe)

            # Adding Data To User Information Table
            params = (first_name, last_name, username, email, mobile, password)
            cursor.execute('INSERT INTO UserInformation VALUES(NULL,?,?,?,?,?,?)', params)
            connection.commit()

            # Close Start Up Page
            self.window.destroy()
            self.go_to = "Login"

            return self.go_to

        elif not password_is_valid:
            """If The Entered Password Does Not Pass The Validation Function 
            (min 8 characters length, min 1 numeric, min 1 lowercase, min 1 uppercase, min 1 special character), Display
             A Message To User To Follow The Password Requirement Or Enable The Program To Suggest One"""
            messagebox.showinfo("Error", "Your Passwords Must Be\n➤ Min 8 Characters Length\n➤ Min 1 Numeric\n➤ Min 1 "
                                         "Lowercase\n➤ Min 1 Uppercase\n➤ Min 1 Special Character")






