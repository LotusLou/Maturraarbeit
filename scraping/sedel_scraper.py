from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import sedel_datum
from datetime import datetime, time
class sedel(baseScraper):
    def __init__(self,):
        super().__init__("https://www.sedel.ch/")
        self.events = []

    def scraper(self, Event):
        self.startDriver()
        eventLinks = self.findAllLinks("//time[contains(text(), 'Sa') or contains(text(), 'Fr')]/ancestor::li//div[contains(@class, 'field-content')]/a")
        for link in eventLinks:
            self.driver.get(link)
            Title = self.findElement("//div[contains(@class, 'field-item')]/h2")

            Date_Starttime = self.findElement("//h4/time")
            title = Title[0].text if Title else ""
            date_time = Date_Starttime[0].get_attribute("datetime") if Date_Starttime else ""
            date_obj, time_obj = sedel_datum(date_time)
            endtime_obj = None  # Sedel hat kein Enddatum
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj))
        self.close()



