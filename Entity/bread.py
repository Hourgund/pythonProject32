from Entity.product import Product


class Bread(Product):
    def __init__(self, color='black', flour="first", price=0):
        super().__init__(price)
        self.__color = color
        self.__flour = flour

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def flour(self):
        return self.__flour

    @flour.setter
    def flour(self, flour):
        self.__flour = flour

    def __str__(self):
        return (f"Bread: Color = {self.__color},"
                f" Flour = {self.__flour},"
                f" Price = ${self.price}")
