import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.niche.com/colleges/search/best-colleges-for-computer-science/?goodFor=internationalStudents&netPrice=0,12000&type=private&type=public")

universities = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "search-result__title")))

university_list = []

for university in universities:
    university_list.append(university.text)

browser.quit()

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://google.com")

for index, university_text in enumerate(university_list):
    if(index != 0):
        browser.execute_script(
            "window.open('https://google.com')")
    browser.switch_to.window(browser.window_handles[-1])
    input = browser.find_element_by_class_name("gLFyf")
    input.send_keys(university_text)
    input.send_keys(Keys.ENTER)
