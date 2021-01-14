import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

main_hashtag = "dog"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

header = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "header"))
)

input = browser.find_element_by_class_name("XTCLo")

input.send_keys(f"#{main_hashtag}")

hashtags = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "yCE8d")))

for hashtag in hashtags:
    name = hashtag.find_element_by_class_name("Ap253").text
    browser.execute_script(
        f"window.open('https://www.instagram.com/explore/tags/{name[1:]}')")
    time.sleep(1)


time.sleep(3)
