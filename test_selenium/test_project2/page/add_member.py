from selenium.webdriver.common.by import By

from test_selenium.test_project2.page.basepage import BasePage
from test_selenium.test_project2.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID, "username")


    def add_member(self, name = "ez"):
        """
        添加成员操作
        :return:
        """
        self.driver.find_element(*self._username).send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("01")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13188881111")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

        return ContactPage(self.driver)

