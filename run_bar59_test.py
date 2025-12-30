# run_bar59_test.py
from dataclasses import dataclass
from scraping.bar59_scraperV2 import bar59  # ggf. Pfad anpassen

# Minimaler Fake-Event, damit dein Scraper etwas instanziieren kann
@dataclass
class FakeEvent:
    title: str
    date: object
    Starttime: object
    club: str
    link: str
    img: str | None
    text: str
    preis: str

def main():
    s = bar59()
    s.scraper(FakeEvent)

    print("\n--- RESULT ---")
    print("events:", len(s.events))
    for e in s.events[:5]:
        print("-", e.title, "|", e.date, "|", e.Starttime, "| img?", bool(e.img), "|", e.text)

if __name__ == "__main__":
    main()
