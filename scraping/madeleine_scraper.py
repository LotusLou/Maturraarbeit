from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import madeleine_datum
from datetime import datetime

# Klasse für den Scraper des Madeleine-Clubs
class madeleine (baseScraper):
    def __init__(self):
        super().__init__("https://www.lamadeleine.ch/#programm")  # Geht direkt zum Programm-Bereich
        self.events= []  # Liste für alle Events
    
    # Die Haupt-Scraping-Funktion für Madeleine
    def scraper(self, Event):
        self.startDriver()  # Öffnet die Madeleine-Website
        
        # Sucht alle Hauptinformationen
        Title = self.findElement("//div[contains(@class, 'em-event-content')]/p[contains(text(), 'DJ')]/preceding-sibling::h3")
        Date = self.findElement("//div[contains(@class, 'em-event-content')]/p[contains(text(), 'DJ')]/preceding-sibling::p/strong")
        Img = self.findElement("//div[contains(@class, 'em-event-content')]/p[contains(text(), 'DJ')]/ancestor::div[contains(@class , 'em-event')][2]/img")
        
        # Geht durch alle gefundenen Events
        for el in range(len(Title)):
            title = Title[el].text  # Holt den Event-Titel
            date_str = Date[el].text  # Holt das Datum als Text
            img = Img[el].get_attribute("src")  # Holt die Bild-URL
            
            # Wandelt das Datum in ein brauchbares Format um
            date_obj, time_obj, endtime_obj = madeleine_datum(date_str)
            
            # Erstellt ein neues Event mit allen gesammelten Infos
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime= endtime_obj, img=img, club="Madeleine", link="https://www.lamadeleine.ch/#programm"))
        
        self.close()  # Schließt den Browser