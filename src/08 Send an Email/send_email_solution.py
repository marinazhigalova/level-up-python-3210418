import smtplib

SENDER_EMAIL = 'YOUR_EMAIL@EMAIL.COM'  # replace with your email address
SENDER_PASSWORD = 'YOUR_PASSWORD'  # replace with your email password

def send_email(receiver, subject, message):
  message = f'Subject: {subject}\n\n{message}'
  with smtplib.SMTP('smtp.office365.com', 587) as server:
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, receiver, message)


# commands used in solution video for reference
if __name__ == '__main__':
    # replace receiver email address
    send_email('RECEIVER@EMAIL.COM', 'Notification', 'Everything is awesome!')
