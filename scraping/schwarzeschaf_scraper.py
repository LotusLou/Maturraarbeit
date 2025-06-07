from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import schwarzeschaf_datum
from datetime import datetime, time
import re

class schwarzeschaf(baseScraper):
    
    def __init__(self,):
        super().__init__("https://www.dasschwarzeschaf.ch/programm")
        self.events= []
    def scraper(self, Event):
        self.startDriver()
        Title = self.findElement("//div[contains(@data-testid, 'mesh-container-content')]/div[2]/h4/span/span/span/span/span")
        Title2 = self.findElement("//div[contains(@data-testid, 'mesh-container-content')]/div[2]/h4/span")
        Date = self.findElement("//span[contains(text(), '202')]")
        # Titel Formatieren:
        Title_single = Title 
        Title_block2 = Title2[-2]  # vorletztes Element
        Title_block3 = Title2[-1]  # letztes Element
        raw_block = [el.text.strip() for el in Title_single if el.text.strip()]
        raw_block2 = Title_block2.text
        raw_block3 = Title_block3.text
        split_block2 = [t.strip() for t in raw_block2.split("\n") if t.strip()] #\n steht für zeilen umbruch so kann man beim zeilen umbruch spliten 
        split_block3 = [t.strip() for t in raw_block3.split("\n") if t.strip()]
        titles = raw_block + split_block2 + split_block3 # alle Titel in eine Liste einfügen

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
                self.events.append(Event(
                    title=titles[el],
                    date=date_obj, 
                    Starttime=datetime.strptime("22:00", "%H:%M").time(),
                    Endtime=datetime.strptime("04:00", "%H:%M").time(),))
        self.close()