from selenium import webdriver
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

try:
    heading3 = driver.find_elements_by_tag_name("h3")
    for item in heading3:   
        print(item.getAttribute("innerText"))
except:
    print("Couldn't find it")
print("Finished!")