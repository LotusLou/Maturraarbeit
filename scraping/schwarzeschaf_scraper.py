from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import schwarzeschaf_datum, schwarzeschafe_titel
from datetime import datetime, time
import re

# Klasse für den Scraper des Schwarzenschaf-Clubs
class schwarzeschaf(baseScraper):
    
    def __init__(self,):
        super().__init__("https://www.dasschwarzeschaf.ch/programm")
        self.events= []  # Liste für alle Events
    
    # Die Haupt-Scraping-Funktion für Schwarzeschaf
    def scraper(self, Event):
        self.startDriver()  # Öffnet die Schwarzeschaf-Website
        
        # Sucht Event-Titel und Daten separat (Schwarzeschaf hat ein spezielles Layout)
        Title2 = self.findElement("//div[contains(@data-testid, 'mesh-container-content')]/div[2]/h4/span")  # Event-Titel
        Date = self.findElement("//span[contains(text(), '202')]")  # Datums-Elemente (die "202" enthalten, also 2024, 2025, etc.)

        # Formatiert die Titel 
        titles = schwarzeschafe_titel(Title2)

        # Extrahiert Daten mit Regex-Muster (sucht nach DD.MM.YYYY Format) (ChatGPT)
        dates = []
        for Block in Date:
            raw = Block.get_attribute("innerHTML")  # Holt den HTML-Inhalt
            # Regex-Muster: \d{2}\.\d{2}\.\d{4} bedeutet "2 Ziffern, Punkt, 2 Ziffern, Punkt, 4 Ziffern"
            found_dates = re.findall(r"\d{2}\.\d{2}\.\d{4}", raw) #(ChatGPT)
            dates.extend(found_dates)  # Fügt alle gefundenen Daten zur Liste hinzu

        # Stellt sicher, dass beide Listen gleich lang sind
        min_len = min(len(titles), len(dates))
        
        # Geht durch alle gefundenen Events
        for el in range(min_len):
            # Wandelt das Datum-String in ein Python-Datum um
            date_obj = schwarzeschaf_datum(dates[el])
            
            if date_obj:  # Nur wenn das Datum gültig ist
                
                self.events.append(Event(
                    title=titles[el], 
                    date=date_obj, 
                    Starttime=datetime.strptime("22:00", "%H:%M").time(),  
                    Endtime=datetime.strptime("04:00", "%H:%M").time(),    
                    img="https://i.pinimg.com/736x/dc/47/23/dc4723738dd4f691a290a1625b8ca4c9.jpg",  
                    club="Das schwarze Schaf", 
                    link="https://www.dasschwarzeschaf.ch/programm"
                ))
        
        self.close()  # Schließt den Browser