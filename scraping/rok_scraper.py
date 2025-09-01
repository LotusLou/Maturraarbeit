from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import rok_datum
from datetime import datetime, date 

# Klasse für den Scraper der Rok-Bar
class rok(baseScraper):
    def __init__(self,):
        super().__init__("https://www.rokklub.ch/programm")
        self.events = []

    # Die Haupt-Scraping-Funktion für Rok
    def scraper(self, Event):
        self.startDriver()  # Öffnet die Rok-Website
        
        # Leere Listen für Datum-Teile vorbereiten
        month_str = []
        day_str = []
        
        # Sammelt alle Event-Links von der Hauptseite
        eventLinks = self.findAllLinks("//ul[contains(@class, 'list-events')]//a")
        
        # Sucht Monat und Tag separat (Rok zeigt sie getrennt an)
        month = self.findElement("//div[contains(@class, 'month')]")  # Monat (z.B. "März")
        day = self.findElement("//div[contains(@class, 'weekdate')]")  # Tag (z.B. "15")
        year = str(date.today().year)  # Nimmt das aktuelle Jahr
        
        # Wandelt die HTML-Elemente in Text um
        month_str = [m.text.strip() for m in month]
        day_str = [d.text.strip() for d in day]

        # Stellt sicher, dass alle Listen gleich lang sind
        min_len = min(len(eventLinks), len(month_str), len(day_str))
        if min_len == 0:
            self.close()
            return

        # Geht durch alle gefundenen Events
        for i in range(min_len):
            link = eventLinks[i]
            self.driver.get(link)  # Öffnet die Event-Detail-Seite
            
            # Sammelt Event-Informationen von der Detail-Seite
            Title = self.findElement("//h1")
            time_el = self.findElement("//h2")
            Text = self.findElement("//p")
            
            # Baut das Datum aus den gesammelten Teilen zusammen
            date_obj = rok_datum(month_str[i], day_str[i], year)
            
            # Extrahiert die Texte
            title = Title[0].text if Title else ""
            time_raw = time_el[0].text if time_el else ""
            img = "https://www.rokklub.ch/_bilder/_default/rokklub_logo.svg"  # Standard-Logo
            text = Text[0].text if Text else ""

            # Versucht die Startzeit zu extrahieren
            try:
                time_str = time_raw.split(" - ")  # Teilt bei " - " auf (ChatGPT)
                time_obj = datetime.strptime(time_str[1], "%H:%M").time() if len(time_str) > 1 and time_str[1] else None
            except Exception:
                time_obj = None  # Falls die Zeit nicht lesbar ist
            
            # Erstellt ein neues Event mit allen gesammelten Infos
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, img=img, text=text, club="Rok", link="https://www.rokklub.ch/programm"))
        
        self.close()  # Schließt den Browser

