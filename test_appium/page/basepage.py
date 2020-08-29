#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
基类：存放一些最基本的方法，最能用方法
实例化 driver，find, back, home,.....
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        """
        初始化driver
        """
        self.driver = driver

    def find(self, locator):
        logging.info(locator)
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        logging.info("点击")
        self.find(locator).click()

    def find_and_sendkeys(self, locator, value):
        logging.info("输入")

        self.find(locator).send_keys(value)

    def find_by_scroll_and_click(self, text):
        logging.info("滚动查找并点击")
        logging.info(text)

        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find(element).click()

    def get_toasttext(self):
        logging.info("获取toast")
        text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(text)

        return text
