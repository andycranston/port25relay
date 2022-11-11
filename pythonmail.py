#! /usr/bin/python3
#
# pythonmail.py
#
# send mail to gandi.net webmail acount
#
# Links:
#
#      https://medium.com/analytics-vidhya/how-to-send-mail-from-a-python-script-to-gmail-account-8d8f718592f8
#

############################################################################

import sys
import os
import argparse

import smtplib
import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

############################################################################

def main():
    global progname
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--address',     help='email address', required=True)
    parser.add_argument('--subject',     help='email subject line text', required=True)
    parser.add_argument('--content',     help='filename with content for body of email', required=True)
        
    args = parser.parse_args()

    sender_email = args.address
    receiver_email = args.address

    try:
        password = os.environ['PASSWORD']
    except KeyError:
        print('environment variable PASSWORD is not set', file=sys.stderr)
        sys.exit(1)

    if password == "":
        print('environment variable PASSWORD is set to the null string', file=sys.stderr)
        sys.exit(1)

    body = ''

    try:
        contentfile = open(args.content, 'r', encoding='utf-8')
    except IOError:
        print('cannot open content file "{}" for reading'.format(args.content), file=sys.stderr)
        sys.exit(1)

    for line in contentfile:
        line = line.rstrip()

        body = body + line + '\n'

    contentfile.close()

    message = MIMEMultipart("alternative")
    message["Subject"] = args.subject
    message["From"] = sender_email
    message["To"] = receiver_email

    part1 = MIMEText(body, "plain")

    message.attach(part1)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("mail.gandi.net", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    return 0

############################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())
     
# end of file
