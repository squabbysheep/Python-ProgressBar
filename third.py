#!/usr/bin/env python
# coding:utf-8
"""
@Name   : third.py
@Author : myLove
@Email  : 17859717522@163.com
@Time   : 2019/7/26
"""
# 范例3：手动更新
import time
from tqdm import tqdm

with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)  # 手动更新
