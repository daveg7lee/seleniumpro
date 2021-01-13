from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class GoogleSearcher:
    def __init__(self, keyword, screenshot_dir, max_page):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshot_dir = screenshot_dir
        self.max_page = max_page

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        try:
            shitty_element = WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
                                                                  )
            self.browser.execute_script(
                """
                const shitty = argument[0];
                shitty.parentElement.removeChild(shitty);

                """,
                shitty_element,
            )
        except Exception:
            pass

        def screenshot_bot(results, current_page):
            print(f"counting page{current_page.text}")
            for index, result in enumerate(results):
                print(result)
                result.screenshot(
                    f"screenshots/page_{current_page.text}-{index}x{self.keyword}.png")

        def searching_bot():
            try:
                shitty_element = WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
                                                                      )
                self.browser.execute_script(
                    """
                    const shitty = argument[0];
                    shitty.parentElement.removeChild(shitty);
                    """,
                    shitty_element,
                )
            except Exception:
                pass
            results = self.browser.find_elements_by_class_name("g")
            current_page = self.browser.find_element_by_class_name("YyVfkd")
            next_page = self.browser.find_element_by_id("pnnext")

            if int(current_page.text) < self.max_page and next_page:
                screenshot_bot(results, current_page)
                next_page.click()
                searching_bot()
            else:
                screenshot_bot(results, current_page)

        searching_bot()

    def finish(self):
        self.browser.quit()


domain_competittors = GoogleSearcher("python book", "screenshots", 5)
domain_competittors.start()
domain_competittors.finish()
