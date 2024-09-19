from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
oauth = OAuth2Provider()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    oauth.init_app(app)
    celery.conf.update(app.config)
    migrate.init_app(app, db)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)


    with app.app_context():
        from .models import create_default_user
        create_default_user()
        from . import auth, billing, crm, nlp_engine, interaction_logger, error_handler
        db.create_all()

    return app

