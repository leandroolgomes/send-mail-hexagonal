import components.config
import components.db
import components.http_server
import components.mail
from ports.http_server import register_routes

def load_components():
    components_map = {}
    components_map['config'] = components.config.start()
    components_map['db'] = components.db.start(components=components_map)
    components_map['mail'] = components.mail.start(components=components_map)
    components_map['http_server'] = components.http_server.start(register_routes, components=components_map)

    return components_map
