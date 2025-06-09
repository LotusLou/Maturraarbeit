from scraping.basescraper import baseScraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
from scraping.sonstiges import neubad_datum
from selenium.common.exceptions import TimeoutException
from datetime import datetime
# Definiere URL und XPaths für die Seite
class neubad(baseScraper):
    def __init__(self,):
        super().__init__("https://neubad.org/veranstaltungen")
        self.events= []
    def scraper(self, Event):
        self.startDriver()
        # Sucht alle Links
        eventLinks = self.findAllLinks("//div[@class='vorschau'][.//span[contains(text(), 'Klubnacht')]]//a")
        for link in eventLinks:
            self.driver.get(link)
            Title = self.findElement("//h2[contains(@class, 'page-title')]")
            Date = self.findElement("//div[contains(@class, 'field--name-field-datum-event') and contains(@class, 'field__item')]")
            try:
                Endtime = self.findElement("//div[contains(@class, 'field--name-field-enddatum')]")
            except TimeoutException:
                Endtime = []

            title = Title[0].text if Title else ""
            date = Date[0].text if Date else ""
            date = date.replace("\nZum Kalender hinzufügen", "").strip()
            date_time = neubad_datum(date)
            date_str = date_time[0]
            time_str = date_time[1]
            # Strings in Python date/time Objekte umwandeln
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
            except Exception:
                date_obj = None
            try:
                time_obj = datetime.strptime(time_str, "%H:%M:%S").time() if time_str else None
            except Exception:
                time_obj = None
            if Endtime and Endtime[0].text:
                endtime = Endtime[0].text
                if " " in endtime:
                    _, endtime = endtime.split(" ", 1)
            else:
                endtime = ""
            # Endtime auch als time-Objekt parsen
            try:
                endtime_obj = datetime.strptime(endtime, "%H:%M:%S").time() if endtime else None
            except Exception:
                endtime_obj = None
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, club="Neubad" , link = "https://neubad.org/veranstaltungen"))
        self.close()
        #return events  ##
