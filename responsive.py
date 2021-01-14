from math import ceil
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ResponsizeTester:
    def __init__(self, urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480, 960, 1366, 1920]
        self.BROWSER_HEIGHT = 1000

    def makeDir(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. ' + directory)

    def screenshots(self, url):
        self.browser.get(url)
        directory = f"screenshots/{url.replace('https://', '').split('.')[0]}"
        self.makeDir(directory)
        for size in self.sizes:
            self.browser.set_window_size(size, self.BROWSER_HEIGHT)
            time.sleep(2)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight")
            total_sections = ceil(scroll_size / self.BROWSER_HEIGHT)
            for section in range(total_sections + 1):
                self.browser.execute_script(
                    f"window.scrollTo(0, {section * self.BROWSER_HEIGHT})")
                self.browser.save_screenshot(
                    f"{directory}/{size}x{section}.png")
                time.sleep(2)

    def start(self):
        for url in self.urls:
            self.screenshots(url)

    def finish(self):
        self.browser.quit()


dicsTester = ResponsizeTester(["https://nomadcoders.co"])
dicsTester.start()
dicsTester.finish()
