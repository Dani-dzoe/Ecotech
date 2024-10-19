from flask import Blueprint



view_b = Blueprint('views', __name__)



@view_b.route('/')
def home():
    return "This is the homepage"
