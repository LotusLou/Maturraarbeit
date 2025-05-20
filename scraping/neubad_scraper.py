from scraping.basescraper import baseScraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 

# Definiere URL und XPaths für die Seite
class neubad(baseScraper):
    def __init__(self,):
        super().__init__("https://neubad.org/veranstaltungen")
        self.events= []
    def scraper(self, Event):
        self.startDriver()
        #Sucht alle Links
        eventLinks= self.findAllLinks("//div[@class='vorschau'][.//span[contains(text(), 'Klubnacht')]]//a")
        for link in eventLinks: #Geht auf jede Event-unterseite und sucht die Daten
            self.driver.get(link) 
            Title = self.findElement("//h2[contains(@class, 'page-title')]")  
            Date = self.findElement("//div[contains(@class, 'field--name-field-datum-event') and contains(@class, 'field__item')]") 
            title = Title[0].text if Title else ""
            date = Date[0].text if Date else ""
            date = date.replace("\nZum Kalender hinzufügen", "").strip()# "Zum Kalender hinzufügen" entfernen
            self.events.append(Event(title=title, date=date))#url = link #Daten werden in ein Datenbank Objekt abgespeichert.
        self.close()
        #return events  ##
