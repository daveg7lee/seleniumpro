import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.youtube.com")

input = browser.find_element_by_name("search_query")

input.click()
input.send_keys("playlist")
input.send_keys(Keys.ENTER)

time.sleep(2)

title = browser.find_element_by_id("video-title")

title.click()


# browser.quit()
