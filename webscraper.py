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
    heading3 = driver.find_elements(By.XPATH, '//h3[@innerText]');
    print(f'This is heading3 - {heading3}')
    for item in heading3:
        print(item.text)
def test():
    print("testing")


try:
    print("We made it here!")
    test()
    get_elements()
except Exception as e:
    print(f'Couldn\'t find it - {e}')
print("Finished!")