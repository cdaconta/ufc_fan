from selenium import webdriver
from selenium.webdriver.common.by import By
import os
# This can be tested at heroku.com in 'Run console' with command: python webscraper.py

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver.implicitly_wait(10) # seconds
driver.get("https://www.ufc.com/trending/all")

def get_elements():
    #elements = driver.find_elements(By.XPATH, '//div[@class="view-items-wrp"]/a')
    """ driver.find_elements(By.XPATH, '//div[@class="view-items-wrp"]/a') """
    heading3 = driver.find_elements_by_tag_name("h3")
    elements = driver.find_elements_by_tag_name("a")

    updatedLength = len(heading3)
    filteredList = []

    for item in heading3:
        print(item.get_attribute("textContent"))

    for item in elements:
        print(item.get_attribute("href"))
        substring = "news"
        substring2 = "video"
        filteredList = [string for string in item.get_attribute("href") if substring or substring2 in string]
    for item in filteredList:
        print(item)
List
try:
    print("We made it here!")

    get_elements()
except Exception as e:
    print(f'Couldn\'t find it - {e}')
print("Finished!")