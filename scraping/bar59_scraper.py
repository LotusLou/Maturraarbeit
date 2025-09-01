from scraping.basescraper import baseScraper
from scraping.sonstiges import bar59_datum
from datetime import datetime

# Klasse für den Scraper der Bar59 und erbt vom baseScraper
class bar59(baseScraper):
    
    def __init__(self,):
        super().__init__("https://www.bar59.ch/")  # Setzt die Bar59-Website als Ziel
        self.events= []  # Liste für alle gefundenen Events
    
    # Die Haupt-Scraping-Funktion für Bar59
    def scraper(self, Event):
        self.startDriver()  # Öffnet die Bar59-Website im Browser
        
        # Sucht alle wichtigen Event-Informationen auf der Hauptseite
        Title = self.findElement("//span[contains(@class, 'icon-club')]/parent::h3/span[1]")
        Date = self.findElement("//h3/parent::div/preceding-sibling::div/span[1]")
        Starttime = self.findElement("//span[contains(@class, 'icon-club')]/parent::h3/small[1]")
        Img = self.findElement("//span[contains(@class, 'icon-club')]/parent::h3/following-sibling::div//img")
        Text = self.findElement("//span[contains(@class, 'icon-club')]/parent::h3/following-sibling::div//img/following-sibling::div")
        
        # Nimmt nur so viele Events, wie in allen Listen vorhanden sind
        min_len = min(len(Title), len(Date), len(Starttime))
        
        # Geht durch alle gefundenen Events
        for el in range(min_len):
            # Extrahiert die Daten aus den HTML-Elementen
            title = Title[el].text
            date_str = Date[el].text
            date_obj = bar59_datum(date_str)  # Wandelt das Datum in ein brauchbares Format um
            time_str = Starttime[el].text
            text = Text[el].get_attribute("innerText") if Text else ""
            img = Img[el].get_attribute("src")
            
            # Wandelt die Zeit-String in ein Python time-Objekt um
            try:
                time_obj = datetime.strptime(time_str, "%H:%M").time() if time_str else None
            except Exception:
                time_obj = None
            
            # Erstellt ein neues Event und fügt es zur Liste hinzu
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, club="Bar59", link="https://www.bar59.ch/",img = img, text=text, preis="keine Angaben"))
        
        self.close()  # Schließt den Browser