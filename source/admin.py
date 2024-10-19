from flask import Blueprint


admin_b = Blueprint('admin', __name__)


@admin_b.route('/')
def admin():
    return "This is the admin Page"
