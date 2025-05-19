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
    def scraper(self):
        self.startDriver()
        eventLinks= self.findAllLinks("//div[@class='vorschau'][.//span[contains(text(), 'Klubnacht')]]//a")
        events = []
        for link in eventLinks:
            self.driver.get(link)  # Gehe zur Event-Unterseite
            Title = self.findElement("//h2[contains(@class, 'page-title')]")  
            Date = self.findElement("//div[contains(@class, 'field--name-field-datum-event') and contains(@class, 'field__item')]") 
            title = Title[0].text if Title else ""
            date = Date[0].text if Date else ""
            # "Zum Kalender hinzufügen" entfernen
            date = date.replace("\nZum Kalender hinzufügen", "").strip()
            events.append({
                "title": title,
                "startdate": date,
                "link": link
            })
        self.close()
        return events  ##
neubad_scraper = neubad()  # Objekt erstellen
events = neubad_scraper.scraper()  # Methode aufrufen und Events speichern
for event in events:
    print(event)