# 1
class Car:
    def __init__(self):
        self._type = ""

    def setType(self, type):
        self._type = type

    def getType(self):
        return self._type


c1 = Car()
c2 = Car()
c3 = Car()

c1.setType("Toyota")
c2.setType("Honda")
c3.setType("Nissan")

print(c1.getType())
print(c2.getType())
print(c3.getType())


# 2
class Coffee:
    def __init__(self):
        self._cost = 2.50

    def __add__(self, other):
        if isinstance(other, Cream):
            return "Yum"


class Cream:
    def __init__(self):
        self._percentage = 10


coffee = Coffee()
cream = Cream()

print(coffee + cream)


# 3
class CashRegister:
    # add the self argument
    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price

    # total argument not needed
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    # total argument not needed
    def getTotal(self):
        return self._totalPrice
