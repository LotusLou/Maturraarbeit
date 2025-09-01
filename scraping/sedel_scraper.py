from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import sedel_datum
from datetime import datetime, time

# Klasse für den Scraper vom Sedel und erbt alle Funktionen vom baseScraper
class sedel(baseScraper):
    def __init__(self,):
        super().__init__("https://www.sedel.ch/")  # Startet den Basescraper mit der Sedel URL
        self.events = []

    # Die Haupt-Scraping-Funktion
    def scraper(self, Event):
        self.startDriver()  # Startet den Browser und öffnet die Sedel-Website
        eventLinks = self.findAllLinks("//time[contains(text(), 'Sa') or contains(text(), 'Fr')]/ancestor::li//div[contains(@class, 'field-content')]/a")
        
        # Geht durch jeden gefundenen Event-Link
        for link in eventLinks:
            self.driver.get(link)  # Öffnet die Event Detailseite
            # Sucht alle wichtigen Informationen auf der Event-Seite
            Title = self.findElement("//div[contains(@class, 'field-item')]/h2")
            Img = self.findElement("//section[contains(@class, 'block-sedel-content')]//img")
            Text = self.findElement("//div[contains(@class, 'layout__region--first-below')]/div[contains(@class, 'field-type-text-with-summary')]//p[1]")
            Date_Starttime = self.findElement("//h4/time")
            
            # Versucht den Preis zu finden, diesen gibts manchmal nicht
            try:
                Preis = self.findElement("//div[contains(text(), 'Eintritt')]/following-sibling::div/div")
            except TimeoutException:
                Preis = []
            
            # Extrahiert die Texte aus den gefundenen Elementen
            title = Title[0].text if Title else ""
            text = Text[0].text if Text else ""
            date_time = Date_Starttime[0].get_attribute("datetime") if Date_Starttime else ""
            
            # Wandelt das Datum in ein brauchbares Format um
            date_obj, time_obj = sedel_datum(date_time)
            
            img = Img[0].get_attribute("src")
            preis = Preis[0].text if Preis else ""
            endtime_obj = None  # Sedel hat keine Endzeiten in den Daten
            
            # Erstellt ein neues Event-Objekt und fügt es zur Liste hinzu
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, text=text ,preis =preis, link="https://www.sedel.ch/",club="Sedel", img=img))
        
        self.close()  # Schließt den Browser



