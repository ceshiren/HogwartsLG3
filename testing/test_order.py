#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.last
def test_zfoo():
    assert True


@pytest.mark.second
def test_foo():
    assert True


@pytest.mark.first
def test_bar():
    assert True


@pytest.mark.second_to_last
def test_afoo():
    assert True
