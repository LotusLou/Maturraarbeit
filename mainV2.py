from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from scraping.neubad_scraper import neubad
#Erstelle eine Datenbank als Objekt
db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
#Aufbau der Datenbank
class Event(db.Model):
    __tablename__= "events"
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String, nullable= False)
    date = db.Column(db.Date)
    Starttime = db.Column(db.Time)
    Endtime = db.Column(db.Time)
#ertellen der DatenBank
with app.app_context():
    db.create_all()

#@app.route("/")
#def homepage():
#    return render_template('test.html', test=test)

@app.route("/scrape-neubad")
def scrape_und_speichere():
    scraper = neubad()
    scraper.scraper(Event) 
    print("🔍 Route wurde aufgerufen!")# führt das Scraping durch und speichert Event-Objekte in scraper.events

    # Alle Event-Objekte in DB schreiben
    for event in scraper.events:
        db.session.add(event)

    db.session.commit()
    return f"{len(scraper.events)} Events erfolgreich gespeichert!"

if (__name__ == "__main__"):
    app.run (debug=True)