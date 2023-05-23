class Milk:
    def __init__(self, volume=0, fat=0, money=0):
        self.__volume = volume
        self.__fat = fat
        self.__money = money

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

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    def __str__(self):
        return (f"Milk: Volume = {self.__volume},"
                f"Fat = {self.__fat},"
                f"Money = {self.__money}")