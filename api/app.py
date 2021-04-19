from flask import Flask, Blueprint

me_blueprint = Blueprint("me", __name__)


@me_blueprint.route("/", methods=["GET"])
def me_api():
    return {
        "username": "dev",
        "theme": "dark",
    }


def create_app():
    app = Flask(__name__)
    app.register_blueprint(me_blueprint, url_prefix="/api/me")
    return app
