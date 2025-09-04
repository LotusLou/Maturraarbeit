from app.models import db, Event
#Gesammelte Events aussortieren nach Doppelten Einträgen und abspeichern.
def scrapeundSpeichere(Club):
    #Scraper Objekt wird erstellt
    scraper = Club()
    #Scraper Sucht die Daten und ertellt Datensätze
    scraper.scraper(Event) 
    # Alle Event-Objekte in DB schreiben
    i = 0
    for event in scraper.events:
        #überprüfe ob es doppelte Element gibt
        prüfe = Event.query.filter_by(title=event.title, date=event.date, club=event.club).first() #first() return das erste gefunde resultat sonst none
        if not prüfe:
            db.session.add(event)
            i += 1
    
    db.session.commit()
    return i

def clean(x, standart):
    # Prüft auf None-Werte
    if x is None:
        return standart
    
    # Wandelt in String um und entfernt Leerzeichen
    s = str(x).strip()
    
    # Prüft auf leere Strings
    if s == "":
        return standart
    
    # Prüft auf "none" Werte (case-insensitive)
    if s.lower() == "none":
        return standart
    return s