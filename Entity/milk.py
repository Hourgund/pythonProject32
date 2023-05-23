from Entity.product import Product


class Milk(Product):
    def __init__(self, volume=0, fat=0, price=0):
        super().__init__(price)
        self.__volume = volume
        self.__fat = fat

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def fat(self):
        return self.__fat

    @fat.setter
    def fat(self, fat):
        self.__fat = fat

    def __str__(self):
        return (f"Milk: Volume = {self.__volume},"
                f" Fat = {self.__fat},"
                f" Price = ${self.price}")
