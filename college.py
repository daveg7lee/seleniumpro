import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GetUniversityInfo:
    def __init__(self, url):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.url = url
        self.university_list = []

    def start(self):
        self.browser.get(self.url)
        universities = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "search-result__title")))

        for university in universities:
            self.university_list.append(university.text)

        self.browser.quit()

        self.search()

    def search(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://google.com")
        for index, university_text in enumerate(self.university_list):
            if index != 0:
                browser.execute_script(
                    "window.open('https://google.com')")
            tabs = browser.window_handles
            browser.switch_to_window(tabs[index])
            input = browser.find_element_by_class_name("gLFyf")
            input.send_keys(university_text)
            input.send_keys(Keys.ENTER)


tester = GetUniversityInfo(
    "https://www.niche.com/colleges/search/best-colleges-for-computer-science/?goodFor=internationalStudents&netPrice=0,12000&type=private&type=public")

tester.start()
