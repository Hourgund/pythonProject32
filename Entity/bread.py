class Orange:
    def __init__(self, color='black', flour="first", price=0):
        self.__color = color
        self.__flour = flour
        self.__price = price

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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return (f"Bread: Color = {self.__color},"
                f"Flour = {self.__flour},"
                f"Price = {self.__price}")