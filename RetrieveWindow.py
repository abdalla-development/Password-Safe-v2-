import functools
from tkinter import *
from tkinter import messagebox
from Functions import connect_to_database


class RetrieveDataWindow:
    """Retrieve Saved Data Window Class"""
    def __init__(self, title):
        """This Page Will Display The Saved Platforms In The Form Of Buttons If There Are Any & And Will Show The
        Relevant Data After The User Clicks On The Platform Button"""
        self.button = []
        self.go_to = ""
        # Defining Sqlite3 Connection
        connection, cursor = connect_to_database()
        cursor.execute('SELECT * FROM UserSafe')
        self.username_saved_db = cursor.fetchall()
        ################################################################################################################
        """Initialize Retrieve Saved Data Window"""
        self.retrieve_data = Tk()
        self.retrieve_data.title(f"{title}")
        self.retrieve_data.geometry("800x800")
        self.retrieve_data.config(bg="#395B64")
        ################################################################################################################
        # Images
        app_logo = PhotoImage(file='Images/shield.png')
        self.retrieve_data.tk.call('wm', 'iconphoto', self.retrieve_data._w, app_logo)
        ################################################################################################################
        """Buttons"""
        if len(self.username_saved_db) == 0:
            """Check The Database Fill If There Are No Data Saved Display A Message To The User And Allow Him To 
            Navigate To Generation Page"""
            ############################################################################################################
            """Messages"""
            no_data_to_retrieve_label_1 = Label(text="Sorry! You Don't Have Any Saved Data Yet!", font=("Arial", 12,
                                                                                                        "normal"))
            no_data_to_retrieve_label_1.grid(row=1, column=0, columnspan=3)

            no_data_to_retrieve_label_2 = Label(
                text="You Can Go To Generate Password By Pressing The Generate Button Below"
                , font=("Arial", 12, "normal"))
            no_data_to_retrieve_label_2.grid(row=2, column=0, columnspan=3)

            ############################################################################################################
            """Buttons"""
            go_to_generate_password_button = Button(self.retrieve_data, text="Generate Password",
                                                    command=self.go_to_generate_page)
            go_to_generate_password_button.grid(row=3, column=2)
        else:
            """If There Are Data Saved In The Database Display Them In The Form Of Buttons With The Name Of The Platform
             On Buttons"""
            ############################################################################################################
            """Messages"""
            retrieve_message = Label(text="Please Enter The Name Of Platform You Want To Retrieve Password For",
                                     font=("Arial", 12, "normal"))
            retrieve_message.grid(row=1, column=1)
            ############################################################################################################
            """Buttons"""
            for i in range(len(self.username_saved_db)):
                """Generate Buttons In Relation To The Number Of Platforms Saved In The Database"""
                self.button.append(Button(self.retrieve_data, text=f'{self.username_saved_db[i][1]}',
                                          command=functools.partial(self.show_data, platform_data_index=i)))
                self.button[i].grid(column=0, row=4 + i, sticky=W)
            ############################################################################################################

        back_to_options_button = Button(self.retrieve_data, text="Back", command=self.go_to_options_page)
        back_to_options_button.grid(row=0, column=1)

        log_out_button = Button(self.retrieve_data, text="Log Out", command=self.logout)
        log_out_button.grid(row=0, column=2)
        ################################################################################################################
        self.retrieve_data.mainloop()

    def show_data(self, platform_data_index=0):
        """This Function Will Display The Specified Saved Platform Data"""
        # Get The Data
        show_data_platform_name = self.username_saved_db[platform_data_index][1]
        show_data_platform_password = self.username_saved_db[platform_data_index][5]
        show_data_platform_username = self.username_saved_db[platform_data_index][2]
        show_data_platform_email = self.username_saved_db[platform_data_index][3]
        show_data_platform_mobile = self.username_saved_db[platform_data_index][4]

        # Showing Saved Data
        messagebox.showinfo("Info", f"Platform: {show_data_platform_name}\nPassword: {show_data_platform_password}"
                                    f"\nUsername: {show_data_platform_username}\n Email: {show_data_platform_email}\n "
                                    f"Mobile: {show_data_platform_mobile}")

    def go_to_generate_page(self):
        """This Function Will Navigate The User To Password Generation Page"""
        # Close Retrieve Saved Data Page
        self.retrieve_data.destroy()
        self.go_to = "Generate New Password"

    def go_to_options_page(self):
        """This Function Will Navigate The User Back To Option Page"""
        # Close Retrieve Saved Data Page
        self.retrieve_data.destroy()
        self.go_to = "Options"

    def logout(self):
        """This Function Will Log out The User & Bring Up The Logout Page"""
        # Close Options Page
        self.retrieve_data.destroy()
        self.go_to = "Logout"
