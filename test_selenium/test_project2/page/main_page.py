from selenium.webdriver.common.by import By
from test_selenium.test_project2.page.add_member import AddMemberPage
from test_selenium.test_project2.page.basepage import BasePage
from test_selenium.test_project2.page.contact_page import ContactPage


class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def go_to_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, "[node-type='addmember']").click()
        return AddMemberPage(self.driver)

    def go_to_contact(self):
        return ContactPage(self.driver)

    def import_contact(self):
        pass
