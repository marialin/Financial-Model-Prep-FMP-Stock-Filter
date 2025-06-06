from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import stripe

stripe.api_key = 'your_stripe_secret_key'

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .auth import auth_bp
    from .routes import main_bp
    from .payments import payments_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(payments_bp)

    return app
