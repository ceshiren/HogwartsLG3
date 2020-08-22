from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _url = ""
    def __init__(self, driver_base = None):
        if driver_base is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver:WebDriver = driver_base
        if self.url != "":
            self.driver.get(self.url)
        # 隐式等待
        self.driver.implicitly_wait(3)

    def find(self, by , value):
        return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        return self.driver.find_elements(by=by, value= value)
    def base_quit(self):
        return self.driver.quit()



