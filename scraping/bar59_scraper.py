from scraping.basescraper import baseScraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
from scraping.sonstiges import bar59_datum
from datetime import datetime

class bar59(baseScraper):
    
    def __init__(self,):
        super().__init__("https://www.bar59.ch/")
        self.events= []
    def scraper(self, Event):
        self.startDriver()
        Title = self.findElement("//span[contains(@class, 'icon-club')]/parent::h3/span[1]")  
        Date = self.findElement("//h3/parent::div/preceding-sibling::div/span[1]")
        Starttime = self.findElement("//span[contains(@class, 'icon-club')]/parent::h3/small[1]")
        min_len = min(len(Title), len(Date), len(Starttime))  # Nur bis zur kleinsten Länge iterieren
        for el in range(min_len):
            title = Title[el].text
            date_str = Date[el].text
            date_obj = bar59_datum(date_str)
            time_str = Starttime[el].text
            # Zeit-String in Python time-Objekt umwandeln
            try:
                time_obj = datetime.strptime(time_str, "%H:%M").time() if time_str else None
            except Exception:
                time_obj = None
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj))
        self.close()