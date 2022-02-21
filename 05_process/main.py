import process as myproc
from multiprocessing import Process
import os

if __name__ == '__main__':
    #不适用fork创建的进程只能在main函数中创建进程
    print("parent process {0}".format(os.getpid()))
    proc1 = Process(target=myproc.process1, args=('process1',)) #传入执行函数和执行参数
    proc1.start()
    proc1.join()  # 与父进程会和