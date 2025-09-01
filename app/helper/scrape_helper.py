from app.helper.db_helper import scrapeundSpeichere
from scraping.neubad_scraper import neubad
from scraping.schüür_scraper import schuur
from scraping.bar59_scraper import bar59
from scraping.treibhaus_scraper import treibhaus
from scraping.madeleine_scraper import madeleine
from scraping.rok_scraper import rok
from scraping.südpol_scraper import sudpol
from scraping.sedel_scraper import sedel
from scraping.schwarzeschaf_scraper import schwarzeschaf

#Funktion um alle Clubseiten gleichzeitig abzuspeichern. 
def scrape_all():
    anzahl= 0
    anzahl += scrapeundSpeichere(neubad)
    anzahl += scrapeundSpeichere(madeleine)
    anzahl += scrapeundSpeichere(treibhaus)
    anzahl += scrapeundSpeichere(schuur)
    anzahl += scrapeundSpeichere(bar59)
    anzahl += scrapeundSpeichere(rok)
    anzahl += scrapeundSpeichere(sudpol)
    anzahl += scrapeundSpeichere(sedel)
    anzahl += scrapeundSpeichere(schwarzeschaf)