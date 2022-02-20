class Animal:
    def __init__(self, name):
        self._name = name   #双下划线连子类也无法访问，相当于protected， 本质上将单下划线都可以访问但是可以暂且当作protected

    def __str__(self):
        return "animal's name is %s"%self._name

    def __len__(self):
        return len(self._name)

    def name(self):
        return self._name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("dog's name is {0}".format(self._name))  #和下等价

    def __str__(self):
        return "dog's name is {0}".format(super(Dog, self)._name)  #同上表示

if __name__ == '__main__':
    dir(Animal)
    print("whether has attribute name: {0}, and get attribute name: {1}".format(hasattr(Animal, 'name'), getattr(Animal, 'name', 404)))
    #不会识别前置下划线，因此直接写变量名即可


