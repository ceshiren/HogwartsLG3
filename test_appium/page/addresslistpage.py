#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage
from test_appium.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_text = "添加成员"

    def add_member(self):
        '''
        添加成员
        '''
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click(self.addmember_text)

        return MemberInvitePage(self.driver)
