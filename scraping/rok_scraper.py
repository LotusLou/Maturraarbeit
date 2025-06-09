from scraping.basescraper import baseScraper
from selenium.common.exceptions import TimeoutException
from scraping.sonstiges import rok_datum
from datetime import datetime


class rok(baseScraper):
    def __init__(self,):
        super().__init__("https://www.rokklub.ch/programm")
        self.events = []

    def scraper(self, Event):
        self.startDriver()
        month_str = []
        day_str = []
        # suche alle Links zusammen 
        eventLinks = self.findAllLinks("//ul[contains(@class, 'list-events')]//a")
        month = self.findElement("//*[contains(@class, 'month')]")
        day = self.findElement("//*[contains(@class, 'weekdate')]")
        year = "2025"
        # Fülle Listen mit den Textwerten
        month_str = [m.text.strip() for m in month]
        day_str = [d.text.strip() for d in day]

        # Sicherstellen, dass alle Listen gleich lang sind wie eventLinks
        min_len = min(len(eventLinks), len(month_str), len(day_str))
        if min_len == 0:
            self.close()
            return

        for i in range(min_len):
            link = eventLinks[i]
            self.driver.get(link)
            Title = self.findElement("//h1")
            time_el = self.findElement("//h2")
            date_obj = rok_datum(month_str[i], day_str[i], year)
            title = Title[0].text if Title else ""
            time_raw = time_el[0].text if time_el else ""
            try:
                time_str = time_raw.split(" - ")
                time_obj = datetime.strptime(time_str[1], "%H:%M").time() if len(time_str) > 1 and time_str[1] else None
            except Exception:
                time_obj = None
            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, club="Rok", link="https://www.rokklub.ch/programm"))
        self.close()

