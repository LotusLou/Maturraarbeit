from scraping.basescraper import baseScraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 

# Definiere URL und XPaths für die Seite
url = "https://www.schuur.ch/programm"
xpath_title = "//meta[contains(@itemprop, 'performer')]"
xpath_start = "//meta[contains(@itemprop, 'startDate')]"
xpath_end = "//meta[contains(@itemprop, 'endDate')]"

scraper = baseScraper(url, xpath_title, xpath_start, xpath_end)
events = scraper.driverGet()

for e in events:
    print(e)

scraper.close()

class neubad(baseScraper):
    def __init__(self,):
        super().__init__("https://www.schuur.ch/programm")
    def scraper(self):
        self.startDriver()
        Title = self.findElement("//meta[contains(@itemprop, 'performer')]") #/following-sibling::a/span
        #Startdate = self.findElement("//div[contains(@class, 'vorschau')]/span[contains(text(), 'Klubnacht')]/ancestor::h3")
        #Time= self.findElement("//div[contains(@class, 'vorschau')]/span[contains(text(), 'Klubnacht')]/ancestor::li/div/span")
        events = []
        for i in range(len(Title)):
            title = Title[i].get_attribute("content")
            event = {
                "title": title,
                # "startdate": startdate,  # auskommentiert, da nicht definiert
                # "enddate": enddate      # auskommentiert, da nicht definiert
            }
            events.append(event)
        return events  ##
        self.close()