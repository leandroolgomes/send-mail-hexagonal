from flask import Flask
import controllers.send_mail

### HTTP server routes ###
def register_routes(components={}):
    app = Flask(__name__)
    @app.route("/send-mail", methods=['POST'])
    def send_mail():
        return controllers.send_mail.send_mail({}, components=components)
    return app
