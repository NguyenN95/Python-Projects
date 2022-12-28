import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
from string import Template
from pathlib import Path

load_dotenv()

email = EmailMessage()
html_template = Template(Path("index.html").read_text())

email["from"] = os.getenv("from")
email["to"] = os.getenv("to")
email["subject"] = "This is a test email subject"

email_address = os.getenv("email_address")
email_password = os.getenv("email_password")

email.set_content(html_template.substitute({"name": "Anonymous"}), 'html')

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.ehlo()
    smtp.login(email_address, email_password)
    smtp.send_message(email)
    print("email sent!")
