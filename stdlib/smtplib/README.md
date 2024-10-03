# smtplib 

To send emails, we use a Python development server, Mailtrap online service and  
a shared webhosting mail server.

## SMTP

Simple Mail Transfer Protocol (SMTP) is a communication protocol for electronic  
mail transmission. Is is an Internet standard, which was first defined in 1982  
by RFC 821, and updated in 2008 by RFC 5321 to Extended SMTP additions. Mail  
servers and other message transfer agents use SMTP to send and receive mail  
messages.

## The smtplib module

The `smtplib` is a Python library for sending emails using the Simple Mail  
Transfer Protocol (SMTP). The `smtplib` is a built-in module; we do not need to  
install it. It abstracts away all the complexities of SMTP.  

## Mail servers

To actually send an email, we need to have access to a mail server. Python comes  
with a simple development mail server. Mailslurper is an easy to use local  
development server. Shared webhosting providers give us access to a mail server.  
We can find the details in the account.  

Note: Avoid using Gmail, because it is a highly secured server and it is quite  
complex to make it work. In fact, most if not all examples on the Internet  
demonstrating how to send an email with a Gmail server do not work. Instead, use  
development servers or a shared webhosting server.  

Finally, we can use a web service. There are development web services such as  
MailTrap or MailSlurp, or production services such as Mailgun or Mandrill.  

## The aiosmtp module 


This aiosmtp module provides an asyncio-based implementation of a server for RFC
5321 - Simple Mail Transfer Protocol (SMTP) and RFC 2033 - Local Mail Transfer
Protocol (LMTP). It is derived from Python's `smtpd.py` standard library
module, and provides both a command line interface and an API for use in testing
applications that send email.

Note that the library has been removed in Python 3.12. 

```
$ python -m aiosmtpd -n
```

We start the  mail server on port 8025.

```python
#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receivers = ['info@example.com']


port = 8025
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

with smtplib.SMTP('localhost', port) as server:

    # server.login('username', 'password')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")
```

We send a simple text message to the local development mail server.  

```python
sender = 'admin@example.com'
receivers = ['info@example.com']
```

We provide the sender and receiver(s). The example.com is a domain name used   
specifically for illustrative examples in documents.  

```python
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'
```

MimeText is used for sending text emails. We provide the subject, from and to  
options.  

```python
with smtplib.SMTP('localhost', port) as server:
...
```

The SMTP class manages a connection to an SMTP server.

```python
# server.login('username', 'password')
```

Since we use a local development server, we do not have to log in.

```python
server.sendmail(sender, receivers, msg.as_string())
```

The email is sent with sendmail.

```
$ python -m aiosmtpd -n
---------- MESSAGE FOLLOWS ----------
---------- MESSAGE FOLLOWS ----------
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Test mail
Content-Transfer-Encoding: 7bit
Subject: Test mail
From: admin@example.com
To: info@example.com
X-Peer: ('::1', 61049, 0, 0)

This is test mail
------------ END MESSAGE ------------
```

We get this message after we send the email.

## Sending mail to Mailtrap

Mailtrap offers a free plan which allows us to send 500 mails per month. Setting  
up Mailtrap is very easy. It literally takes seconds if we have Github or Google  
accounts.  


The neccessary credentials are provided in the settings page. Also, there are  
short code examples which show how to use the service, including smtplib,  
Django, or Flask.

```python
#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receiver = 'info@example.com'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

user = 'username'
password = 'passoword'

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")
```

The example sends a simple mail to the Mailtrap account.

```python
server.login(user, password)
```

The username and password are given in the settings page; they are comprised of  
random characters such as 24h328df3e32.  


## Sending email with attachment

MIMEMultipart is used when we have attachments or want to provide alternative  
versions of the same content (e.g. a plain text/HTML version).  


The `words.txt` file:

```
falcon
blue
sky
cloud
```

We have a simple text file.

```python
#!/usr/bin/python

import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender = 'admin@example.com'
receiver = 'info@example.com'

msg = MIMEMultipart()

msg['Subject'] = 'Test mail with attachment'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

filename = 'words.txt'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))

part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)

user = 'username'
password = 'password'

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("Successfully sent email")
```

The example sends an email with a text file attachment to Mailtrap.

```python
filename = 'words.txt'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))
```

We read the contents of the text file.

```python
part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)
```

The attachment is added with the attach method.


## Mailtrap with STARTTLS

Mailtrap does not support SSL on any SMTP port, it supports only STARTTLS. If we  
tried to use SSL, we would get the following error message:  

```
ssl.SSLError: [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1045)
```

The so called oportunistic TLS (Transport Layer Security) is an extension in  
plain text communication protocols. It offers a way to upgrade a plain text  
connection to an encrypted (TLS or SSL) connection instead of using a separate  
port for encrypted communication. Several protocols use a command named STARTTLS  
for this purpose. It is primarily intended as a countermeasure to passive  
monitoring.  

```python
#!/usr/bin/python

import smtplib

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
```

The example sends an email to a Mailtrap account with opportunistic TLS.

```python
server.starttls() # Secure the connection
```

The starttls puts the connection to the SMTP server into TLS mode.

## Sending mail via SSL

The following example sends an email via SSL. A webhosting SMTP server (from  
websupport.sk) is utilized.  

```python
#!/usr/bin/python

import smtplib, ssl
from email.mime.text import MIMEText

sender = 'admin@example.com'
receivers = ['info@example.com']

port = 465
user = 'admin@example.com'
password = 'password'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.websupport.sk", port, context=context) as server:

    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print('mail successfully sent')
```

The SMTP_SSL connects over an SSL encrypted socket.
