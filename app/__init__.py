from flask import Flask
from .models import db
from .routes import main
#erstellung von Flask
def flaskapp():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
#erstellt die Datenbank
    with app.app_context():
        from . import routes
        db.create_all()
        app.register_blueprint(main)

    return app 