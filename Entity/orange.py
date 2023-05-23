class Orange:
    def __init__(self, diameter=100, vitamin=1000, cost=0):
        self.__diameter = diameter
        self.__vitamin = vitamin
        self.__cost = cost

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        self.__diameter = diameter

    @property
    def vitamin(self):
        return self.__vitamin

    @vitamin.setter
    def vitamin(self, vitamin):
        self.__vitamin = vitamin

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    def __str__(self):
        return (f"Orange: Diameter = {self.__diameter},"
                f"Vitamin C = {self.__vitamin},"
                f"Cost = ${self.__cost}")