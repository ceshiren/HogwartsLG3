#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_a():
    print("aaaa")


def test_b():
    assert False


@pytest.mark.flaky(reruns=5)
def test_example():
    import random
    # assert random.choice([True, False])
    assert False


def test_assume():
    pytest.assume(1 == 4)
    pytest.assume(2 == 4)
    pytest.assume(3 == 4)
    pytest.assume(4 == 4)
    pytest.assume(5 == 4)
    # assert 1 == 4
    # assert 2 == 4
