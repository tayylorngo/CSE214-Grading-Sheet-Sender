import os
from dotenv import load_dotenv, find_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

load_dotenv(find_dotenv())
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('PASSWORD')

body = 'SOMETHING 2'

msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'thecse214ta@gmail.com'
msg['Subject'] = "CSE 214 Homework 2 Grading Sheet"

msg.attach(MIMEText(body, 'plain'))

filename = 'gradingsheets/CSE214RecitationParticipation.xlsx'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= "+filename)
msg.attach(part)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, PASSWORD)

    smtp.send_message(msg)
    smtp.close()
