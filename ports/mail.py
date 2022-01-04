import smtplib

def start(components={}):
    config = components['config']
    return smtplib.SMTP(config['SMTP_SERVER_URI'])

def send_email(components={}):
    sender = 'from@fromdomain.com'
    receivers = ['infologol@gmail.com']

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    try:
        smtpObj = components['mail']
        smtpObj.sendmail(sender, receivers, message)         
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
