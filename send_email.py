import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import main

# Email account credentials
smtp_server = 'smtp.gmail.com'  # For example, 'smtp.gmail.com'
smtp_port = 587  # For Gmail use 587 for TLS
username = 'Enter User Email'
password = 'Enter User Password'

# Create the email
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = username
msg['Subject'] = f'Weather in {main.place}'

# Add email body
body = main.content
msg.attach(MIMEText(body, 'plain'))

# Connect to the server and send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(username, password)
        server.send_message(msg)
        print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
