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
from scraping.schüür_scraper import schuur
from scraping.bar59_scraper import bar59
from scraping.sonstiges import today
from scraping.treibhaus_scraper import treibhaus
from scraping.madeleine_scraper import madeleine

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
    #imgurl = db.Column(db.String)
#ertellen der DatenBank
with app.app_context():
    db.create_all()

#@app.route("/")
#def homepage():
#    return render_template('test.html', test=test)

@app.route("/scrape-neubad")
def scrape_und_speichere_1():
    scraper = neubad()
    scraper.scraper(Event) 
    for event in scraper.events:
        db.session.add(event)
    db.session.commit()
    return f"{len(scraper.events)} Events erfolgreich gespeichert!"

@app.route("/scrape-madeleine")
def scrape_und_speichere_5():
    scraper = madeleine()
    scraper.scraper(Event) 
    for event in scraper.events:
        db.session.add(event)
    db.session.commit()
    return f"{len(scraper.events)} Events erfolgreich gespeichert!"

@app.route("/scrape-treibhaus")  
def scrape_und_speichere_4():
    scraper = treibhaus()
    scraper.scraper(Event) 
    for event in scraper.events:
        db.session.add(event)
    db.session.commit()
    return f"{len(scraper.events)} Events erfolgreich gespeichert!"

@app.route("/scrape-schuur")
def scrape_und_speichere_2():
    scraper = schuur()
    scraper.scraper(Event) 
    print("Gefundene Events (Schüür):", scraper.events)
    # Alle Event-Objekte in DB schreiben
    for event in scraper.events:
        db.session.add(event)

    db.session.commit()
    return f"{len(scraper.events)} Events erfolgreich gespeichert!"

@app.route("/scrape-bar59")
def scrape_und_speichere_3():
    scraper = bar59()
    scraper.scraper(Event) 
    print("Gefundene Events (Bar59):", scraper.events)
    # Alle Event-Objekte in DB schreiben
    for event in scraper.events:
        db.session.add(event)

    db.session.commit()
    return f"{len(scraper.events)} Events erfolgreich gespeichert!"

@app.route("/events")
def show_events():
    heute_date, heute_time = today()
    # filtere Event nach aktualität (Heute und Zunkunft)
    events = Event.query.order_by(Event.date, Event.Starttime).filter((Event.date > heute_date) | ((Event.date == heute_date) & (Event.Starttime >= heute_time))).all()
    if events:
        ausgabe = []
        for event in events:
            ausgabe.append({
                "id": event.id,
                "title": event.title,
                "date": str(event.date) if event.date else "",
                "Starttime": str(event.Starttime) if event.Starttime else "",
                "Endtime": str(event.Endtime) if event.Endtime else ""
            })
        return render_template("index.html", events=ausgabe)
    else:
        return {"Konnten Keine Events geladen werden."}
if __name__ == "__main__":
    app.run(debug=True)