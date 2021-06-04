from flask import Blueprint, render_template

short = Blueprint("short", __name__)


@short.route("/<short_url>")
def redirect_to_url(short_url):
    return "NotImplemented"


@short.route("/")
def index():
    return render_template("index.html")


@short.route("/add_link", methods=["POST"])
def add_link():
    return "NotImplemented"


@short.route("/stats")
def stats():
    return "NotImplemented"


@short.errorhandler(404)
def page_not_found(e):
    return "", 404
