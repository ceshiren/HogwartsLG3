#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml
import sys

print(sys.path)
sys.path.append('..')
from pythoncode.calculator import Calculator

"""
pytest 命名规则 
文件名：以 test_开头 （test_*.py）
类名：以 Test 开头 
方法名：以test_开头
"""


# 读取测试数据
def get_datas():
    with open('./datas/calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]


class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        '''
        测试相加
        '''
        print("测试相加")
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', [
        (0.1, 0.1, 0.2),
        (0.1, 0.2, 0.3),
    ])
    def test_add_float(self, a, b, expect):
        result = round(self.calc.add(a, b), 2)
        assert expect == result
