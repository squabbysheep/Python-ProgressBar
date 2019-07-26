#!/usr/bin/env python
# coding:utf-8
"""
@Name   : one.py
@Author : myLove
@Email  : 17859717522@163.com
@Time   : 2019/7/26
"""
# 范例1：基本范例
import time
from tqdm import tqdm

for i in tqdm(range(100)):
    time.sleep(0.1)
