from flask import Flask


def create_app(config_file="settings.py"):
    app = Flask(__name__)
    return app
