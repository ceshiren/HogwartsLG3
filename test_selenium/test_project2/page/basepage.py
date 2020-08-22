from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    url = ""
    def __init__(self, driver_base = None):
        if driver_base is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver:WebDriver = driver_base
        if self.url != "":
            self.driver.get(self.url)
        self.driver.implicitly_wait(3)

    def wait_for_clickable(self, element):

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))


    def find(self):
        pass

    def finds(self):
        pass

    def quit(self):
        pass



