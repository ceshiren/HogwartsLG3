#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_case1(connDB):
    print("case1")


class TestDemo:
    def test_a(self, connDB):
        print("testa")

    def test_b(self, connDB):
        print("testb")


class TestDemo1:
    def test_a(self, connDB):
        print("testa")

    def test_b(self, connDB):
        print("testb")
