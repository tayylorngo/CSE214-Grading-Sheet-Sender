import os
from dotenv import load_dotenv, find_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv(find_dotenv())
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('PASSWORD')

msg = EmailMessage()
msg['Subject'] = "CSE 214 Homework 2 Grading Sheet"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'thecse214ta@gmail.com'
msg.set_content('TESTING1234')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, PASSWORD)

    smtp.send_message(msg)