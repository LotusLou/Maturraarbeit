# Diese Datei importiert alle nötigen Teile von Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
from datetime import datetime

# Das ist die Basis-Klasse für alle Scraper, wie ein Bauplan für alle anderen Scraper
class baseScraper: 

    # Hier wird der Scraper vorbereitet
    def __init__(self, url,): 
        self.url = url  # Die Website-Adresse, die wir scrapen wollen
        self.driver= self.setupDriver() # Der Browser wird hier gestartet
    def setupDriver (self):
        # Lädt automatisch die neueste Version des Chrome-Treibers herunter (ChatGPT)
        service = Service(ChromeDriverManager().install()) 
        # Erstellt einen neuen Chrome-Browser
        driver = webdriver.Chrome(service=service)
        return driver # Gibt den Browser zurück
    # Diese Funktion öffnet die Website im Browser
    def startDriver (self):
        # Prüft, ob der Browser richtig funktioniert
        if self.driver is None:
            raise RuntimeError("WebDriver funktioniert nicht.")
        # Öffnet die gewünschte Website
        self.driver.get(self.url)
        time.sleep(3)
    # Diese Funktion sucht nach bestimmten Elementen auf der Website
    def findElement(self, Xpath):
        # Wartet maximal 10 Sekunden, bis die Elemente auf der Seite erscheinen (ChatGPT)
        wait = WebDriverWait(self.driver, 10)
        # Sucht alle Elemente, die dem XPath entsprechen
        findElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, Xpath)))
        return findElements # Gibt alle gefundenen Elemente zurück
    # Diese Funktion sammelt alle Links der Events
    def findAllLinks(self, Xpath,):
        base_url = self.url
        Links = []
        # Findet alle Link-Elemente auf der Seite
        Linkselemente = self.findElement(Xpath)
        # Geht durch jeden gefundenen Link
        for el in Linkselemente:
            href = el.get_attribute("href")  # Holt die Link-Adresse
            if href:
                # Wenn der Link nicht vollständig ist (startet mit "/"), füge die Basis-URL hinzu (ChatGPT)
                if href.startswith("/"):
                    href = base_url + href
                Links.append(href)
        return Links  # Gibt alle gesammelten Links zurück
    # Diese Funktion wird von den spezifischen Scrapern überschrieben
    def scraper ():
        pass  # Hier passiert nichts, bis die individuellen Scraper Code einsetzten 
    
    # Diese Funktion schließt den Browser sauber
    def close(self):
        self.driver.quit()

