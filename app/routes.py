from flask import Blueprint, render_template, request
from .models import Event
from scraping.neubad_scraper import neubad
from scraping.schüür_scraper import schuur
from scraping.bar59_scraper import bar59
from scraping.sonstiges import today
from scraping.treibhaus_scraper import treibhaus
from scraping.madeleine_scraper import madeleine
from scraping.rok_scraper import rok
from scraping.südpol_scraper import sudpol
from scraping.sedel_scraper import sedel
from scraping.schwarzeschaf_scraper import schwarzeschaf
from app.helper.db_helper import scrapeundSpeichere
from app.helper.scrape_helper import scrape_all

main = Blueprint('main', __name__)

@main.route("/scrape-neubad")
def scrape_und_speichere_1():
    anzahl = scrapeundSpeichere(neubad)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-madeleine")
def scrape_und_speichere_2():
    anzahl = scrapeundSpeichere(madeleine)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-treibhaus")  
def scrape_und_speichere_3():
    anzahl = scrapeundSpeichere(treibhaus)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-schuur")
def scrape_und_speichere_4():
    anzahl = scrapeundSpeichere(schuur)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-bar59")
def scrape_und_speichere_5():
    anzahl = scrapeundSpeichere(bar59)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-rok")
def scrape_und_speichere_6():
    anzahl = scrapeundSpeichere(rok)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-sudpol")
def scrape_und_speichere_7():
    anzahl = scrapeundSpeichere(sudpol)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-sedel")
def scrape_und_speichere_8():
    anzahl = scrapeundSpeichere(sedel)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-schwarzeschaf")
def scrape_und_speichere_9():
    anzahl = scrapeundSpeichere(schwarzeschaf)
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/scrape-all")
def scrapeall():
    anzahl = scrape_all()
    return f"{anzahl} Events erfolgreich gespeichert!"

@main.route("/")
def show_events():
    heute_date, heute_time = today()
    # filtere Event nach aktualität (Heute und Zunkunft)
    events = Event.query.order_by(Event.date, Event.Starttime)\
        .filter((Event.date > heute_date) | ((Event.date == heute_date) & (Event.Starttime >= heute_time))).all()
    if events:
        ausgabe = []
        for event in events:
            ausgabe.append({
                "id": event.id,
                "title": event.title,
                "date": str(event.date) if event.date else "",
                "Starttime": str(event.Starttime) if event.Starttime else "",
                "Endtime": str(event.Endtime) if event.Endtime else "Keine Angaben",
                "img": str(event.img) if event.img else "",
                "preis" : str(event.preis) if event.preis else "Keine Angaben",
                "link" : str(event.link) if event.link else "",
                "club" : str(event.club) if event.club else "",
                "text" : str(event.text) if event.text else "Kein Textbeschreib gefunden"
                })
        return render_template("index1.html", events=ausgabe)
    else:
        return {"Konnten Keine Events geladen werden."}
@main.route("/programm/<int:event_id>") #ChatGPT
def event_details(event_id):
    event = Event.query.get_or_404(event_id) #ChatGPT
    return render_template("details.html", event=event)
@main.route("/programm")
def programm():
    return render_template("programm.html")
@main.route("/search")
def search():
    heute_date, heute_time = today()
    q = request.args.get("q")
    print(q)
    if q:
        resultate = Event.query.order_by(Event.date, Event.Starttime)\
            .filter((Event.date > heute_date) | ((Event.date == heute_date) & (Event.Starttime >= heute_time)))\
                .filter((Event.title.contains(q)) | (Event.club.contains(q))).limit(10).all()
    else:
        resultate = []
    return render_template("suchresultate.html", resultate = resultate)
@main.route("/about")
def about():
    return render_template("about.html")
@main.route("/clubs")
def clubs():
    return render_template("clubs.html")