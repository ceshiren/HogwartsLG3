#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

import sys

print(sys.path)
sys.path.append("/Users/juanxu/Documents/霍格沃兹培训/01ceshiren实战项目/HogwartsLG3/testing")
from demo1.search import Search


def test_search1(connDB):
    s = Search()
    print("search1")


def test_search2(connDB):
    print("search2")
