import os
from dotenv import load_dotenv, find_dotenv
import smtplib

load_dotenv(find_dotenv())
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('PASSWORD')


