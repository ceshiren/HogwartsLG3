#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from test_appium.page.contactaddpage import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_menul_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def addmember_menual(self):
        from test_appium.page.contactaddpage import ContactAddPage
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmember_menul_element)
        return ContactAddPage(self.driver)

    def get_toast(self):
        # toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        toasttext = self.get_toasttext()
        return toasttext
