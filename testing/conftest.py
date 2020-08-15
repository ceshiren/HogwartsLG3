#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import List

import pytest
import yaml

from pythoncode.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 修改编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# scope = session  整个session域只执行一次。
@pytest.fixture(scope='session')
def connDB():
    print("连接数据库")
    yield
    print("断开数据库连接")


@pytest.fixture(scope="class")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


# 读取测试数据
def get_datas():
    # 获取测试数据的绝对路径
    mydatapath = os.path.dirname(__file__) + "/datas/calc.yml"
    with open(mydatapath, encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]


@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])
def get_datas(request):
    return request.param
