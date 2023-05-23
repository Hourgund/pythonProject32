from Entity.milk import Milk
from Entity.orange import Orange
from Entity.bread import Bread
from Container.basket import Basket


def main():
    basket = Basket()

    br = Bread()
    o = Orange()
    m = Milk(1, 4.2, 5.5)

    basket.add(br)
    basket.add(m)
    basket.add(o)

    print(f"size = {basket.size}")

    print(basket)


if __name__ == "__main__":
    main()
