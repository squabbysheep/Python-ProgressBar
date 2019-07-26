#!/usr/bin/env python
# coding:utf-8
"""
@Name   : second.py
@Author : myLove
@Email  : 17859717522@163.com
@Time   : 2019/7/26
"""
# 范例2：增加描述
import time
from tqdm import tqdm

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(0.25)
    pbar.set_description("Processing %s" % char)
