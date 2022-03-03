import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Jay Michalek'
email['to'] = 'recipient@gmail.com'
email['subject'] = 'Testing python email script from my PC'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummy_account@gmail.com', 'Dummy_password')
    smtp.send_message(email)
    print('Email sent!')
