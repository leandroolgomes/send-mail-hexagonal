import ports.config
import ports.http_server
import ports.db
import ports.mail

components = {}
components['config'] = ports.config.start()
components['db'] = ports.db.start(components=components)
components['mail'] = ports.mail.start(components=components)
components['http_server'] = ports.http_server.start(components=components)

print('STARTED!')