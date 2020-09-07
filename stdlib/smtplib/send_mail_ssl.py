#!/usr/bin/python

import smtplib, ssl
from email.mime.text import MIMEText

sender = 'admin@zetcode.com'
receivers = ['admin2@zetcode.com']

port = 465
user = 'admin@zetcode.com'
password = '17ttZdLjpY'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.websupport.sk", port, context=context) as server:

    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print('mail successfully sent')

