#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/20 20:40
# @Author   : Wayne Qi
# @FileName : error.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # typo不用管,否则无法写入到文件，参数不对
#DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='exceptions.log', level=logging.DEBUG, format=LOG_FORMAT)#, datefmt=DATE_FORMAT)

try:
    print("try ...")
    r = 10 / int('0')
    k = 10 / 0
    print('result = ', r)
except ZeroDivisionError as e:  # 需要注意的是，如果某个错误是先前出现过的except的子类，则该子类会被之前的except捕获而不会被子类捕获
    print("ZeroDivisionError except: ", e)
    # logging.info("Zero Division Error")
    logging.info(e)

except ValueError as e:
    print("ValueError except:", e)
except UnicodeError as e:
    print("except: ", e)
#在except中用raise可以转换错误类型
except OverflowError:
    raise ValueError #虽然逻辑上不对
else:
    print("no error")
# 如果try出错则转入except执行，如果有finally则接着执行finally
finally:
    print("finally...")

print('End')

#自定义错误类,需要继承自子类

class FooError(ValueError):
    pass

def foo(s):
    n = int(s);
    if n == 0:
        logging.info(ZeroDivisionError)
        raise FooError("invalid value: {0}".format(s))
    return 10/n
foo(0)


