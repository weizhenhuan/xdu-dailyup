import smtplib
from email.mime.text import MIMEText

import Settings

def send_email(subject, message):  
    if Settings.use_email:
        msg_from = Settings.email_address  
        passwd = Settings.email_password  
        msg_to = Settings.email_address 
    
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to

        with smtplib.SMTP_SSL(Settings.email_server, Settings.email_port) as smtp:
            smtp.login(msg_from, passwd)
            smtp.sendmail(msg_from, msg_to, msg.as_string())