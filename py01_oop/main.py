# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from person import Person
from functools import reduce


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# generator function
def triangles():
    L = [1]
    if (len(L) == 1): yield L
    while True:
        tmp = [0] + L + [0]
        L = [tmp[i] + tmp[i + 1] for i in range(len(L) + 1)]
        yield L


def str2float(s):
    idxDoc = s.find('.')
    s1 = s[0:idxDoc]
    s2 = s[idxDoc + 1:]
    if (idxDoc == 0): s1 = '0'
    pintegar = int(s1)
    ldecimal = [int(c) for c in s2[::-1]]
    pdecimal = reduce(lambda x, y: x * 0.1 + y, ldecimal)
    return 0.1 * pdecimal + pintegar


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # iniName, weight = input("input name and age").split(',')
    # XiaoMing = person.Person(iniName, float(weight))
    # XiaoMing.eat(10)
    # XiaoMing.run(20)
    # print("体重：%d, 姓名: %s" %(XiaoMing.weight(), XiaoMing.name()))
    # d = {'x': 'A', 'y': 'B', 'z': 'C'}
    # l1 = [k + '=' + v for k, v in d.items()]
    # print(l1)
    # L = ["Hello", "1Bm", 18]
    # L_lower = [s.lower() for s in L if isinstance(s, str)]
    # print(L_lower)

    # g = triangles()
    # for i in range(10):
    #     print(next(g))

    inFormalList = ['dsfaAaf', 'SDFDA', 'GREAgd', 'F']

    iterName = map(str.lower, inFormalList)

    formalList = [(s[0].upper() + s[1:len(s)] if (len(s) > 1) else s[0].upper) for s in list(iterName)]

    print(formalList)

    strFloat = '123.23'

    print(str2float(strFloat))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
