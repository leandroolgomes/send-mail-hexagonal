import adapters.mail
import ports.db
import ports.mail

def send_mail(data,components={}):
    rows = ports.db.create_email(components=components)
    ports.mail.send_email(components=components)
    return adapters.mail.internal_to_wire(rows)
