from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Setup Driver
service = Service(r"C:\Users\Lou\OneDrive - sluz\Desktop\Coding Python\Maturaarbeit\Maturraarbeit\chromedriver.exe")
driver = webdriver.Chrome(service=service)
#Open Website and find Title Elements
driver.get("https://www.schuur.ch/programm") 
textElement = driver.find_elements(By.XPATH, "//span[contains(@class, 'viz-event-name')]")

print (f"Gefundene Programmpunkte: {len(textElement)}")
for text in textElement:
    title = textElement
    print(f"Programmpunkt: {title}")
#close the link
driver.quit()