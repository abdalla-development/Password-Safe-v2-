from tkinter import *
from tkinter import messagebox

import customtkinter

from Functions import send_validation_code_email, send_validation_code_mobile, connect_to_database, \
    password_validate, generate_validation_code


class UserPasswordRetrieveWindow:
    """Password Generation Window Class"""
    def __init__(self, title):
        """This Page Will Allow The User To Save His Data For The Intended Platform By Providing The Relevant Data And
        He Will Be Given The Choice Either TO Enter A Password That Must Pass The Validation Function Or To Enable
        Automatic Generation"""
        self.goto = ""
        self.generated_password = ""
        self.validation_code = ""
        self.verification_method = ""

        self.user_password_retrieve = Tk()
        self.user_password_retrieve.title(f"{title}")
        self.user_password_retrieve.geometry("800x500")
        self.user_password_retrieve.config(bg="#395B64")
        ################################################################################################################
        """Images"""
        app_logo = PhotoImage(file='Images/shield.png')
        self.user_password_retrieve.tk.call('wm', 'iconphoto', self.user_password_retrieve._w, app_logo)

        canvas = Canvas(highlightthickness=0, bg="#395B64")
        safe_image = PhotoImage(file="Images/safe-lock.png")
        canvas.create_image(200, 110, image=safe_image)
        canvas.grid(column=0, row=0, rowspan=2)
        ################################################################################################################
        """Messages"""
        # welcome_message_1 = Label(text="Enter The Information You Want To Change", font=("Arial", 12, "normal"),
        #                           bg="#395B64")
        # welcome_message_1.grid(row=1, column=1)
        welcome_message_2 = Label(text="Please Provide The Information Below", font=("Arial", 12, "normal"),
                                  bg="#395B64")
        welcome_message_2.grid(row=1, column=1)
        ################################################################################################################
        """Inputs"""
        # Validation Code
        validation_code_label = Label(text="Password Safe", font=("Arial", 16, "normal"), bg="#395B64")
        # validation_code_label = customtkinter.CTkLabel(master=self.user_password_retrieve, corner_radius=6, width=200,
        #                                                height=40, fg_color=("gray70", "gray20"), text="Validation
        #                                                Code")
        validation_code_label.grid(row=2, column=0)
        # self.validation_code_input = Entry(width=50)
        self.validation_code_input = customtkinter.CTkEntry(master=self.user_password_retrieve, corner_radius=20
                                                            , width=300, fg_color="white",
                                                            placeholder_text="Validation Code", bg_color="#395B64")
        self.validation_code_input.grid(row=3, column=1)

        #  New Password
        # retrieve_new_password_1_label = Label(text="New Password", font=("Arial", 16, "normal"))
        # retrieve_new_password_1_label = customtkinter.CTkLabel(master=self.user_password_retrieve, corner_radius=6,
        #                                                        width=200, height=40, fg_color=("gray70", "gray20"),
        #                                                        text="New Password")
        # retrieve_new_password_1_label.grid(row=5, column=0)
        # self.retrieve_new_password_1_input = Entry(width=50, show="*")
        self.retrieve_new_password_1_input = customtkinter.CTkEntry(master=self.user_password_retrieve, corner_radius=20
                                                                    , width=300, fg_color="white", show="*",
                                                                    placeholder_text="New Password", bg_color="#395B64")
        self.retrieve_new_password_1_input.grid(row=4, column=1)

        # Re-Enter New Password
        # retrieve_new_password_2 = Label(text="Re-Enter Password", font=("Arial", 16, "normal"))
        # retrieve_new_password_2 = customtkinter.CTkLabel(master=self.user_password_retrieve, corner_radius=6,
        # width=200,
        #                                                  height=40, fg_color=("gray70", "gray20"),
        #                                                  text="Re-Enter Password")
        # retrieve_new_password_2.grid(row=6, column=0)
        # self.retrieve_new_password_2_input = Entry(width=50, show="*")
        self.retrieve_new_password_2_input = customtkinter.CTkEntry(master=self.user_password_retrieve, corner_radius=20
                                                                    , width=300, fg_color="white", show="*",
                                                                    placeholder_text="Re-Enter Password",
                                                                    bg_color="#395B64")
        self.retrieve_new_password_2_input.grid(row=6, column=1)

        ################################################################################################################
        """Buttons"""
        # verify_via_email_button = Button(self.user_password_retrieve, text="Verify Via Email",
        #                                  command=lambda: self.send_validation_code("Email"))
        verify_via_email_button = customtkinter.CTkButton(master=self.user_password_retrieve, text="Verify Via Email",
                                                          width=100, height=50, corner_radius=10, compound="right",
                                                          command=lambda: self.send_validation_code("Email"),
                                                          bg_color="#395B64")
        verify_via_email_button.grid(row=10, column=1)

        # verify_via_mobile_button = Button(self.user_password_retrieve, text="Verify Via Mobile",
        #                                   command=lambda: self.send_validation_code("Mobile"))
        verify_via_mobile_button = customtkinter.CTkButton(master=self.user_password_retrieve, text="Verify Via Mobile",
                                                           width=100, height=50, corner_radius=10, compound="right",
                                                           command=lambda: self.send_validation_code("Mobile"),
                                                           bg_color="#395B64")
        verify_via_mobile_button.grid(row=10, column=2)

        # retrieve_new_password_button = Button(self.user_password_retrieve, text="Change Password",
        #                                       command=self.create_new_retrieve_password)
        retrieve_new_password_button = customtkinter.CTkButton(master=self.user_password_retrieve,
                                                               text="Change Password", width=100, height=50,
                                                               corner_radius=10, compound="right",
                                                               command=self.create_new_retrieve_password,
                                                               bg_color="#395B64")
        retrieve_new_password_button.grid(row=11, column=1)

        retrieve_new_password_cancel_button = Button(self.user_password_retrieve, text="Cancel",
                                                     command=self.cancel_retrieve_password)
        retrieve_new_password_cancel_button = customtkinter.CTkButton(master=self.user_password_retrieve,
                                                                      text="Cancel", width=100, height=50,
                                                                      corner_radius=10, compound="right",
                                                                      command=self.cancel_retrieve_password,
                                                                      bg_color="#395B64")
        retrieve_new_password_cancel_button.grid(row=11, column=2)
        ################################################################################################################
        """Enter Key To Create An Account"""
        self.user_password_retrieve.bind("<Return>", self.create_new_retrieve_password)
        ################################################################################################################
        self.user_password_retrieve.mainloop()

    def send_validation_code(self, method):
        """This Function Will Generate A Validation Code To Be Send To The User"""
        self.validation_code = generate_validation_code()
        self.verification_method = method
        if method == "Email":
            """If The User Chose To Get The Validation Code Via Email Send It By Email"""
            send_validation_code_email(self.validation_code)
        else:
            """If The User Chose To Get The Validation Code Via Mobile Send It By Mobile"""
            send_validation_code_mobile(self.validation_code)

    def create_new_retrieve_password(self, keypress=""):
        """This Function Will Save The New Retrieved Password After It Passes The Validation"""
        # Defining Sqlite3 Connection
        connection, cursor = connect_to_database()

        # Get Fields Data
        entered_validation_code = self.validation_code_input.get()
        entered_retrieve_password_1 = self.retrieve_new_password_1_input.get()
        entered_retrieve_password_2 = self.retrieve_new_password_2_input.get()
        password_is_valid = password_validate(entered_retrieve_password_1)

        if entered_validation_code == self.validation_code:
            """Check The Entered Validation Code if It Is The Same As The Sent One"""
            if entered_retrieve_password_1 == entered_retrieve_password_2 and password_is_valid:
                """Save The New Password If The Password Is Valid And The Two Password Fields Are The Same"""
                sql_update_query = """UPDATE UserInformation SET Password = ? WHERE User_ID = ?"""
                data = (entered_retrieve_password_1, 1)
                cursor.execute(sql_update_query, data)
                connection.commit()

            elif entered_retrieve_password_1 == entered_retrieve_password_2:
                """Check If The Two Entered Passwords Are The Same But Wrong Validation Code"""
                messagebox.showinfo("Error", "The Passwords You Enter Don't Match A New Validation Code Will Be Send")
                self.validation_code = generate_validation_code()
                if self.verification_method == "Email":
                    """If The Verification Method Is Email Re-send The Validation Code Via Email"""
                    self.validation_code = generate_validation_code()
                    send_validation_code_email(self.validation_code)
                elif self.verification_method == "Mobile":
                    """If The Verification Method Is Mobile Re-send The Validation Code Via Mobile"""
                    self.validation_code = generate_validation_code()
                    send_validation_code_mobile(self.validation_code)

            elif not password_is_valid:
                """If The Entered Password Is Not Valid Guide The User To The Password Specifications Needed To Pass 
                The Validation With A Displayed Message"""
                messagebox.showinfo("Error",
                                    "Your Passwords Must Be\n➤ Min 8 Characters Length\n➤ Min 1 Numeric\n➤ Min 1 "
                                    "Lowercase\n➤ Min 1 Uppercase\n➤ Min 1 Special Character")
        else:
            """Check If The Entered Wrong Validation Code Send A New One In Regard To The Method He Had Chosen"""
            messagebox.showinfo("Error", "Wrong Validation Code A New One Will Be Send")
            validation_code = generate_validation_code()
            if self.verification_method == "Email":
                """If The Validation Method Is Email Sen The Validation Code Via Email"""
                self.validation_code = generate_validation_code()
                send_validation_code_email(self.validation_code)
            elif self.verification_method == "Mobile":
                """If The Validation Method Is Mobile Sen The Validation Code Via Mobile"""
                self.validation_code = generate_validation_code()
                send_validation_code_mobile(self.validation_code)

    def cancel_retrieve_password(self):
        """If The User Wishes To Cancel Close The User Password Retrieve Page And Navigate Him Back To Login Page"""
        self.user_password_retrieve.destroy()
        self.goto = "Login"
        return self.goto

