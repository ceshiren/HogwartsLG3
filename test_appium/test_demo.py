#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# pip install appium-python-client 里面提供的api
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


def get_contact():
    with open("./datas/contacts.yml") as f:
        datas = yaml.safe_load(f)
    return datas


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_sendmess(self):
        inputtext = "helloappiumx"
        el1 = self.driver.find_element_by_id("gq_")
        el1.click()
        el2 = self.driver.find_element_by_id("ffq")
        el2.send_keys("西西")
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView")
        el3.click()
        el4 = self.driver.find_element_by_id("dtv")
        el4.send_keys(inputtext)
        el5 = self.driver.find_element_by_id("dtr")
        el5.click()
        eles = self.driver.find_elements(MobileBy.ID, "dtg")
        # for i in range(num):
        #     print(f"这是第{i}次")
        #     print(eles[i].text)
        name = eles[len(eles) - 1].text
        assert name == inputtext

    @pytest.mark.parametrize('name,gender,phonenum', get_contact())
    def test_addcontact(self, name, gender, phonenum):
        '''
        企业微信：添加联系人测试用例
        前提条件
            已登录状态（ noReset=True）
        打卡用例：
            1、打开【企业微信】应用
            2、进入【通讯录】
            3、点击【添加成员】
            4、在添加成员页面点击【手动输入添加】
            5、输入【姓名】【性别】【手机号】
            6、点击【保存】
            7、验证保存成功
        '''
        # name = "霍格沃兹02"
        # gender = '男'
        # phonenum = "13900000002"

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(phonenum)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        # sleep(2)
        # toast 弹框,打印当前页面的布局结构 ，xml 结构
        # print(self.driver.page_source)
        toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == toasttext

    def test_delcontact(self):
        name = "霍格沃兹04"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq_").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ffq").send_keys(name)
        sleep(2)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        beforenum = len(eles)
        if beforenum < 2:
            print("没有可删除的人员")
            return

        eles[1].click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq0").click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='编辑成员']").click()
        # self.driver.find_element(MobileBy.XPATH, f"//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='确定']").click()
        sleep(2)
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        afternum = len(eles1)
        assert afternum == beforenum - 1
