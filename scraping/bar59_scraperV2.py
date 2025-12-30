from scraping.basescraperV2 import baseScraper
from scraping.sonstiges import bar59_datum
from datetime import datetime


class bar59(baseScraper):
    def __init__(self):
        super().__init__("https://www.bar59.ch/")
        self.events = []
    def scraper(self, Event):
        
        self.open()

        CardsXpath = "//h3[.//span[contains(@class,'icon-club')]]/ancestor::div[1]"
        cards = self.find_all(CardsXpath, None , 5)

        allgemeinXpath = ".//h3[.//span[contains(@class,'icon-club')]]"

        for card in cards:
            title = self.get_text(f"{allgemeinXpath}/span[1]", root=card, default="")
            date_str = self.get_text(f".//h3/parent::div/preceding-sibling::div/span[1]",root=card, default="")
            img = self.get_attr(f"{allgemeinXpath}/parent::div//img", attr= "src", root=card, default= None )
            time_str = self.get_text(f"{allgemeinXpath}/small[1]", root=card, default="")
            text = self.get_attr(f"{allgemeinXpath}/parent::div//img/following-sibling::div", attr="innerText",root= card, default= "Keine Angaben")

            date_obj = bar59_datum(date_str) if date_str else None

            try:
                time_obj = datetime.strptime(time_str, "%H:%M").time() if time_str else None
            except Exception:
                time_obj = None

            self.events.append(Event(title=title, date=date_obj, Starttime=time_obj, club="Bar59", link="https://www.bar59.ch/",img = img, text=text, preis="keine Angaben"))
