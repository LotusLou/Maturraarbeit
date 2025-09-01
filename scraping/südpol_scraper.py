from scraping.basescraper import baseScraper
from scraping.sonstiges import sudpol_datum

# Klasse für den Scraper des Südpol-Clubs
class sudpol(baseScraper):
    def __init__(self,):
        super().__init__("https://www.sudpol.ch/programm")  # Südpol-Programm-Seite
        self.events = []  # Liste für alle Events

    # Die Haupt-Scraping-Funktion für Südpol
    def scraper(self, Event):
        self.startDriver()  # Öffnet die Südpol-Website
        
        # Sucht alle Links zu Club-Events
        eventLinks = self.findAllLinks("//li[contains(text(), 'Club')]/ancestor::a[1]")
        
        # Geht durch jeden gefundenen Club-Event-Link
        for Link in eventLinks:
            self.driver.get(Link)  # Öffnet die Event-Detail-Seite
            
            # Sammelt alle wichtigen Event-Informationen
            Title = self.findElement("//h1/span[contains(@class, 'Heading__content')]")
            Date_Starttime = self.findElement("//span[contains(@class, 'EventInfos__date-day')]")
            Text = self.findElement("//div[contains(@class, 'ContentSection__richtext')]")
            Img = self.findElement("//img")
            Preis = self.findElement("//span[contains(text(), 'Eintritt')]/following::span[1]")
            
            # Extrahiert die Texte aus den HTML-Elementen
            title = Title[0].text if Title else ""
            date_time = Date_Starttime[0].text if Date_Starttime else ""
            
            # Wandelt das Datum und die Zeit in brauchbare Objekt um
            date_obj, time_obj = sudpol_datum(date_time)
            
            text = Text[0].text if Text else ""
            img = Img[0].get_attribute("src") if Img else ""
            preis = Preis[0].text
            endtime_obj = None  # Südpol hat keine Endzeiten in den Daten
            
            # Erstellt ein neues Event mit allen gesammelten Infos
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, text=text, preis=preis, img=img, club="Südpol", link="https://www.sudpol.ch/programm"))
        
        self.close()  # Schließt den Browser



