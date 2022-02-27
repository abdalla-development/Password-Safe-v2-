import functools
from tkinter import *
from tkinter import messagebox
from Functions import connect_to_database, password_validate


class UpdateUserPlatforms:
    """Password Generation Window Class"""
    def __init__(self, title):
        """This Page Will Allow The User To Save His Data For The Intended Platform By Providing The Relevant Data And
        He Will Be Given The Choice Either TO Enter A Password That Must Pass The Validation Function Or To Enable
        Automatic Generation"""
        self.status = ""
        self.goto = ""
        self.platform_index = 0
        self.platform_name = ""

        self.update_user_platforms = Tk()
        self.update_user_platforms.title(f"{title}")
        self.update_user_platforms.geometry("800x500")
        self.update_user_platforms.config(bg="#395B64")
        ################################################################################################################
        """Images"""
        app_logo = PhotoImage(file='Images/shield.png')
        self.update_user_platforms.tk.call('wm', 'iconphoto', self.update_user_platforms._w, app_logo)
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

        if len(saved_platforms_db) == 0:
            """If There Are No Data Saved Display A Message To The User And Give Him To The Option To Add Data"""
            ############################################################################################################
            """Messages"""
            welcome_message_1 = Label(text="Sorry But You Haven't Added Any Platforms Yet!",
                                      font=("Arial", 12, "normal"))
            welcome_message_1.grid(row=1, column=1)
            ############################################################################################################
        else:
            """IF There Are Saved Data Show The In The Form Of Buttons"""
            ############################################################################################################
            """Messages"""
            welcome_message_1 = Label(text="Please Select The Platform You Want To Update",
                                      font=("Arial", 12, "normal"))
            welcome_message_1.grid(row=1, column=1)
            ############################################################################################################
            """Buttons"""
            for i in range(len(saved_platforms_db)):
                """Fetch The Data From The Database One By One And Create A Button For Each Platform With The Name Of 
                The Button As The Name Of The Platform, Then When The User Clicks On Any Button Pass The Index Of The 
                Button To The Next Function To DO Further Process"""
                buttons.append(Button(self.update_user_platforms, text=f'{saved_platforms_db[i][1]}',
                                      command=functools.partial(self.open_platform, i, saved_platforms_db[i][1])))
                buttons[i].grid(column=7, row=i + 1, sticky=W)

        back_to_options_button = Button(self.update_user_platforms, text="Back", command=self.go_to_options_page)
        back_to_options_button.grid(row=0, column=1)
        ################################################################################################################
        """Enter Key To Create An Account"""
        self.update_user_platforms.bind("<Return>", self.open_platform)
        ################################################################################################################
        self.update_user_platforms.mainloop()

    def open_platform(self, platform_index, platform_name):
        """After The User Clicks And Chose A Platform Take The Index And The Name Of The Platform And Pass Them Through
        Inorder To Open A Specific Platform Edit Window"""
        self.update_user_platforms.destroy()
        self.goto = "Update Platform"
        self.platform_index = platform_index
        self.platform_name = platform_name
        return self.goto, self.platform_index, self.platform_name

    def go_to_options_page(self):
        """If The User Wishes To Cancel Navigate Him Back To Option Page"""
        self.update_user_platforms.destroy()
        self.goto = "Options"
        return self.goto


