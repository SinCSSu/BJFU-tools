import init
import smtplib
from email.mime.text import MIMEText


def send_mail(content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = '北林自动化脚本'
    message['From'] = init.sender
    message['To'] = init.receivers[0]

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(init.mail_host, 25)
        smtpObj.login(init.mail_user, init.mail_pass)
        smtpObj.sendmail(
            init.sender, init.receivers, message.as_string())
        smtpObj.quit()
        return 1
    except smtplib.SMTPException as e:
        return -1
