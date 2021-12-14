from flask import Blueprint

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return "<title>Gift Exchange</title>" \
           "<body>" \
           "<div>" \
           "<p>Welcome to Gift Exchange!</p>" \
           "<label>Please enter names for the gift exchange:</label>" \
           "<textarea rows='1' cols='100'>" \
           "</textarea>" \
           "</div>" \
           "</body>"
