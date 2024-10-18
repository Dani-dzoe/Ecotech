from flask import Blueprint


admin = ('admin', __name__)


@admin.route('/')
def admin():
    return "This is the admin Page"
