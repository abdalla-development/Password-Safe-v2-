from tkinter import *
from tkinter import messagebox
from Functions import connect_to_database
from Functions import email_validate, password_validate, mobile_validate, generate_password


class PasswordGenerationWindow:
    """Password Generation Window Class"""
    def __init__(self, title):
        """This Page Will Allow The User To Save His Data For The Intended Platform By Providing The Relevant Data And
        He Will Be Given The Choice Either TO Enter A Password That Must Pass The Validation Function Or To Enable
        Automatic Generation"""
        self.go_to = ""
        self.generated_password = ""
        # Defining Sqlite3 Connection
        connection, cursor = connect_to_database()

        self.generation = Tk()
        self.generation.title("Generation Page")
        self.generation.geometry("800x500")
        self.generation.config(bg="#395B64")
        ################################################################################################################
        """Images"""
        app_logo = PhotoImage(file='Images/shield.png')
        self.generation.tk.call('wm', 'iconphoto', self.generation._w, app_logo)
        ################################################################################################################
        """Messages"""
        generate_message = Label(text="Please Provide The Information Bellow", font=("Arial", 12, "normal"))
        generate_message.grid(row=1, column=1)
        ################################################################################################################
        """Inputs"""
        #  Platform
        platform_label = Label(text="Platform", font=("Arial", 12, "normal"))
        platform_label.grid(row=2, column=1)
        self.platform_generation_input = Entry(width=50)
        self.platform_generation_input.focus()
        self.platform_generation_input.grid(row=2, column=2)

        #  Username
        username_label = Label(text="Username", font=("Arial", 12, "normal"))
        username_label.grid(row=3, column=1)
        self.username_generation_input = Entry(width=50)
        self.username_generation_input.grid(row=3, column=2)

        # Email
        email_label = Label(text="Email", font=("Arial", 12, "normal"))
        email_label.grid(row=4, column=1)
        self.email_generation_input = Entry(width=50)
        self.email_generation_input.grid(row=4, column=2)

        # Mobile
        mobile_label = Label(text="Mobile", font=("Arial", 12, "normal"))
        mobile_label.grid(row=5, column=1)
        self.mobile_generation_input = Entry(width=50)
        self.mobile_generation_input.grid(row=5, column=2)

        # Password
        password_label = Label(text="Password", font=("Arial", 12, "normal"))
        password_label.grid(row=6, column=1)
        self.password_generation_input = Entry(width=50)
        self.password_generation_input.grid(row=6, column=2)
        ################################################################################################################
        """Buttons"""
        generate_password_button = Button(self.generation, text="Generate Password", command=self.generate_new_password)
        generate_password_button.grid(row=7, column=1)

        save_generated_password_button = Button(self.generation, text="Save Password",
                                                command=self.save_new_generated_password)
        save_generated_password_button.grid(row=7, column=2)

        back_to_options_button = Button(self.generation, text="Back", command=self.go_to_options_page)
        back_to_options_button.grid(row=7, column=3)

        log_out_button = Button(self.generation, text="Log Out", command=self.logout)
        log_out_button.grid(row=7, column=4)
        ################################################################################################################
        # Enter Key To Save New Data
        self.generation.bind("<Return>", self.save_new_generated_password)
        ################################################################################################################
        self.generation.mainloop()

    def save_new_generated_password(self, keypress=""):
        """This Function Will Save The New Generated Password"""
        # Getting Entered Data
        password_entered = self.password_generation_input.get()
        platform_entered = self.platform_generation_input.get().capitalize()
        username_entered = self.username_generation_input.get()
        mobile_entered = self.mobile_generation_input.get()
        email_entered = self.email_generation_input.get()

        # Validate Email
        email_is_valid = email_validate(email_entered)
        password_is_valid = password_validate(password_entered)
        mobile_is_valid = mobile_validate(mobile_entered)

        if password_entered == "":
            """Check If The Password Field Is Empty & The User Had Not Entered A Password Or Clicked On Generate 
            Button"""
            messagebox.showinfo("Error", "Please Either Enter A Password Or Press Generate Button To Proceed")
            self.password_generation_input.focus()

        elif platform_entered == "" or username_entered == "":
            """Check if Ihe Platform And Username Fields Are Provided"""
            messagebox.showinfo("Error", "Please Make Sure To Provide Both The Platform & The Username Fields")
            if platform_entered == "":
                self.platform_generation_input.focus()
            else:
                self.username_generation_input.focus()

        elif mobile_entered == "" and email_entered == "":
            """Check If Any Of Mobile, Email Fields Are Provided"""
            messagebox.showinfo("Error", "Please Provide Either The Mobile Number Or The Email You Registered With")
            if email_entered == "":
                """Check If The Email Field Is Empty But The Cursor On It"""
                self.email_generation_input.focus()
            else:
                """Check If The Mobile Field Is Empty But The Cursor On It"""
                self.mobile_generation_input.focus()

        elif not email_is_valid and email_entered != "":
            """Check If The Email Field Is Not Empty And Valid"""
            messagebox.showinfo("Error", "Please Provide A Valid Email")
            self.email_generation_input.focus()

        elif mobile_entered != "" and not mobile_is_valid:
            """Check If The Mobile Filed Is Not Empty And At Least Has The Length Of 10"""
            messagebox.showinfo("Error", "Please Provide A Valid Mobile Number")
            self.mobile_generation_input.focus()

        elif not password_is_valid and password_entered != self.generated_password:
            """Check The Entered Password Either It Is Automatically Generated By The Program Or It Is A Valid 
            Password"""
            messagebox.showinfo("Error", "The Password You Entered Is Not Valid")
            self.password_generation_input.focus()

        else:
            """If Everything Is Ok And All The Input Validations Had Passed, Then Proceed To Save The Data To The 
            Database File"""
            # Defining Sqlite3 Connection
            connection, cursor = connect_to_database()

            # Adding Data To User Safe Table
            params = (platform_entered, username_entered, email_entered, mobile_entered, password_entered)
            cursor.execute('INSERT INTO UserSafe VALUES(NULL,?,?,?,?,?)', params)
            connection.commit()
            messagebox.showinfo("info", "Congratulations The Data Had Been Successfully Saved To The Database")
            self.generation.destroy()
            self.go_to = "Options"
            return self.go_to

    def generate_new_password(self):
        """This Function Will Generate A New Password And Insert It In The Password Field"""
        self.generated_password = generate_password()
        self.password_generation_input.delete(0, END)
        self.password_generation_input.insert(0, self.generated_password)

    def go_to_options_page(self):
        """This Function Will Navigate The User Back To Option Page"""
        # Close Retrieve Saved Data Page
        self.generation.destroy()
        self.go_to = "Options"
        return self.go_to

    def logout(self):
        """This Function Will Log out The User & Bring Up The Login Page"""
        # Close Options Page
        self.generation.destroy()
        self.go_to = "Logout"
        return self.go_to
