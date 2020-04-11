# Import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

BASE = (os.path.dirname(os.path.realpath(__file__)))

driver = webdriver.Chrome(BASE +'/chromedriver') 



# Run the Webdriver, save page an quit browser
driver.get("https://www.dotabuff.com/heroes/winning")

htmltext = driver.page_source
driver.quit()