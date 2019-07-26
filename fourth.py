#!/usr/bin/env python
# coding:utf-8
"""
@Name   : fourth.py
@Author : myLove
@Email  : 17859717522@163.com
@Time   : 2019/7/26
"""
# Appendix：手工实现循环进度条
import sys
import time


# 进度条函数
def progress_bar(num, total):
    rate = float(num) / total
    ratenum = int(100 * rate)
    r = '\r[{}{}]{}%'.format('*' * ratenum, ' ' * (100 - ratenum), ratenum)  # 一定要使用'\r'这个转义字符（回到行首）
    sys.stdout.write(r)  # 输出
    sys.stdout.flush()  # 刷新


i, n = 0, 100
for i in range(n):
    time.sleep(0.1)
    progress_bar(i + 1, n)
