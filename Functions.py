import re
import sqlite3
from tkinter import *
import random
import os
import smtplib
from twilio.rest import Client


################################################################################################################
# General Used Variables
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_mobile = r'^\+(?:[0-9]●?){11,14}[0-9]$'
regex_password = r'^(?=\S*[a-z])(?=\S*[A-Z])(?=\S*\d)(?=\S*[^\w\s])\S{8,}$'

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
################################################################################################################


def password_validate(password_to_validate):
    """This Function Will Validate Any Password Passed To It, If The Password Is Min 8 Characters Long, Min 1 Numeric
    Character, Min 1 Lowercase Character, Min 1 Uppercase Character & Min 1 Special CharacterIt Will Return True
    Otherwise It Will Return False"""
    if re.fullmatch(regex_password, password_to_validate):
        return True

    else:
        return False


def mobile_validate(number_to_validate):
    """This Function Will Validate Any Mobile Number Passed To It Making Sure The Number Contains The International Key
    And it Will Return True If Valid"""
    if re.fullmatch(regex_mobile, number_to_validate):
        return True

    else:
        return False


def email_validate(email_to_validate):
    """This Function Will Validate Any Email Address Passed To It To Make Sure It Is A Valid Email Address"""
    if re.fullmatch(regex_email, email_to_validate):
        return True

    else:
        return False


def connect_to_database():
    """This Function Will Be Defining The Sqlite3 Connection"""
    connection = sqlite3.connect('MySafe.db')
    cursor = connection.cursor()
    return connection, cursor


def loading_animation():
    """This Function Will Create And Play Gif Animation Image On A New Window"""
    animation = Tk()
    animation.title("Please Wait Until Loading")
    frames = [PhotoImage(file='Images/loading.gif', format='gif -index %i' % i) for i in range(15)]

    def play_animation(n=0, top=None, lbl=None):
        """This Function Will Play The Animation In The Duration Of Number Of Frames In Relation To The Interval
        Of 4 Seconds"""
        # Play GIF (file name = m95.gif) in a 320x320 tkinter window

        num_cycles = 2
        count = len(frames) * num_cycles
        delay = 4000 // count  # make required cycles of animation in around 4 secs
        if n == 0:
            animation.withdraw()
            top = Toplevel()
            lbl = Label(top, image=frames[0])
            lbl.pack()
            lbl.after(delay, play_animation, n + 1, top, lbl)

        elif n < count - 1:
            lbl.config(image=frames[n % len(frames)])
            lbl.after(delay, play_animation, n + 1, top, lbl)
        else:
            top.destroy()
            animation.destroy()

    # start GIF animation
    play_animation()

    animation.mainloop()


def generate_password():
    """This Function Will Generate A New Password"""
    number_of_letters = random.randint(8, 10)
    number_of_symbols = random.randint(2, 4)
    number_of_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(number_of_letters)]
    password_list += [random.choice(symbols) for e in range(number_of_symbols)]
    password_list += [random.choice(numbers) for k in range(number_of_numbers)]
    random.shuffle(password_list)
    generated_password = "".join(password_list)
    return generated_password


def generate_validation_code():
    """This Function Will Generate Validation Code Inorder To Authenticate The User"""
    validation_code_digits = random.randint(4, 8)
    validation_code_list = [random.choice(numbers) for i in range(validation_code_digits)]
    random.shuffle(validation_code_list)
    code = "".join(validation_code_list)
    return code


def send_validation_code_email(validation_code):
    """Sending Validation Code Via Email Message To The User"""
    # Defining Sqlite3 Connection
    connection, cursor = connect_to_database()
    cursor.execute('SELECT Email FROM UserInformation')
    sending_to = cursor.fetchall()[0][0]

    # Data To Be Send To The User
    subject = "Password Safe User Password Change"
    message = f"You Are Trying To Change Your Account Password\n\nUse This Code To Complete The Process\n\n" \
              f"{validation_code}"
    recovery_message = 'Subject: {}\n\n{}'.format(subject, message)

    # App Email Account Settings
    password_safe_email = os.environ.get('SAFE_EMAIL')
    password_safe_password = os.environ.get('SAFE_PASS')
    gmail_get_way = os.environ.get('SAFE_GETWAY')

    # Sending The Email
    with smtplib.SMTP(gmail_get_way) as connection:
        connection.starttls()
        connection.login(user=password_safe_email, password=password_safe_password)
        connection.sendmail(from_addr=password_safe_password, to_addrs=sending_to, msg=f"{recovery_message}")


def send_validation_code_mobile(validation_code):
    """Sending Validation Code Via SMS Message To The User"""
    # Defining Sqlite3 Connection
    connection, cursor = connect_to_database()
    cursor.execute('SELECT Mobile FROM UserInformation')
    sending_to = cursor.fetchall()[0][0]

    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(body=f"{validation_code}", from_='+18456715358', to=f'{sending_to}')



