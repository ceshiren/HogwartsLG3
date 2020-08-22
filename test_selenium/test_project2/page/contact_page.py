from selenium.webdriver.common.by import By

from test_selenium.test_project2.page.basepage import BasePage


class ContactPage(BasePage):
    def go_to_add_member(self):
        from test_selenium.test_project2.page.add_member import AddMemberPage

        return AddMemberPage()

    def add_department(self):
        pass

    def get_member(self):
        # element = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        # self.wait_for_clickable(element)
        memberlist = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

        return [member.text for member in memberlist]