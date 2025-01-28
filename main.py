from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Setup Driver
service = Service(r"C:\Users\Lou\OneDrive - sluz\Maturaarbeit\Maturraarbeit\chromedriver.exe")
driver = webdriver.Chrome(service=service)

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

# Prints the title and date of each program point
for i in range(len(titleElements)):
    title = titleElements[i].get_attribute("content")
    startdate = startdateElements[i].get_attribute("content")
    enddate = enddateElements[i].get_attribute("content")
    with open("index.html", "a", encoding="utf-8") as file:
        file.write(f"<p>Programmpunkt {i+1}: {title} von {startdate} bis {enddate}</p>\n")

# Close the driver
driver.quit()