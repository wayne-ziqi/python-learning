# 生成素数的方法
import functools
import time


def genOdd():
    n = 1
    while True:
        n += 2
        yield n


def divisible(n):
    return lambda x: x % n > 0


def genPrime():
    yield 2
    it = genOdd()
    while True:
        n = next(it)
        yield n
        it = filter(divisible(n), it)

itPrime = genPrime()
for i in range(100):
    print(next(itPrime))

def createCounter():
    sumNum = 0
    def counter():
        nonlocal  sumNum
        sumNum += 1
        return sumNum

    return counter

# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        res = fn(*args, **kw)
        end = time.time()
        print("executing time: %.2f" %(end - start))
        return res
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x + y

fast(1,2)