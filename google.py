import time
import os
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GoogleImageScrapper:
    def __init__(self, word):
        self.SEARCH_WORD = word
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.directory = f"images/{self.SEARCH_WORD}"

    def go_to_image_search(self):
        buttons = self.browser.find_elements_by_class_name("gb_h")
        for button in buttons:
            if button.text == "이미지":
                button.click()

    def makeDir(self):
        try:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        except OSError:
            print('Error: Creating directory.' + self.directory)

    def scroll_down(self):
        last_height = self.browser.execute_script(
            "return document.body.scrollHeight")
        while True:
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    view_more = self.browser.find_element_by_class_name(
                        "mye4qd")
                    view_more.click()
                except:
                    break
            last_height = new_height

    def scrapping_img(self):
        self.makeDir()
        self.scroll_down()
        imgs = self.browser.find_elements_by_class_name("wXeWr")
        for index, img in enumerate(imgs):
            try:
                img.click()
                time.sleep(1)
                big_img = self.browser.find_element_by_xpath(
                    '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img')
                url = big_img.get_attribute("src")
                request.urlretrieve(
                    url, f'{self.directory}/{self.SEARCH_WORD}x{index + 1}.png')
            except:
                pass

    def start(self):
        self.browser.get("https://google.com")
        self.go_to_image_search()
        input = self.browser.find_element_by_class_name("gLFyf")
        input.send_keys(self.SEARCH_WORD)
        input.send_keys(Keys.ENTER)
        self.scrapping_img()

    def finish(self):
        print("Scrapping Done!")
        self.browser.quit()


user_input = input("Get Image with term: ")

image_scrapper = GoogleImageScrapper(user_input)
image_scrapper.start()
image_scrapper.finish()
