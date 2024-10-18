from flask import Blueprint

views = Bluerint('views', __name__)

views.route('/')
def home():
    return "This is the homepage"
