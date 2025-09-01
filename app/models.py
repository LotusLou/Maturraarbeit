from flask_sqlalchemy import SQLAlchemy

#Datenbank objekt erstellt 
db = SQLAlchemy()
#Definiert den Aufbau der Datenbank
class Event(db.Model):
    __tablename__= "events"
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String, nullable= False)
    date = db.Column(db.Date)
    Starttime = db.Column(db.Time)
    Endtime = db.Column(db.Time)
    img = db.Column(db.String, nullable=False)
    text = db.Column(db.String)
    link = db.Column(db.String, nullable= False)
    preis = db.Column(db.String)
    club = db.Column(db.String, nullable= False)