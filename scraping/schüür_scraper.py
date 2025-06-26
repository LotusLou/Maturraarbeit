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
from scraping.sonstiges import schuur_datum
# Definiere URL und XPaths für die Seite

class schuur(baseScraper):
    def __init__(self,):
        super().__init__("https://www.schuur.ch/programm")
        self.events = []
    def scraper(self, Event):
        self.startDriver()
        # Sucht Alle Daten
        Title = self.findElement("//span[contains(text(), 'Party')]/ancestor::div[contains(@class, 'viz-event-box-title')][1]//meta[@itemprop='performer']")
        StartDate = self.findElement("//span[contains(text(), 'Party')]/ancestor::div[contains(@class, 'viz-event-box-title')][1]//meta[@itemprop='startDate']")
        Img =self.findElement("//span[contains(text(), 'Party')]/ancestor::article/preceding-sibling::div[contains(@class, 'viz-event-box-image-container')]//img")
        Text = self.findElement("//span[contains(text(), 'Party')]/ancestor::article/following-sibling::meta[contains(@itemprop, 'description')]")
        Preis = self.findElement("//span[contains(text(), 'Party')]/ancestor::section//span[contains(@itemprop, 'offers')][1]/meta[@itemprop= 'price']")

        try:
            Endtime = self.findElement("//span[contains(text(), 'Party')]/ancestor::div[contains(@class, 'viz-event-box-title')][1]//meta[@itemprop='endDate']")
        except TimeoutException:
            Endtime = []
        for el in range(min(len(Title), len(StartDate), len(Preis))):
            title = Title[el].get_attribute("content") if Title else ""
            startdate = StartDate[el].get_attribute("content") if StartDate else ""
            enddate = Endtime[el].get_attribute("content")
            img = Img[el].get_attribute("src")
            preis = Preis[el].get_attribute("content")
            text = Text[el].get_attribute("content")

            date_obj, time_obj, endtime_obj = schuur_datum(startdate, enddate)
            enddate = Endtime[el].get_attribute("content") if Endtime else ""
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, link="https://www.schuur.ch/programm", club="Schüür", preis=preis,img=img, text=text))
        self.close()