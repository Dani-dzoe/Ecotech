from flask import Blueprint


auth_b = Blueprint('auth', __name__)



@auth_b.route('/login')
def login():
    return "This is the Login Page"



@auth_b.route('/sign-up')
def sign_up():
    return "This is the Sign-up Page"
