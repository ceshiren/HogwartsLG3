#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml
import sys
from pythoncode.calculator import Calculator
print(sys.path)
sys.path.append('..')

"""
pytest 命名规则 
文件名：以 test_开头 （test_*.py）
类名：以 Test 开头 
方法名：以test_开头
"""


class TestCalc:
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("结束计算")

    @pytest.mark.add
    # @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, get_datas):
        '''
        测试相加
        '''
        print("测试相加")
        # calc = Calculator()
        result = get_calc.add(get_datas[0], get_datas[1])
        assert get_datas[2] == result

    @pytest.mark.parametrize('a,b,expect', [
        (0.1, 0.1, 0.2),
        (0.1, 0.2, 0.3),
    ])
    def test_add_float(self, get_calc, a, b, expect):
        result = round(get_calc.add(a, b), 2)
        assert expect == result
