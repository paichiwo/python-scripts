#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)

    return message


def generate_error_email(sender, recipient, subject, body):
    """Creates an email without an attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message


def send_email(message):
    """
    Sends the message from the configured SMTP server.
    This function needs data of your email server
    """
    mail_server = smtplib.SMTP_SSL('smtp.server', 000)  # set your smtp server and port
    mail_server.login('your_login', 'your_password')  # set your email login and password
    mail_server.send_message(message)
    mail_server.quit()


def main():
    """
    Main function with email data
    """
    sender = "example@example.com"
    recipient = "test@test.com"
    subject = "Test email with attachment from Lukas' python application"
    body = "This is a body where contents of the email will normally be written"
    attachment_path = "/path_to_attachment/file.jpg"

    message = generate_email(sender, recipient, subject, body, attachment_path)
    send_email(message)


if __name__ == '__main__':
    main()
