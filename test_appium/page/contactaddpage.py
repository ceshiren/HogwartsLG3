#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from test_appium.page.memberinvitepage import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    name_element = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText')
    gender_element = (MobileBy.XPATH, "//*[@text='男']")
    male_element = (MobileBy.XPATH, "//*[@text='男']")
    female_element = (MobileBy.XPATH, "//*[@text='女']")
    phonenum_element = (MobileBy.ID, "com.tencent.wework:id/emh")
    save_element = (MobileBy.ID, "com.tencent.wework:id/gq7")

    def edit_name(self, name):
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        self.find_and_sendkeys(self.name_element, name)
        return self

    def edit_gender(self, gender):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # if gender == '男':
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.find_and_click(self.gender_element)
        if gender == '男':
            self.find_and_click(self.male_element)
        else:
            self.find_and_click(self.female_element)
        return self

    def edit_phonenum(self, phonenum):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(phonenum)
        self.find_and_sendkeys(self.phonenum_element, phonenum)
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        self.find_and_click(self.save_element)
        from test_appium.page.memberinvitepage import MemberInvitePage
        return MemberInvitePage(self.driver)
