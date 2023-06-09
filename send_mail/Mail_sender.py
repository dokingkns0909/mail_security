import os
import smtplib
from email.mime.text import MIMEText
with open('mail_body.txt', 'r') as f:
    body = f.read()


sender = '<no-reply@accounts.google.com>'
recipients = open('receivers.txt', 'r')
recipient= recipients.readline()

while recipient :
    changebody = body.replace('tempmail',recipient)
    msg = MIMEText(changebody,"html")
    msg['Subject'] = 'security notification'
    msg['From'] = sender
    msg['To'] = recipient

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, recipient, msg.as_string())
        print("Email sent successfully.")
        recipient= recipients.readline()
    except Exception as e:
        print("error has occurred.", e)
