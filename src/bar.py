class Bar:
    """Implementation of a Bar class, inspired by Pub.py in CodeClan
        TDD lab (week_02): https://github.com/GiulianoDerosas/TestingLabDay8
        written by Giuliano Derosas & Allen Kelly"""

    def __init__(self):
        self.drinks = {}
        self.till = 0

    def add_to_till(self, amount):
        self.till += amount

    def stock_bar(self, drink, stock_lvl):
        if drink in self.drinks:
            self.drinks[drink] += stock_lvl
        else:
            self.drinks[drink] = stock_lvl

    def drink_in_stock(self, drink):
        if drink in self.drinks and self.drinks[drink] > 0:
                return True

        return False

    def sell_drink(self, guest, drink):
        if guest.can_afford_item(drink.price) and self.drink_in_stock(drink):
            guest.pay(drink.price)
            self.add_to_till(drink.price)
            self.drinks[drink] -= 1


    