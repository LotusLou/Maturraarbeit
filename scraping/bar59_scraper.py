from scraping.basescraper import baseScraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 

class bar59(baseScraper):
    
    def __init__(self,):
        super().__init__("https://www.bar59.ch/")
    def scraper(self):
        self.startDriver()
        events = []
        Title = self.findElement("//h3/span[1]")  
        Date = self.findElement("//h3/parent::div/preceding-sibling::div/span[1]") 
        for el in range(len(Title)):
            title = Title[el].text
            date = Date[el].text
            events.append({
                "title": title,
                "startdate": date,
                "link": self.url
            })
        self.close()
        return events  ##
bar59_scraper = bar59()  # Objekt erstellen
events = bar59_scraper.scraper()  # Methode aufrufen und Events speichern
for event in events:
    print(event)