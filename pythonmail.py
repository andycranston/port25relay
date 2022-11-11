#!/usr/bin/python3
#
# pythonmail.py
#
# send mail to a gmail acount
#

import sys
import os

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'andy@cranstonhub.com'
receiver_email = 'andy@cranstonhub.com'
password = 'XXXXXXXXXXXX'  # please put your password here.

message = MIMEMultipart("alternative")
message["Subject"] = "How to send mail from a Python script"
message["From"] = sender_email
message["To"] = receiver_email

body_text = "Hi, This is plain text messag and you are learing How to send mail from a Python script."

# Turn these into plain/html MIMEText objects
part1 = MIMEText(body_text, "plain")

# Add HTML/plain-text parts to MIMEMultipart message
message.attach(part1)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("mail.gandi.net", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )

sys.exit(0)
