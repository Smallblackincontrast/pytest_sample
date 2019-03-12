#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_fixt.py
# @Author  : Ruanzhe
# @Date  : 2019/2/11  10:10


def func(x):
    return x+1


def test_answer():
    assert func(3) == 4
