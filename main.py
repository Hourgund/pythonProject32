from Entity.milk import Milk
from Entity.orange import Orange
from Entity.bread import Bread
from Container.basket import Basket
from Logic.shop_Assistance import ShopAssistance


def main():
    basket = Basket()

    br = Bread("White", 'Second', 3.0)
    o = Orange(200, 2000, 1.5)
    m = Milk(1, 4.2, 5.5)

    basket.add(br)
    basket.add(m)
    basket.add(o)

    print(f"size = {basket.size}")

    print(basket)

    total = ShopAssistance.calculate_total_price(basket)

    print(f"Total price = {total}")


if __name__ == "__main__":
    main()
