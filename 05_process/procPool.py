#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/21 22:17
# @Author   : Wayne Qi
# @FileName : procPool.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

from multiprocessing import Pool
import os, time, random


def time_task(id):
    print("run process: {0} start".format(id))
    start = time.time()
    time.sleep(random.random() *3)
    end = time.time()
    print("process Nom.%d executing time: %0.2f"%(id,end - start))

if __name__ == '__main__':
    print("parent process id: {0}".format(os.getpid()))
    pool = Pool(4)  #最多可执行4个进程，默认cpu的核心数
    for i in range(5):
        pool.apply_async(time_task, args=(i,))
    #调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    print("waiting for all subprocess")
    pool.close()
    pool.join()
    print("done")

