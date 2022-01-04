import smtplib

def start(components={}):
    config = components['config']
    return smtplib.SMTP(config['SMTP_SERVER_URI'])