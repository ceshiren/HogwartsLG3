#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from test_appium.page.app import App


def get_contact():
    with open("../datas/contacts.yml") as f:
        datas = yaml.safe_load(f)
    return datas


class TestWexin:
    def setup(self):
        """
        启动app
        """
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum', get_contact())
    def test_addcontact(self, name, gender, phonenum):
        mypage = self.main.goto_addresslist().add_member().addmember_menual() \
            .edit_name(name).edit_gender(gender).edit_phonenum(phonenum) \
            .click_save()

        mytoast = mypage.get_toast()
        assert mytoast == '添加成功'
