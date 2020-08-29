#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslistpage import AddressListPage
from test_appium.page.basepage import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addresslist_elemenet = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find_and_click(self.addresslist_elemenet)
        return AddressListPage(self.driver)
