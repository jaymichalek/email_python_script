import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jay Michalek'
email['to'] = 'recipient@gmail.com'
email['subject'] = 'Testing python email script from my PC'

email.set_content(html.substitute({'name': 'Timmy'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummy_account@gmail.com', 'Dummy_password')
    smtp.send_message(email)
    print('Email sent!')
