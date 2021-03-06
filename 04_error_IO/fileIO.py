#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/20 22:08
# @Author   : Wayne Qi
# @FileName : fileIO.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com
import logging



LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # typo不用管,否则无法写入到文件，参数不对
#DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='exceptions.log', level=logging.DEBUG, format=LOG_FORMAT)#, datefmt=DATE_FORMAT)

try:
    f = open("日志处理.md", 'r')
    content = f.read()
except FileNotFoundError as e:
    logging.info(e)
except UnicodeError as e:
    logging.info(e)
finally:
    if f:
        f.close()

#上述的try可等价为，读取图片视频等用二进制rb打开
with open("日志处理.assets/1063221-20170511145312144-488305597.png", 'rb') as f:
    f.read()
     #datadict = pickle.load(f, encoding='latin1')

with open("日志处理.md", 'r', encoding='gbk', errors='ignore') as f:
    f.read()
print('End')

#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

with open("日志处理.md", 'r', encoding='gbk', errors='ignore') as f:
    line = f.readline()
    while line:
        #
        # procedure
        #
        line = f.readline()

