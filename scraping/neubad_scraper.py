from scraping.basescraper import baseScraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
from scraping.sonstiges import neubad_datum, neubad_datum2
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
        try:
            eventLinks = self.findAllLinks("//div[@class='vorschau'][.//span[contains(text(), 'Klubnacht')]]//a")
            for link in eventLinks:
                self.driver.get(link)
                Title = self.findElement("//h2[contains(@class, 'page-title')]")
                Date = self.findElement("//div[contains(@class, 'field--name-field-datum-event') and contains(@class, 'field__item')]")
                Text = self.findElement("//div[contains(@class, 'details-wrapper')]/div[contains(@class, 'field--type-text-with-summary')][1]")
                Img = self.findElement("//div[contains(@class, 'field__item')]/img[contains(@class, 'w3-image')]")
                Preis = self.findElement("//label[contains(text(), 'Eintritt')]/following::div[1]/p")
                try:
                    Endtime = self.findElement("//div[contains(@class, 'field--name-field-enddatum')]")
                except TimeoutException:
                    Endtime = []
                title = Title[0].text if Title else ""
                date = Date[0].text if Date else ""
                print(f"Debug - Raw date string: '{date}'")

                date_time = neubad_datum(date)
                date_str = date_time[0]
                time_str = date_time[1]
                print(f"Debug - Nach neubad_datum: date_str='{date_str}', time_str='{time_str}'")
                date_obj, time_obj, endtime_obj = neubad_datum2(date_str, time_str, Endtime)
                print(f"Debug - Nach neubad_datum2: date_obj={date_obj}, time_obj={time_obj}, endtime_obj={endtime_obj}")
                preis= Preis[0].text if Preis else ""
                text = Text[0].text if Text else ""
                img = Img[0].get_attribute("src") if Text else ""
                self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, club="Neubad" , link = "https://neubad.org/veranstaltungen", img=img, preis=preis, text=text))
            self.close()
        except TimeoutException:
            print(f"Keine Gefundenen Elemente")


