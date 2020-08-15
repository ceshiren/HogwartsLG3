#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 说明 yield 的用法

# yield  python 生成器,如果一个方法里面使用了yield ，这个方法就变成了生成器
def provider():
    for i in range(1, 10):
        print("before")
        yield i  # 相当于 return i，同时记录下当时执行的位置
        print("after")


p = provider()
print(next(p))
print(next(p))
print(next(p))
