from scraping.basescraper import baseScraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.common.exceptions import TimeoutException
from datetime import datetime
# Definiere URL und XPaths für die Seite
url = "https://www.schuur.ch/programm"
xpath_title = "//meta[contains(@itemprop, 'performer')]"
xpath_start = "//meta[contains(@itemprop, 'startDate')]"
xpath_end = "//meta[contains(@itemprop, 'endDate')]"

class schuur(baseScraper):
    def __init__(self,):
        super().__init__("https://www.schuur.ch/programm")
        self.events = []
    def scraper(self, Event):
        self.startDriver()
        # Sucht Alle Daten
        Title = self.findElement("//span[contains(text(), 'Party')]/ancestor::div[contains(@class, 'viz-event-box-title')][1]//meta[@itemprop='performer']")
        StartDate = self.findElement("//span[contains(text(), 'Party')]/ancestor::div[contains(@class, 'viz-event-box-title')][1]//meta[@itemprop='startDate']")
        try:
            Endtime = self.findElement("//span[contains(text(), 'Party')]/ancestor::div[contains(@class, 'viz-event-box-title')][1]//meta[@itemprop='endDate']")
        except TimeoutException:
            Endtime = []
        for el in range(len(Title)):
            title = Title[el].get_attribute("content") if Title else ""
            startdate = StartDate[el].get_attribute("content") if StartDate else ""
            date_str, time_str = startdate.split("T")
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
            time_obj = datetime.strptime(time_str, "%H:%M").time() if time_str else None
            enddate = Endtime[el].get_attribute("content") if Endtime else ""
            if enddate:
                endtime_str = enddate.replace(date_str + "T", "")
                try:
                    endtime_obj = datetime.strptime(endtime_str, "%H:%M").time()
                except Exception:
                    endtime_obj = None
            else:
                endtime_obj = None
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj))
        self.close()