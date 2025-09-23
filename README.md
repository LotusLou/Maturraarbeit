# Produkt meiner Maturraarbeit - Eventplattform Luzern

Dieser Ordner enthält den Code und Dateien, um meine Webseite lokal starten zu können.

---

## 1. Voraussetzungen

- **Python 3.10 oder höher** (https://www.python.org/downloads/)
- **Google Chrome installieren** (https://www.google.com/chrome/)
---

## 2. Notwendige Python-Pakete installieren

Im Hauptordner liegt eine `requirements.txt` bei.  
Bitte in der im Terminal ausführen:

```bash
pip install -r requirements.txt
```
---
## 3. Chromedriver

ChromeDriver ist bereits im Ordner enthalten (chromedriver.exe)

---

## 4. Starten des Programms

Um den localen Server zu starten müssen sie im Terminal folgender Befehl eingeben:
```bash
python -m run 
```

In /app/routes.py sehen sie alle Routen die mein Produkt bietet. Diese können sie in einem beliebigen Browser als URL eintippen: 
- localhost:5000/beliebigeRoute
Beispiele:
- localhost:5000/ => Homepage
- localhost:5000/scrape-all => Alle 9 Clubs scrapen
---

## 5. Ordnerübersicht

- run.py - Start-Datei

- app – Hauptordner der Flask-Anwendung

- app/routes - Routes von Flask

- app/models.py - Struktur der DB

- app/templates/ – HTML-Templates

- app/static/ – CSS/Images

- scraping/ – Selenium-Skripte

- chromedriver.exe – ChromeDriver

- instance/project.db – SQLite-Datenbank (Bewusst nicht leer aber nicht akutell, da ab dem 22.09.25 nicht mehr gescrapt wurde.)
---

## 6. Kondakt 

Bei Fragen oder Unklarheiten, zur bedienungen meines Produktes, bitte mich kontaktieren. 