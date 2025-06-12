from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import madeleine_datum
from datetime import datetime

class madeleine (baseScraper):
    def __init__(self):
        super().__init__("https://www.lamadeleine.ch/#programm")
        self.events= []
    def scraper(self, Event):
        self.startDriver()
        Title = self.findElement("//div[contains(@class, 'em-event-content')]/p[contains(text(), 'DJ')]/preceding-sibling::h3")  
        Date = self.findElement("//div[contains(@class, 'em-event-content')]/p[contains(text(), 'DJ')]/preceding-sibling::p/strong")
        Img = self.findElement("//div[contains(@class, 'em-event-content')]/p[contains(text(), 'DJ')]/ancestor::div[contains(@class , 'em-event')][2]/img")
        for el in range(len(Title)):
            title = Title[el].text
            date_str = Date[el].text
            img = Img[el].get_attribute("src")
            date_obj, time_obj, endtime_obj = madeleine_datum(date_str)
            
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime= endtime_obj, img=img, club="Madeleine", link="https://www.lamadeleine.ch/#programm"))
        self.close()