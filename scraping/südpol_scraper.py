from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import sudpol_datum
from datetime import datetime, time
class sudpol(baseScraper):
    def __init__(self,):
        super().__init__("https://www.sudpol.ch/programm")
        self.events = []

    def scraper(self, Event):
        self.startDriver()
        eventLinks = self.findAllLinks("//li[contains(text(), 'Club')]/ancestor::a[1]")
        for Link in eventLinks:
            Title = self.findElement("//h1/span[contains(@class, 'Heading__content')]")
            Date_Starttime = self.findElement("//span[contains(@class, 'EventInfos__date-day')]")
            title = Title[0].text if Title else ""
            date_time = Date_Starttime[0].text if Date_Starttime else ""
            date_obj, time_obj = sudpol_datum(date_time)
            endtime_obj = None  # Südpol hat kein Enddatum
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj))
        self.close()



