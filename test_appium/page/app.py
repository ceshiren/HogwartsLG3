#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
App 类：
app 常用的方法：比如 启动应用，关闭应用，重启应用，进入首页
"""
from appium import webdriver

from test_appium.page.basepage import BasePage
from test_appium.page.mainpage import MainPage


class App(BasePage):

    def start(self):
        """
        启动应用
        如果driver已经被实例化，就复用已有的driver
        如果driver=None ，就要重新创建一个driver
        """
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待
            self.driver.implicitly_wait(5)
        else:
            # 启动 caps 里面设置的appPackage appActivity
            self.driver.launch_app()
            # 启动 任何一个包和activity
            # self.driver.start_activity()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
