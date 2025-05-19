from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
class baseScraper: 

    def __init__(self, url, xpathTitel, xpathStartdate, xpathEnddate): #xpathimg
        self.url = url
        self.xpathTitel = xpathTitel
        self.xpathStartdate = xpathStartdate
        self.xpathEnddate = xpathEnddate
        ##self.xpathimg = xpathimg
        self.driver= self.setupDriver() #Chatgpt
    def setupDriver (self):
        service = Service(ChromeDriverManager().install()) # Automatisch Neuste Version installieren ChatGPT
        driver = webdriver.Chrome(service=service)
        return driver #Chatgpt
    def driverGet (self):
        if self.driver is None:#
            raise RuntimeError("WebDriver is not initialized.")#
        self.driver.get(self.url)
        time.sleep(3) 
        wait = WebDriverWait(self.driver, 10)
        
        titleElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.xpathTitel)))
        startdateElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.xpathStartdate)))
        enddateElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.xpathEnddate)))

        events = []
        for i in range(len(titleElements)):
            title = titleElements[i].get_attribute("content")
            startdate = startdateElements[i].get_attribute("content")
            enddate = enddateElements[i].get_attribute("content")
            event = {
                "title": title,
                "startdate": startdate,
                "enddate": enddate
            }
            events.append(event)
        return events  ##
    def close(self):
        self.driver.quit()

