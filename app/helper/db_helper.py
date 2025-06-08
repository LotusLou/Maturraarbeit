from models import db, Event

def scrapeundSpeichere(Club):
    #Scraper Objekt wird erstellt
    scraper = Club()
    #Scraper Sucht die Daten und ertellt Datensätze
    scraper.scraper(Event) 
    # Alle Event-Objekte in DB schreiben
    for event in scraper.events:
        db.session.add(event)
    
    db.session.commit()
    return f"{len(scraper.events)}"