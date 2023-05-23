from Entity.product import Product


class Orange(Product):
    def __init__(self, diameter=100, vitamin=1000, price=0):
        super().__init__(price)
        self.__diameter = diameter
        self.__vitamin = vitamin

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

    def __str__(self):
        return (f"Orange: Diameter = {self.__diameter},"
                f" Vitamin C = {self.__vitamin},"
                f" Price = ${self.price}")
