import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from datetime import date


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Sender Name'
email['to'] = 'receiver email address'
email['subject'] = 'You won the twillio! And html file template.'

today = date.today()
# email.set_content(html.substitute({'name': 'TinTin'}), 'html')  # using dictionary
email.set_content(html.substitute(name='TinTin', date=today),
                  'html')   # using keyword arguement


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender email address', 'sender email password')
    smtp.send_message(email)
    print('Email has been sent!')
