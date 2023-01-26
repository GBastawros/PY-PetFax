from . import pet
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Home Route
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'


    # register the pet blueprint
    app.register_blueprint(pet.bp)

    # return the app
    return app
