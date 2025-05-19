from scraping.basescraper import baseScraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 

# Definiere URL und XPaths für die Seite
url = "https://www.bar59.ch/"
xpath_title = "//div[@class='event']/h3/span[1]"
xpath_start = "//div[@class='event']/h3/span[2]"
xpath_end = "//div[@class='event']/h3/span[1]"

scraper = baseScraper(url, xpath_title, xpath_start, xpath_end)
try:
    events = scraper.driverGet()
except Exception as e:
    print(f"Fehler beim Scrapen: {e}")
    events = []

for e in events:
    print(e)
scraper.close()