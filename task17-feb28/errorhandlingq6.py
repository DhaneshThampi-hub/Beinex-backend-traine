"""Write a Python program that reads email details (sender, recipient, subject, and body) from user input and sends the email
 using Mailtrap as the SMTP server.
"""

import smtplib
from email.mime.text import MIMEText

# compose email
email_from = "dhaneshthampi010@gmail.com"
email_to = "dhaneshthampi10@gmail.com"
subject = "sample"
body = "hello boyy"
message = MIMEText(body)
message["From"] = email_from
message["To"] = email_to
message["Subject"] = subject

# connect to SMTP server
EMAIL_HOST = "sandbox.smtp.mailtrap.io"
EMAIL_HOST_USER = "246def237286fd"
EMAIL_HOST_PASSWORD = "fb6d1a11707b80"
EMAIL_PORT = "2525"


server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
# puts the connection to SMTP server into TLS mode
server.starttls()

# login to mail server using username and password
server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

# send mail
server.sendmail(email_from, email_to, message.as_string())

# close connection
server.quit
