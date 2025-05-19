from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
class baseScraper: 

    def __init__(self, url,): 
        self.url = url
        self.driver= self.setupDriver() #Chatgpt
    def setupDriver (self):
        service = Service(ChromeDriverManager().install()) # Automatisch Neuste Version installieren ChatGPT
        driver = webdriver.Chrome(service=service)
        return driver #Chatgpt
    def startDriver (self):
        if self.driver is None:#
            raise RuntimeError("WebDriver funktioniert nicht.")#
        self.driver.get(self.url)
        time.sleep(3)
    def findElement(self, Xpath):
        wait = WebDriverWait(self.driver, 10)
        findElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, Xpath)))
        return findElements #ChatGPT
    def findAllLinks(self, Xpath,):
        base_url = self.url
        Links = []
        Linkselemente = self.findElement(Xpath)
        for el in Linkselemente:
            href = el.get_attribute("href")
            if href:
                # Wenn es ein relativer Link ist, Basis-URL hinzufügen ChatGPT
                if href.startswith("/"):
                    href = base_url + href
                Links.append(href)
        return Links
    def scraper ():
        pass
    def close(self):
        self.driver.quit()

