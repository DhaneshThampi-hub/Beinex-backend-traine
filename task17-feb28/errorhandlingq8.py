"""write a python program to handle exceptions when sending emails using Python's smtplib library.
"""

import smtplib
from email.mime.text import MIMEText


def send_email(email_from, email_to, subject, body):
    message = MIMEText(body)
    message["From"] = email_from
    message["To"] = ", ".join(email_to)
    message["Subject"] = subject

    # Connect to SMTP server (Mailtrap)
    EMAIL_HOST = "smtp.mailtrap.io"
    EMAIL_HOST_USER = "246def237286fd"
    EMAIL_HOST_PASSWORD = "fb6d1a11707b80"
    EMAIL_PORT = 2525

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            # Puts the connection to SMTP server into TLS mode
            server.starttls()
            # Login to the mail server using username and password
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            # Send mail
            server.sendmail(email_from, email_to, message.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"SMTP Exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        # User input for email details
        email_from = "dhaneshthampi010@gmail.com"
        recipients = ["dhaneshthampi10@gmail.com", "bincybiju50@gmail.com"]
        subject = "Sample"
        body = "Hello everyone, this is a sample email."

        # Send email to multiple recipients
        send_email(email_from, recipients, subject, body)

    except Exception as e:
        print(f"An error occurred: {e}")
