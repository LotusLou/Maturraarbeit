from app.helper.scrape_helper import scrape_all
from app import flaskapp
import schedule
import time

app = flaskapp ()

def aufgabe():
    with app.app_context():
        print("Programm fängt an zu scrapen")
        anzahl = scrape_all()
        if not anzahl:
            print(f"Gespeicherte Events:{anzahl} Alle Webseiten wurden erfolgreich gescraped!")
        else:
            print(f"Gespeicherte Events:0 Alle Webseiten wurden erfolgreich gescraped!")
schedule.every().monday.at("08:00").do(aufgabe)

while True:
    schedule.run_pending()
    time.sleep(60)
