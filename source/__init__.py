from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'QU1CK B0Y 111 0A'
    
    from .views import view_b
    from .auth import auth_b
    from .admin import admin_b

    app.register_blueprint(view_b, url_prefix='/')
    app.register_blueprint(auth_b, url_prefix='/')
    app.register_blueprint(admin_b, url_prefix='/')

    return app
