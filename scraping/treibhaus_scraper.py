from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import treibhaus_datum
from datetime import datetime

class treibhaus(baseScraper):
    def __init__(self,):
        super().__init__("https://www.treibhausluzern.ch/programm?filter=partys")
        self.events = []

    def scraper(self, Event):
        self.startDriver()
        
        try:
            eventLinks = self.findAllLinks("//li[contains(@class, 'mb-10')]/a[1]") # suche alle Links zusammen 
            if not eventLinks:
                print("Events gefunden")
                return
            for link in eventLinks:
                self.driver.get(link)
                Title = self.findElement("//h1[1]")
                Date = self.findElement("//time")
                Img = self.findElement("//img")
                Text = self.findElement("//div[contains(@class, 'prose js-force-target-blank')]")
                time_el = self.findElement("/html/body/div[3]/main/div[1]/div/div/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[2]")
                try:
                    Preis = self.findElement("//span[contains(text(), 'CHF')]")
                    preis = Preis[0].text
                except TimeoutException:
                    preis = "Gratis"
                try:
                    endtime_el = self.findElement("/html/body/div[3]/main/div[1]/div/div/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]")
                except TimeoutException:
                    endtime_el = []
                text = Text[0].text if Text else ""
                title = Title[0].text if Title else ""
                date = Date[0].get_attribute("datetime") if Date else ""
                time_str = time_el[0].text if time_el else ""
                img = Img[0].get_attribute("src") if Img else ""
                date_obj, time_obj, endtime_obj = treibhaus_datum(date, time_str , endtime_el)
                self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, preis=preis, text=text ,link="https://www.treibhausluzern.ch/programm", club= "Treibhaus", img=img,))
        except Exception as e:
            print("Allgemeines Problem mit dem Scraper.")
        self.close()

