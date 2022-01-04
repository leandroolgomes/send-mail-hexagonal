from flask import Flask
import controllers.send_mail
import multiprocessing
import gunicorn.app.base

def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1

class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def start(register_routes, components={}):
    config = components['config']
    try:
        app = register_routes(components=components)
    finally:
        if config['ENV'] == 'prod':
            print('Starting in prod mode')
            options = {
                'bind': '%s:%s' % ('127.0.0.1', config['APP_PORT']),
                'workers': number_of_workers(),}
            StandaloneApplication(app, options).run()
        else:
            app.run(debug=True, port=config['APP_PORT'])
