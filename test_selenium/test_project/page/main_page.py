from selenium.webdriver.common.by import By

from test_selenium.test_project.page.add_member_page import AddMember
from test_selenium.test_project.page.base_page import BasePage
from test_selenium.test_project.page.contact_page import ContactPage
from selenium import webdriver

class MainPage(BasePage):
    _memberAdd_phone = ""

    _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def go_to_contact(self):
        return ContactPage(self.driver)

    def go_to_add_member(self):

        self.driver.find_element(By.CSS_SELECTOR, "[node-type='addmember']").click()
        return AddMember(self.driver)