from tkinter import *
from tkinter import messagebox
from Functions import connect_to_database, password_validate


class ChangeUserAccountPassword:
    """Password Generation Window Class"""
    def __init__(self, title):
        """This Page Will Allow The User To Save His Data For The Intended Platform By Providing The Relevant Data And
        He Will Be Given The Choice Either TO Enter A Password That Must Pass The Validation Function Or To Enable
        Automatic Generation"""
        self.status = ""
        self.go_to = ""

        self.change_user_password = Tk()
        self.change_user_password.title(f"{title}")
        self.change_user_password.geometry("800x500")
        self.change_user_password.config(bg="#395B64")
        ################################################################################################################
        # Images
        app_logo = PhotoImage(file='Images/shield.png')
        self.change_user_password.tk.call('wm', 'iconphoto', self.change_user_password._w, app_logo)
        canvas = Canvas(highlightthickness=0)
        safe_image = PhotoImage(file="Images/safe-lock.png")
        canvas.create_image(237, 150, image=safe_image)
        canvas.grid(column=1, row=0, columnspan=3)
        ################################################################################################################
        # Messages
        welcome_message_1 = Label(text="Enter The Information You Want To Change", font=("Arial", 12, "normal"))
        welcome_message_1.grid(row=1, column=1)
        welcome_message_2 = Label(text="Please Provide The Information Below", font=("Arial", 12, "normal"))
        welcome_message_2.grid(row=2, column=1)
        ################################################################################################################
        # Inputs
        # Current Password
        current_password_label = Label(text="Current Password", font=("Arial", 16, "normal"))
        current_password_label.grid(row=3, column=1)
        self.current_password_input = Entry(width=50, show="*")
        self.current_password_input.grid(row=3, column=2)

        #  New Password
        new_password_1_label = Label(text="New Password", font=("Arial", 16, "normal"))
        new_password_1_label.grid(row=4, column=1)
        self.new_password_1_input = Entry(width=50, show="*")
        self.new_password_1_input.grid(row=4, column=2)

        # Re-Enter New Password
        new_password_2 = Label(text="Re-Enter Password", font=("Arial", 16, "normal"))
        new_password_2.grid(row=5, column=1)
        self.new_password_2_input = Entry(width=50, show="*")
        self.new_password_2_input.grid(row=5, column=2)

        ################################################################################################################
        # Buttons
        update_user_info_update_button = Button(self.change_user_password, text="Change Password",
                                                command=self.update_user_password)
        update_user_info_update_button.grid(row=11, column=1)

        update_user_info_cancel_button = Button(self.change_user_password, text="Cancel",
                                                command=self.cancel_change_user_password)
        update_user_info_cancel_button.grid(row=11, column=2)
        ################################################################################################################
        # Enter Key To Create An Account
        self.change_user_password.bind("<Return>", self.update_user_password)
        ################################################################################################################
        self.change_user_password.mainloop()

    def update_user_password(self, keypress=""):
        # Defining Sqlite3 Connection
        connection, cursor = connect_to_database()

        # Getting The Data
        cursor.execute('SELECT Password FROM UserInformation')
        saved_password = cursor.fetchall()[0][0]
        entered_current_password = self.current_password_input.get()
        entered_new_password_1 = self.new_password_1_input.get()
        entered_new_password_2 = self.new_password_2_input.get()
        password_is_valid = password_validate(entered_new_password_1)

        if entered_current_password == "":
            messagebox.showinfo("Error", "You Must Provide Current Password")
            self.current_password_input.focus()
        elif entered_new_password_1 == "" or entered_new_password_2 == "":
            messagebox.showinfo("Error", "You Need To Provide Both Of The New Password Fields")
            if entered_new_password_1 == "":
                self.new_password_1_input.focus()
            else:
                self.new_password_2_input.focus()
        elif saved_password == entered_current_password and entered_new_password_2 == entered_new_password_1:
            if password_is_valid:
                # Update The User Password
                sql_update_query = """UPDATE UserInformation SET Password = ? WHERE User_ID = ?"""
                data = (entered_new_password_1, 1)
                cursor.execute(sql_update_query, data)
                connection.commit()

                self.change_user_password.destroy()

            else:
                messagebox.showinfo("Error",
                                    "Your Passwords Must Be\n➤ Min 8 Characters Length\n➤ Min 1 Numeric\n➤ Min 1 "
                                    "Lowercase\n➤ Min 1 Uppercase\n➤ Min 1 Special Character")

        elif saved_password != entered_current_password:
            messagebox.showinfo("Error", "Wrong Current Password")
        elif entered_new_password_2 != entered_new_password_1:
            messagebox.showinfo("Error", "The Passwords You Entered Don't Match")

    def cancel_change_user_password(self):
        self.change_user_password.destroy()
