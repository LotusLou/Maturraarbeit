from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from flask import Flask, render_template

# Setup Driver
service = Service(r"C:\Users\Lou\OneDrive - sluz\Maturaarbeit\Maturraarbeit\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Setup Flask
app = Flask(__name__)

# Open Website and find Title Elements
driver.get("https://www.schuur.ch/programm")
time.sleep(5)  # Add a delay to allow the page to load completely
wait = WebDriverWait(driver, 10)
titleElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//meta[contains(@itemprop, 'performer')]")))
startdateElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//meta[contains(@itemprop, 'startDate')]")))
enddateElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//meta[contains(@itemprop, 'endDate')]")))

print(f"Gefundene Programmpunkte: {len(titleElements)}")
print(f"Gefundene Startdaten: {len(startdateElements)}")
print(f"Gefundene Enddaten: {len(enddateElements)}")

# Collect events data, list them in dictionaries and than to a list. so i got 1 dictionary for each event
events = []
for i in range(len(titleElements)):
    title = titleElements[i].get_attribute("content")
    startdate = startdateElements[i].get_attribute("content")
    enddate = enddateElements[i].get_attribute("content")
    event = {
        "title": title,
        "startdate": startdate,
        "enddate": enddate
    }
    events.append(event)

# Close the driver
driver.quit()

# Setup Flask route
@app.route("/")
def index():
    return render_template("index.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)