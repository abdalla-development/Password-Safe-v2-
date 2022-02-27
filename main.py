import sqlite3
import os
from Functions import connect_to_database
from StartUpWindow import *
from LoginWindow import *
from OptionsWindow import *
from RetrieveWindow import *
from PasswordGenerationWindow import *
from UpdateUserInformationWindow import *
from UserPasswordRetrieve import *
from ChangeUserAccountPasswordWindow import *
from UpdateUserPlatformsWindow import *
from UpdatePlatformDataWindow import *
import customtkinter

login_window = ""
options_window = ""
user_password_retrieve_window = ""
update_user_information_window = ""
change_user_password_window = ""
update_user_platforms = ""
retrieve_saved_data_window = ""
password_generation_window = ""


def go_to_page(page):
    """This Function Will Navigate The User To The Next Page"""
    global login_window, options_window, user_password_retrieve_window, update_user_information_window, \
        change_user_password_window, update_user_platforms, retrieve_saved_data_window, password_generation_window
    # Go To Login Page
    if page == "Login":
        """Open Login Window & After The Window Roll Is Finished Navigate To The Next Intended Page Passed By The 
        Previous Page"""
        login_window = Login("Login")
        go_to_page(login_window.goto)

    elif page == "Options":
        """ Open Options Window & After The Window Roll Is Finished Navigate To The Next Intended Page Passed By The 
        Previous Window"""
        options_window = OptionsWindow("Options")
        go_to_page(options_window.go_to)

    elif page == "Forget My Password":
        """Open User Password Retrieve Window & After The Window Roll Is Finished Navigate To The Next Intended Page 
        Passed By The Previous Window"""
        user_password_retrieve_window = UserPasswordRetrieveWindow("User Password Retrieve")
        go_to_page(user_password_retrieve_window.goto)

    elif page == "Update My Information":
        """Open Update User Information Window & After The Window Roll Is Finished Navigate To The Next Intended Page 
        Passed By The Previous Window"""
        update_user_information_window = UpdateUserInformationWindow("Update User Information")
        go_to_page(update_user_information_window.go_to)

    elif page == "Change My Password":
        """Open Change My Account Password Window & After The Window Roll Is Finished Navigate To The Next Intended Page 
        Passed By The Previous Window"""
        change_user_password_window = ChangeUserAccountPassword("Change User Password")
        go_to_page(change_user_password_window.go_to)

    elif page == "Update Platforms":
        """Open Update Platform Window & After The Window Roll Is Finished Navigate To The Next Intended Page 
        Passed By The Previous Window"""
        update_user_platforms = UpdateUserPlatforms("Update User Platforms")
        go_to_page(update_user_platforms.goto)

    elif page == "Retrieve Saved Data":
        """Open Retrieve Saved Data Window & After The Window Roll Is Finished Navigate To The Next Intended Page 
        Passed By The Previous Window"""
        retrieve_saved_data_window = RetrieveDataWindow("Retrieve Saved Data")
        go_to_page(retrieve_saved_data_window.go_to)

    elif page == "Generate New Password":
        """Open Generate New Password Window & After The Window Roll Is Finished Navigate To The Next Intended Page 
        Passed By The Previous Window"""
        password_generation_window = PasswordGenerationWindow("Password Generation")
        go_to_page(password_generation_window.go_to)

    elif page == "Logout":
        """Go To Login Window"""
        login_window = Login("Login")
        go_to_page(login_window.goto)

    elif page == "Update Platform":
        """Open Update Platform Window And Filter The Data With The Passed Platform Index"""
        platform_index = update_user_platforms.platform_index
        platform_name = update_user_platforms.platform_name.title()
        update_platform_window = UpdatePlatformData(f"Update {platform_name} Data", platform_index)
        go_to_page(update_platform_window.goto)


# Get User Data From The Data Base
try:
    """Try If The Database File Exists Or Not"""
    # Defining Sqlite3 Connection
    connection, cursor = connect_to_database()
    cursor.execute('SELECT * FROM UserInformation')
    username_data_db = cursor.fetchall()
except sqlite3.OperationalError:
    """For The Except There Is No File Created Yet That Means This Is The First Time The User Installed The Program & It
     Need To Bring Up The Start Up Page For The User To Register His Data"""
    username_data_db = ""


if os.path.exists('MySafe.db') and len(username_data_db) != 0:
    """If The Database File Contains User Information And Not An Empty File Direct To Login Window"""
    # LoginWindow
    login_window = Login("Login")
    go_to_page(login_window.goto)

else:
    """If There Is No Database File Or The File Is Empty And Doesn't Contain User Information Bring Up Start Up Window 
    For The User Either To Create An Account Or Fill Out The Information's Required"""
    # StartUpWindow
    start_up_window = StartUpWindow("Create Account")
    go_to_page(start_up_window.go_to)

# darkdetect
