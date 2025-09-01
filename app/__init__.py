from flask import Flask
from .models import db
from .routes import main
#Erstellung des Flaskobjektes 
def flaskapp():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)

    with app.app_context(): #Zeile ist von ChatGPT
        from . import routes #Verbindung mit den Flask Routes 
        db.create_all() #Erstellt die Datenbank, wenn keine vorhanden ist 
        app.register_blueprint(main) #Zeile ist von ChatGPT

    return app 