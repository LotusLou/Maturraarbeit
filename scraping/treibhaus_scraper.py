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
        # suche alle Links zusammen 
        eventLinks = self.findAllLinks("//li[contains(@class, 'mb-10')]/a[1]")
        for link in eventLinks:
            self.driver.get(link)
            Title = self.findElement("//h1[1]")
            Date = self.findElement("//time")
            Img = self.findElement("//img")
            time_el = self.findElement("/html/body/div[3]/main/div[1]/div/div/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[2]")
            try:
                Preis = self.findElement("//span[contains(text(), 'CHF')]")
                preis = Preis[0].text
            except TimeoutException:
                preis = ["Gratis"]
            try:
                endtime_el = self.findElement("/html/body/div[3]/main/div[1]/div/div/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]")
            except TimeoutException:
                endtime_el = []
            title = Title[0].text if Title else ""
            date = Date[0].get_attribute("datetime") if Date else ""
            date_obj = treibhaus_datum(date)
            time_str = time_el[0].text if time_el else ""
            img = Img[0].get_attribute("src") if Img else ""
            try:
                time_obj = datetime.strptime(time_str, "%H:%M").time() if time_str else None
            except Exception:
                time_obj = None
            endtime_str = endtime_el[0].text if endtime_el else ""
            try:
                endtime_obj = datetime.strptime(endtime_str, "%H:%M").time() if endtime_str else None
            except Exception:
                endtime_obj = None
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, preis=preis, link="https://www.treibhausluzern.ch/programm", club= "Treibhaus", img=img,))
        self.close()

