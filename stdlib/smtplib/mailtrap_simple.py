#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receiver = 'info@example.com'

msg = MIMEText('Another test mail 2')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

user = 'fe0e78fa439420'
password = 'b6bae53adb325b'

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")
