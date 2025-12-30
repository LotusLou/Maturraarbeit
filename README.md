# Produkt meiner Maturaarbeit - Eventplattform Luzern

Dieser Ordner enthält den Code und Dateien, um meine Webseite lokal starten zu können.

---

## 1. Voraussetzungen

- **Python 3.10 oder höher** (https://www.python.org/downloads/)
- **Google Chrome installieren** (https://www.google.com/chrome/)
---

## 2. Notwendige Python-Pakete installieren
  
Bitte im Terminal ausführen:

```bash
py -m pip install selenium

py -m pip install flask

py -m pip install flask_sqlalchemy

py -m pip install sqlalchemy

py -m pip install webdriver-manager
```
---
## 3. Chromedriver

ChromeDriver ist bereits im Ordner enthalten (chromedriver.exe)

---

## 4. Starten des Programms

Um den lokalen Server zu starten müssen Sie die Datei run.py starten:


In /app/routes.py sehen Sie alle Routen die mein Produkt bietet. Diese können Sie in einem beliebigen Browser als URL eintippen: 
- localhost:5000/beliebigeRoute
Beispiele:
- localhost:5000/ => Homepage "WAS LAUFT?"
- localhost:5000/scrape-all => Alle 9 Clubs scrapen (!Hinweis bei dieser Route kann es möglich sein, dass es auf ihrem Rechner nicht funktioniert. Die Installation auf jedem Rechner anzuwenden, hat den Zeitrahmen gesprengt. Am einfachsten wäre es, wenn ich ihnen diese Funktion auf meinem Laptop zeigen könnte.)
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

- instance/project.db – SQLite-Datenbank (letztes Update: 23.09.25)
---

## 6. Kontakt 

Bei Fragen oder Unklarheiten zur bedienungen meines Produktes kontaktieren Sie bitte mich. 
