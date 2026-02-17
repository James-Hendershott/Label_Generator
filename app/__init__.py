import os
from flask import Flask


def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.pardir, "templates"),
        static_folder=os.path.join(os.pardir, "static"),
    )

    from .routes import bp
    app.register_blueprint(bp)

    return app
