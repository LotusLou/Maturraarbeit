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
from app.helper.db_helper import scrapeundSpeichere, clean
from app.helper.scrape_helper import scrape_all

main = Blueprint('main', __name__)

#Route für scrapen vom Neubad
@main.route("/scrape-neubad")
def scrape_und_speichere_1():
    anzahl = scrapeundSpeichere(neubad)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für scrapen vom Madeleine
@main.route("/scrape-madeleine")
def scrape_und_speichere_2():
    anzahl = scrapeundSpeichere(madeleine)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für scrapen vom Treibhaus
@main.route("/scrape-treibhaus")  
def scrape_und_speichere_3():
    anzahl = scrapeundSpeichere(treibhaus)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für scrapen von der Schüür
@main.route("/scrape-schuur")
def scrape_und_speichere_4():
    anzahl = scrapeundSpeichere(schuur)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für scrapen vom Bar59
@main.route("/scrape-bar59")
def scrape_und_speichere_5():
    anzahl = scrapeundSpeichere(bar59)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für scrapen vom Rok
@main.route("/scrape-rok")
def scrape_und_speichere_6():
    anzahl = scrapeundSpeichere(rok)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für scrapen vom Sudpol
@main.route("/scrape-sudpol")
def scrape_und_speichere_7():
    anzahl = scrapeundSpeichere(sudpol)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für scrapen vom Sedel
@main.route("/scrape-sedel")
def scrape_und_speichere_8():
    anzahl = scrapeundSpeichere(sedel)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für scrapen vom Schwarzenschaf
@main.route("/scrape-schwarzeschaf")
def scrape_und_speichere_9():
    anzahl = scrapeundSpeichere(schwarzeschaf)
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route fürs scrapen aller Clubseiten
@main.route("/scrape-all")
def scrapeall():
    anzahl = scrape_all()
    return f"{anzahl} Events erfolgreich gespeichert!"

#Route für die Homepage
@main.route("/")
def show_events():
    heute_date, heute_time = today()
    # filtere Event nach aktualität
    events = Event.query.order_by(Event.date, Event.Starttime)\
        .filter((Event.date > heute_date) | ((Event.date == heute_date) & (Event.Starttime >= heute_time))).all()
    #DB Inhalt in Dictionarys um schreiben für die Darstellung auf der Webseite.
    if events:
        ausgabe = []
        for event in events:
            ausgabe.append({
                "id": event.id,
                "title": event.title,
                "date": str(event.date),
                "Starttime": str(event.Starttime),
                "Endtime": clean(event.Endtime, "Keine Angaben"),
                "img": clean(event.img, "https://i.pinimg.com/736x/dc/47/23/dc4723738dd4f691a290a1625b8ca4c9.jpg") ,
                "preis" : clean((event.preis), "Preis auf Anfrage"),
                "link" : event.link,
                "club" : str(event.club),
                "text" : clean(event.text, "Kein Textbeschreib gefunden")
                })
        return render_template("index1.html", events=ausgabe)
    else:
        return {"Konnten Keine Events geladen werden."}

#Route für die dynamischen Detailseiten
@main.route("/programm/<int:event_id>") #Zeile ist von ChatGPT
def event_details(event_id):
    event = Event.query.get_or_404(event_id) #Zeile ist von ChatGPT
    ausgabe = {
                "id": event.id,
                "title": event.title,
                "date": str(event.date),
                "Starttime": str(event.Starttime),
                "Endtime": clean(event.Endtime, "Keine Angaben"),
                "img": clean(event.img, "https://i.pinimg.com/736x/dc/47/23/dc4723738dd4f691a290a1625b8ca4c9.jpg") ,
                "preis" : clean((event.preis), "Keine Angabe"),
                "link" : event.link,
                "club" : str(event.club),
                "text" : clean(event.text, "Kein Textbeschreib vorhanden")
                }
    return render_template("details.html", event=ausgabe)
#Route für die Nebenseite mit einer Suchfunktion 
@main.route("/programm")
def programm():
    return render_template("programm.html")
#Route, welche die Sucheinträge verarbeitet
@main.route("/search")
def search():
    heute_date, heute_time = today()
    q = request.args.get("q")
    print(q)
    #Prüfe, ob q eine Gemeinsamkeit mit DB Einträgen hat. 
    if q:
        resultate = Event.query.order_by(Event.date, Event.Starttime)\
            .filter((Event.date > heute_date) | ((Event.date == heute_date) & (Event.Starttime >= heute_time)))\
                .filter((Event.title.contains(q)) | (Event.club.contains(q))).limit(10).all()
    else:
        resultate = []
    return render_template("suchresultate.html", resultate = resultate)
#Route für eine Nebenseite 
@main.route("/about")
def about():
    return render_template("about.html")