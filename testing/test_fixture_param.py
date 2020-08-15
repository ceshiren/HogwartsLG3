#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=[('tom', 123456), ('jerry', 654321)],
                ids=['用户tom', '用户jerry'])
def login(request):
    return request.param


def test_case1(login):
    print(f"username: {login[0]} ,password:{login[1]}")
    print("case1")
