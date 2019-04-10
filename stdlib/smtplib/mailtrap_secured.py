#!/usr/bin/env python

import smtplib, ssl

from email.mime.text import MIMEText

port = 465

sender = 'admin@example.com'
receiver = 'info@example.com'

msg = MIMEText('Secured test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

user = 'username'
password = 'password'

with smtplib.SMTP("smtp.mailtrap.io", port) as server:

    server.starttls() # Secure the connection

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")
