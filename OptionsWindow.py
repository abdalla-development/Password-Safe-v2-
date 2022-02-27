from tkinter import *

import customtkinter


class OptionsWindow:
    """This Page Will Give The User The Options To Choose From Inorder TO Navigate Him To The Desired Page"""
    def __init__(self, title):
        """This Page Will Show The User The Different Options That He Can Do"""
        self.status = ""
        self.go_to = ""
        ################################################################################################################
        self.options = Tk()
        self.options.title(f"{title}")
        self.options.geometry("800x500")
        self.options.config(bg="#395B64")
        ################################################################################################################
        # Images
        app_logo = PhotoImage(file='Images/shield.png')
        self.options.tk.call('wm', 'iconphoto', self.options._w, app_logo)
        ################################################################################################################
        # Messages
        options_message = Label(text="Please Select An Option Bellow", font=("Arial", 12, "normal"), bg="#395B64")
        options_message.grid(row=0, column=1, columnspan=4)
        ################################################################################################################
        # Buttons
        # retrieve_button = Button(self.options, text="Retrieve", command=self.go_to_retrieve_page)
        retrieve_button = customtkinter.CTkButton(master=self.options, text="Retrieve", width=100, height=50,
                                                  corner_radius=10, compound="right", command=self.go_to_retrieve_page,
                                                  bg_color="#395B64")
        retrieve_button.grid(row=3, column=1)

        # generate_button = Button(self.options, text="Generate", command=self.go_to_generate_page)
        generate_button = customtkinter.CTkButton(master=self.options, text="Generate", width=100, height=50,
                                                  corner_radius=10, compound="right", command=self.go_to_generate_page,
                                                  bg_color="#395B64")
        generate_button.grid(row=3, column=2)

        # update_my_info_button = Button(self.options, text="Update My Account", command=self.go_to_update_my_info_page)
        update_my_info_button = customtkinter.CTkButton(master=self.options, text="Update My Account", width=100,
                                                        height=50, corner_radius=10, compound="right",
                                                        command=self.go_to_update_my_info_page, bg_color="#395B64")
        update_my_info_button.grid(row=3, column=3)

        # change_password_button = Button(self.options, text="Change Password",
        #                                 command=self.go_to_change_my_password_page)
        change_password_button = customtkinter.CTkButton(master=self.options, text="Change Password", width=100,
                                                         height=50, corner_radius=10, compound="right",
                                                         command=self.go_to_change_my_password_page,
                                                         bg_color="#395B64")
        change_password_button.grid(row=3, column=4)

        update_platforms_button = Button(self.options, text="Update Platforms Data",
                                         command=self.go_to_update_platforms_page)
        update_platforms_button = customtkinter.CTkButton(master=self.options, text="Update Platforms Data", width=100,
                                                          height=50, corner_radius=10, compound="right",
                                                          command=self.go_to_update_platforms_page, bg_color="#395B64")
        update_platforms_button.grid(row=3, column=4)

        log_out_button = Button(self.options, text="Log Out", command=self.logout)
        log_out_button = customtkinter.CTkButton(master=self.options, text="Log Out", width=100, height=50,
                                                 corner_radius=10, compound="right", command=self.logout,
                                                 fg_color="orange", bg_color="#395B64")
        log_out_button.grid(row=0, column=4)
        ################################################################################################################
        self.options.mainloop()

    def go_to_update_my_info_page(self):
        """This Function Will Navigate The User To Account Information Update Page"""
        # Close Options Page
        self.options.destroy()
        self.go_to = "Update My Information"

    def go_to_change_my_password_page(self):
        """This Function Will Navigate The User To Password Change Page"""
        # Close Options Page
        self.options.destroy()
        self.go_to = "Change My Password"

    def go_to_update_platforms_page(self):
        """This Function Will Navigate The User To Platforms Update Page"""
        # Close Options Page
        self.options.destroy()
        self.go_to = "Update Platforms"

    def go_to_retrieve_page(self):
        """This Function Will Navigate The User To Retrieve Saved Passwords Page"""
        # Close Options Page
        self.options.destroy()
        self.go_to = "Retrieve Saved Data"

    def go_to_generate_page(self):
        """This Function Will Navigate The User To Password Generation Page"""
        # Close Options Page
        self.options.destroy()
        self.go_to = "Generate New Password"

    def logout(self):
        """This Function Will Log out The User & Bring Up The Login Page"""
        # Close Options Page
        self.options.destroy()
        self.go_to = "Logout"


