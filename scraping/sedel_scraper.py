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
            Img = self.findElement("//section[contains(@class, 'block-sedel-content')]//img")
            Text = self.findElement("//div[contains(@class, 'layout__region--first-below')]/div[contains(@class, 'field-type-text-with-summary')]//p[1]")
            Date_Starttime = self.findElement("//h4/time")
            try:
                Preis = self.findElement("//div[contains(text(), 'Eintritt')]/following-sibling::div/div")
            except TimeoutException:
                Preis = []
            title = Title[0].text if Title else ""
            text = Text[0].text if Text else ""
            date_time = Date_Starttime[0].get_attribute("datetime") if Date_Starttime else ""
            date_obj, time_obj = sedel_datum(date_time)
            img = Img[0].get_attribute("src")
            preis = Preis[0].text if Preis else ""
            endtime_obj = None  # Sedel hat kein Enddatum
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, text=text ,preis =preis, link="https://www.sedel.ch/",club="Sedel", img=img))
        self.close()



