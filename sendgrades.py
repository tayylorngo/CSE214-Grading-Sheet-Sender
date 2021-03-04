import os
import smtplib
import pylightxl as xl
from dotenv import load_dotenv, find_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from studentdata import students

load_dotenv(find_dotenv())

# DATA FROM .env
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('PASSWORD')

# EMAIL DATA
HOMEWORK_NUMBER = 2
SUBJECT = "CSE 214 Homework " + str(HOMEWORK_NUMBER) + " Grading Sheet"
body = ""


def send_email(from_address, to_address, subject, filename):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, PASSWORD)
        smtp.send_message(msg)
        smtp.close()
    print("Email sent to: " + to_address)


def main():
    failed_to_send = []
    for filename in os.listdir("gradingsheets"):
        if filename.endswith('.xlsx'):
            db = xl.readxl("gradingsheets/" + filename, ws='Sheet1')
            name = db.ws(ws='Sheet1').address(address='G1')
            name = name[6:len(name)]
            if students.get(name) is not None:
                send_email(EMAIL_ADDRESS, students.get(name), SUBJECT, "gradingsheets/" + filename)
            else:
                failed_to_send.append(name)
    print()
    for student in failed_to_send:
        print("Email not sent to: " + student)


main()
