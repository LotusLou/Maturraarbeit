from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  

# Setup Driver
service = Service(r"C:\Users\Lou\OneDrive - sluz\Maturaarbeit\Maturraarbeit\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Website and find Title Elements
driver.get("https://www.schuur.ch/programm")
time.sleep(5)  # Add a delay to allow the page to load completely
wait = WebDriverWait(driver, 10)
textElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//meta[contains(@itemprop, 'performer')]")))

print(f"Gefundene Programmpunkte: {len(textElements)}")
for element in textElements:
    title = element.get_attribute("content")  # Access text property without parentheses
    if title:  # Check if title is not empty
        print(f"Programmpunkt: {title}")

# Close the driver
driver.quit()