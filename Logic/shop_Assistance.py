from Entity.milk import Milk
from Entity.orange import Orange
from Entity.bread import Bread
from Container.basket import Basket


class ShopAssistance:
    @staticmethod
    def calculate_total_price(basket):
        if isinstance(basket, Basket) and basket.size != 0:
            total = 0
            for i in range(basket.size):
                product = basket.get_product(i)

                if isinstance(product, Milk):
                    total += product.money

                if isinstance(product, Bread):
                    total += product.price

                if isinstance(product, Orange):
                    total += product.cost

            return total
