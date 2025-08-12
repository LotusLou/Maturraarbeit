from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import schwarzeschaf_datum, schwarzeschafe_titel
from datetime import datetime, time
import re

class schwarzeschaf(baseScraper):
    
    def __init__(self,):
        super().__init__("https://www.dasschwarzeschaf.ch/programm")
        self.events= []
    def scraper(self, Event):
        self.startDriver()
        Title2 = self.findElement("//div[contains(@data-testid, 'mesh-container-content')]/div[2]/h4/span")
        Date = self.findElement("//span[contains(text(), '202')]")
        # Titel Formatieren:
        titles = schwarzeschafe_titel(Title2)

        # Datum Formatieren mit Regex:
        dates = []
        for Block in Date:
            raw = Block.get_attribute("innerHTML")
            found_dates = re.findall(r"\d{2}\.\d{2}\.\d{4}", raw)
            dates.extend(found_dates)

        min_len = min(len(titles), len(dates))  # Nur bis zur kleinsten Länge iterieren
        for el in range(min_len):
            date_obj = schwarzeschaf_datum(dates[el])
            if date_obj:
                self.events.append(Event(title=titles[el], date=date_obj, Starttime=datetime.strptime("22:00", "%H:%M").time(), Endtime=datetime.strptime("04:00", "%H:%M").time(), img="https://i.pinimg.com/736x/dc/47/23/dc4723738dd4f691a290a1625b8ca4c9.jpg", club="Das schwarze Schaf", link="https://www.dasschwarzeschaf.ch/programm"))
        self.close()