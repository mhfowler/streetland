import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

from hello_settings import SECRETS_DICT


def send_text(msg, to_phone_number):
    """
    helper for sending SMS text messages
    :param msg: string text message to send
    :param to_phone_number: string of phone number to send text to (must have provider in string)
    :return:
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SECRETS_DICT['TEXT_EMAIL'], SECRETS_DICT['TEXT_PASSWORD'])

    msg = msg.encode('ascii', 'ignore')
    message = MIMEText(msg)
    message['Date'] = formatdate()
    message['From'] = SECRETS_DICT['TEXT_EMAIL']

    server.sendmail(SECRETS_DICT['TEXT_EMAIL'], to_phone_number, message.as_string())
    server.quit()


if __name__ == '__main__':
    send_text('hello', to_phone_number=SECRETS_DICT['MY_PHONE_NUMBER'])
