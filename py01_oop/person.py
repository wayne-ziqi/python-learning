class Person:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def eat(self, incWeight):
        self.__weight += incWeight

    def run(self, decWeight):
        self.__weight -= decWeight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight


