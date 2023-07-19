import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Gmail:
    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(self, msg_from, msg_to, msg_subj, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = msg_from
            msg_to = msg_to if isinstance(msg_to, list) else [msg_to]
            msg['To'] = ', '.join(msg_to)
            msg['Subject'] = msg_subj
            msg.attach(MIMEText(message))
            ms = smtplib.SMTP(self.gmail_smtp, 587)
            ms.starttls()
            ms.ehlo()
            ms.login(self.login, self.password)
            result = ms.sendmail(msg_from, msg_to, msg.as_string())
            ms.quit()
            return result
        except Exception as e:
            return f'Error while send email: {e}'

    def receive_last_message(self):
        try:
            mail = imaplib.IMAP4_SSL(self.gmail_imap)
            mail.login(self.login, self.password)
            mail.list()
            mail.select("inbox")
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid.decode('utf-8'), '(RFC822)')
            raw_email = data[0][1]
            result = email.message_from_string(raw_email.decode('utf-8'))
            mail.logout()
            return result
        except Exception as e:
            return f'Error while receive email: {e}'


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    recipients = ['vasya@email.com', 'petya@email.com']
    subject = 'Test subject'
    message = 'Test message'
    header = None

    gmail = Gmail(login, password)
    gmail.send_message(login, recipients, subject, message)
    gmail.receive_last_message()
