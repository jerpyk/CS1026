# 1
class Fruit:
    def __init__(self, clr="", shp="", tst=""):
        self._colour = clr
        self._shape = shp
        self._taste = tst

    def descriptor(self):
        return self._colour + "," + self._shape + "," + self._taste


class Banana(Fruit):
    def __init__(self, clr="", shp="", tst=""):
        super().__init__(clr, shp, tst)


class Apple(Fruit):
    def __init__(self, clr="", shp="", tst="", type=""):
        super().__init__(clr, shp, tst)
        self._type = type

    def setType(self, value):
        self._type = value

    def descriptor(self):
        return super().descriptor() + "," + self._type


afruit = Fruit("green", "round", "sweet")
print("A fruit: ", afruit.descriptor())
bn = Banana("yellow", "long", "soft and sweet")
print("A banana: ", bn.descriptor())

app1 = Apple("red", "round", "sweet and crunchy")
print("An apple: ", app1.descriptor())
app1.setType("Gala")
print("A particular apple: ", app1.descriptor())


# 2
class Automobile:
    def __init__(self, ndoors=0, clr=""):
        self._doors = ndoors
        self._colour = clr

    def printDoors(self):
        # self._doors instead of ndoors
        return "Number of doors is: " + str(self._doors)

    def printColour(self):
        return "Colour is: " + self._colour

    def display(self):
        return "Car is: " + str(self._doors) + " doors," + self._colour


class SportsCar(Automobile):
    # add parameters ndoors, clr, and eng
    def __init__(self, ndoors=0, clr="", eng=0):
        super().__init__(ndoors, clr)
        self._engine = eng

    def display(self):
        return "Car is: " + str(self._doors) + " doors," + self._colour + ", with " + str(self._engine) + "hp"


auto = Automobile(4, "black")
sports = SportsCar(4, "white", 50)
print(auto.display())
print(sports.display())
print(sports.printColour())
