from tkinter import *
from tkinter import messagebox
from Functions import connect_to_database, email_validate, mobile_validate


class UpdateUserInformationWindow:
    """Update User Information Window Class"""
    def __init__(self, title):
        """This Page Will Allow The User To Update His Information Provided With The Registration Mainly The Email And
        Mobile Number"""
        self.go_to = ""
        self.generated_password = ""
        # Defining Sqlite3 Connection
        connection, cursor = connect_to_database()

        # Getting the user data from the database
        cursor.execute('SELECT FirstName FROM UserInformation')
        user_first_name = cursor.fetchall()[0][0]
        cursor.execute('SELECT LastName FROM UserInformation')
        user_last_name = cursor.fetchall()[0][0]
        cursor.execute('SELECT Username FROM UserInformation')
        user_username = cursor.fetchall()[0][0]
        cursor.execute('SELECT Email FROM UserInformation')
        user_email = cursor.fetchall()[0][0]
        cursor.execute('SELECT mobile FROM UserInformation')
        user_mobile = cursor.fetchall()[0][0]

        self.update_user_data = Tk()
        self.update_user_data.title(f"{title}")
        self.update_user_data.geometry("800x500")
        self.update_user_data.config(bg="#395B64")
        ################################################################################################################
        """Images"""
        app_logo = PhotoImage(file='Images/shield.png')
        self.update_user_data.tk.call('wm', 'iconphoto', self.update_user_data._w, app_logo)
        ################################################################################################################
        """Messages"""
        generate_message = Label(text="Please Provide The Information Bellow", font=("Arial", 12, "normal"))
        generate_message.grid(row=1, column=1)
        ################################################################################################################
        """Inputs"""
        # First Name
        first_name_label_update_user_info = Label(text="First Name", font=("Arial", 16, "normal"))
        first_name_label_update_user_info.grid(row=3, column=1)
        first_name_label_update_user_info_input = Entry(width=50)
        first_name_label_update_user_info_input.insert(END, f'{user_first_name}')
        first_name_label_update_user_info_input.config(state='disabled')
        first_name_label_update_user_info_input.grid(row=3, column=2)

        # Last Name
        last_name_label_update_user_info = Label(text="Last Name", font=("Arial", 16, "normal"))
        last_name_label_update_user_info.grid(row=4, column=1)
        last_name_update_user_info_input = Entry(width=50)
        last_name_update_user_info_input.insert(END, f'{user_last_name}')
        last_name_update_user_info_input.config(state='disabled')
        last_name_update_user_info_input.grid(row=4, column=2)

        #  Username
        username_label_update_user_info = Label(text="Username", font=("Arial", 16, "normal"))
        username_label_update_user_info.grid(row=5, column=1)
        username_update_user_info_input = Entry(width=50)
        username_update_user_info_input.insert(END, f'{user_username}')
        username_update_user_info_input.config(state='disabled')
        username_update_user_info_input.grid(row=5, column=2)

        # Email
        email_label_update_user_info = Label(text="Email", font=("Arial", 16, "normal"))
        email_label_update_user_info.grid(row=6, column=1)
        self.email_update_user_info_input = Entry(width=50)
        self.email_update_user_info_input.insert(END, f'{user_email}')
        self.email_update_user_info_input.grid(row=6, column=2)

        # Mobile Number
        mobile_label_update_user_info = Label(text="Mobile Number", font=("Arial", 16, "normal"))
        mobile_label_update_user_info.grid(row=7, column=1)
        self.mobile_update_user_info_input = Entry(width=50)
        self.mobile_update_user_info_input.insert(END, f'{user_mobile}')
        self.mobile_update_user_info_input.grid(row=7, column=2)
        ################################################################################################################
        """Buttons"""
        update_user_info_update_button = Button(self.update_user_data, text="Update Information",
                                                command=self.update_user_information)
        update_user_info_update_button.grid(row=10, column=1)

        update_user_info_cancel_button = Button(self.update_user_data, text="Cancel",
                                                command=self.cancel_update_information)
        update_user_info_cancel_button.grid(row=10, column=2)
        ################################################################################################################
        """Enter Key To Create An Account"""
        self.update_user_data.bind("<Return>", self.update_user_information)
        ################################################################################################################
        self.update_user_data.mainloop()

    def update_user_information(self, keypress=""):
        """This Function Will Allow The User To Update His Data & Regrading The First, Last Names And The Username Of
        The Program Are Constants He Will Only Be Able To Modify Only The Email And The Mobile Number"""
        updated_user_email = self.email_update_user_info_input.get()
        updated_user_mobile = self.mobile_update_user_info_input.get()

        # validate email & mobile
        updated_email_is_valid = email_validate(updated_user_email)
        updated_mobile_is_valid = mobile_validate(updated_user_mobile)

        if updated_email_is_valid:
            """Check If The Entered Email Address Is Valid"""
            # Defining Sqlite3 Connection
            connection, cursor = connect_to_database()

            # Update The Email
            sql_update_query = """UPDATE UserInformation SET Email = ? WHERE User_ID = ?"""
            data = (updated_user_email, 1)
            cursor.execute(sql_update_query, data)

            # Update The Mobile
            sql_update_query = """UPDATE UserInformation SET Mobile = ? WHERE User_ID = ?"""
            data = (updated_user_mobile, 1)
            cursor.execute(sql_update_query, data)

            if updated_mobile_is_valid or updated_user_mobile == "":
                """Check If The Mobile Number Is Valid Or Not, Consider The Mobile Field Could Be Either Empty Or 
                Valid"""
                print(updated_mobile_is_valid)
                connection.commit()

                messagebox.showinfo("info", "Data Updated Successfully")

                self.go_to_options_page()
            else:
                """If The Mobile Field Is Not Empty And Not Valid Display A Message To The User To Enter A Valid 
                Number"""
                messagebox.showinfo("Error", "Please Provide A Valid Mobile Number +966")

        else:
            """Id The Entered Email Address Is Not Valid Display A Message To The User To Notify Them To Enter A Valid 
            Email Address"""
            messagebox.showinfo("Error", "Please Provide A Valid Email")

    def cancel_update_information(self):
        """If The User Wishes To Cancel The Information Update Process Navigate Him Back To Option Window"""
        self.update_user_data.destroy()
        self.go_to = "Options"
        return self.go_to

    def go_to_options_page(self):
        """If The Process Ended Successfully And The New Data Had Been Saved To The Database File Navigate The User Back
         To The Option Window"""
        self.update_user_data.destroy()
        self.go_to = "Options"
        return self.go_to


