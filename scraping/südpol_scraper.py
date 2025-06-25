from scraping.basescraper import baseScraper
from scraping.sonstiges import sudpol_datum
class sudpol(baseScraper):
    def __init__(self,):
        super().__init__("https://www.sudpol.ch/programm")
        self.events = []

    def scraper(self, Event):
        self.startDriver()
        eventLinks = self.findAllLinks("//li[contains(text(), 'Club')]/ancestor::a[1]")
        for Link in eventLinks:
            self.driver.get(Link)
            Title = self.findElement("//h1/span[contains(@class, 'Heading__content')]")
            Date_Starttime = self.findElement("//span[contains(@class, 'EventInfos__date-day')]")
            Text = self.findElement("//div[contains(@class, 'ContentSection__richtext')]")
            Img = self.findElement("//img")
            Preis = self.findElement("//span[contains(text(), 'Eintritt')]/following::span[1]")
            title = Title[0].text if Title else ""
            date_time = Date_Starttime[0].text if Date_Starttime else ""
            date_obj, time_obj = sudpol_datum(date_time)
            text = Text[0].text if Text else ""
            img = Img[0].get_attribute("src") if Img else ""
            preis = Preis[0].text
            endtime_obj = None  # Südpol hat kein Enddatum
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, Endtime=endtime_obj, text=text, preis=preis, img=img, club="Südpol", link="https://www.sudpol.ch/programm"))
        self.close()



