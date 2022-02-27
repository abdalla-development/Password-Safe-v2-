import functools
from tkinter import *
from tkinter import messagebox
from Functions import connect_to_database, password_validate, generate_password, email_validate, mobile_validate


class UpdatePlatformData:
    """Password Generation Window Class"""
    def __init__(self, title, platform_index):
        """This Page Will Allow The User To Save His Data For The Intended Platform By Providing The Relevant Data And
        He Will Be Given The Choice Either TO Enter A Password That Must Pass The Validation Function Or To Enable
        Automatic Generation"""
        self.status = ""
        self.goto = ""
        self.generated_password = ""
        self.platform_id = platform_index

        self.update_platform_data = Tk()
        self.update_platform_data.title(f"{title}")
        self.update_platform_data.geometry("800x500")
        self.update_platform_data.config(bg="#395B64")
        ################################################################################################################
        """Images"""
        app_logo = PhotoImage(file='Images/shield.png')
        self.update_platform_data.tk.call('wm', 'iconphoto', self.update_platform_data._w, app_logo)
        canvas = Canvas(highlightthickness=0)
        safe_image = PhotoImage(file="Images/safe-lock.png")
        canvas.create_image(237, 150, image=safe_image)
        canvas.grid(column=1, row=0, columnspan=3)
        ################################################################################################################
        """Messages"""
        welcome_message_1 = Label(text="Enter The Information You Want To Change", font=("Arial", 12, "normal"))
        welcome_message_1.grid(row=1, column=1)
        welcome_message_2 = Label(text="Please Provide The Information Below", font=("Arial", 12, "normal"))
        welcome_message_2.grid(row=2, column=1)
        ################################################################################################################
        """Inputs"""
        buttons = []

        # Defining Sqlite3 Connection
        connection, cursor = connect_to_database()

        # Getting the username and password from the database
        cursor.execute('SELECT * FROM UserSafe')
        saved_platforms_db = cursor.fetchall()

        # Getting The Platform Data
        platform_name = saved_platforms_db[platform_index][1]
        platform_username = saved_platforms_db[platform_index][2]
        platform_email = saved_platforms_db[platform_index][3]
        platform_mobile = saved_platforms_db[platform_index][4]
        platform_password = saved_platforms_db[platform_index][5]

        #  Platform
        platform_label = Label(text="Platform", font=("Arial", 12, "normal"))
        platform_label.grid(row=2, column=1)
        self.platform_update_input = Entry(width=50)
        self.platform_update_input.insert(END, f'{platform_name}')
        self.platform_update_input.focus()
        self.platform_update_input.grid(row=2, column=2)

        #  Username
        username_label = Label(text="Username", font=("Arial", 12, "normal"))
        username_label.grid(row=3, column=1)
        self.username_update_input = Entry(width=50)
        self.username_update_input.insert(END, f'{platform_username}')
        self.username_update_input.grid(row=3, column=2)

        # Email
        email_label = Label(text="Email", font=("Arial", 12, "normal"))
        email_label.grid(row=4, column=1)
        self.email_update_input = Entry(width=50)
        self.email_update_input.insert(END, f'{platform_email}')
        self.email_update_input.grid(row=4, column=2)

        # Mobile
        mobile_label = Label(text="Mobile", font=("Arial", 12, "normal"))
        mobile_label.grid(row=5, column=1)
        self.mobile_update_input = Entry(width=50)
        self.mobile_update_input.insert(END, f'{platform_mobile}')
        self.mobile_update_input.grid(row=5, column=2)

        # Password
        password_label = Label(text="Password", font=("Arial", 12, "normal"))
        password_label.grid(row=6, column=1)
        self.password_update_input = Entry(width=50)
        self.password_update_input.insert(END, f'{platform_password}')
        self.password_update_input.grid(row=6, column=2)
        ################################################################################################################
        """Buttons"""
        update_generate_new_button = Button(self.update_platform_data, text="Generate New",
                                            command=self.generate_new_password)
        update_generate_new_button.grid(row=6, column=3)

        update_platform_data_button = Button(self.update_platform_data, text="Update Data",
                                             command=self.update_platform_data_confirm)
        update_platform_data_button.grid(row=7, column=1)

        update_platform_data_cancel_button = Button(self.update_platform_data, text="Cancel",
                                                    command=self.back_to_options_page)
        update_platform_data_cancel_button.grid(row=7, column=2)
        ################################################################################################################
        """Enter Key To Save New Data"""
        self.update_platform_data.bind("<Return>", self.update_platform_data_confirm)
        ################################################################################################################
        self.update_platform_data.mainloop()

    def generate_new_password(self):
        """This Function Will Generate A New Password And Insert It In The Password Field"""
        self.generated_password = generate_password()
        self.password_update_input.delete(0, END)
        self.password_update_input.insert(0, self.generated_password)

    def update_platform_data_confirm(self):
        """This Function Will Eventually Save The New User Platform Data If It Passes The Validation"""
        # Defining Sqlite3 Connection
        connection, cursor = connect_to_database()

        # Getting The Data
        new_updated_platform_name = self.platform_update_input.get()
        new_updated_platform_username = self.username_update_input.get()
        new_updated_platform_email = self.email_update_input.get()
        new_updated_platform_mobile = self.mobile_update_input.get()
        new_updated_platform_password = self.password_update_input.get()

        # Validate Entered Password, Mobile & Email
        password_is_valid = password_validate(new_updated_platform_password)
        updated_email_is_valid = email_validate(new_updated_platform_email)
        mobile_is_valid = mobile_validate(new_updated_platform_mobile)

        if new_updated_platform_name == "":
            """Check If The Platform Name Field Is Empty Notify The User To Fill It"""
            messagebox.showinfo("Error", "You Can't Leave Platform Name Empty")

        elif new_updated_platform_username == "":
            """Check If The Username Field Is Empty Notify The User To Fill It"""
            messagebox.showinfo("Error", "You Can't Leave Username Empty")

        elif not password_is_valid or new_updated_platform_password != self.generated_password:
            """Check If The Entered Password Either Valid Or It Is Automatically Generated By The Program"""
            messagebox.showinfo("Error", "Your Passwords Must Be\n➤ Min 8 Characters Length\n➤ Min 1 Numeric\n➤ Min 1 "
                                         "Lowercase\n➤ Min 1 Uppercase\n➤ Min 1 Special Character\n\n Or You Can Hit "
                                         "Generate Button")

        elif not updated_email_is_valid:
            """Check If The Email Field Is Empty Notify The User To Fill It"""
            messagebox.showinfo("Error", "Please Provide A Valid Email")

        elif not mobile_is_valid and new_updated_platform_mobile != "":
            """Check If The Mobile Field Is Empty Notify The User To Fill It"""
            messagebox.showinfo("Error", "Please Provide A Valid Mobile Number")

        else:
            """Update The Platform Data If Everything is Ok And Had Passed The Validation"""

            # Platform Name
            sql_update_query = """UPDATE UserSafe SET Platform = ? WHERE Safe_ID = ?"""
            data = (new_updated_platform_name, self.platform_id)
            cursor.execute(sql_update_query, data)

            # Username
            sql_update_query = """UPDATE UserSafe SET Username = ? WHERE Safe_ID = ?"""
            data = (new_updated_platform_username, self.platform_id)
            cursor.execute(sql_update_query, data)

            # Email
            sql_update_query = """UPDATE UserSafe SET Email = ? WHERE Safe_ID = ?"""
            data = (new_updated_platform_email, self.platform_id)
            cursor.execute(sql_update_query, data)

            # Mobile
            sql_update_query = """UPDATE UserSafe SET Mobile = ? WHERE Safe_ID = ?"""
            data = (new_updated_platform_mobile, self.platform_id)
            cursor.execute(sql_update_query, data)

            # Password
            sql_update_query = """UPDATE UserSafe SET Password = ? WHERE Safe_ID = ?"""
            data = (new_updated_platform_password, self.platform_id)
            cursor.execute(sql_update_query, data)

            connection.commit()

            self.update_platform_data.destroy()
            self.goto = "Options"
            return self.goto

    def back_to_options_page(self):
        """If The User Wishes To Cancel Navigate The User To The Options Page"""
        self.update_platform_data.destroy()
        self.goto = "Options"
        return self.goto
