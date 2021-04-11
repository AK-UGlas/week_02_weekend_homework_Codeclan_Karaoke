import unittest
from src.drink import Drink
from src.guest import Guest
from src.bar import Bar

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Jimmy's Lager", 1.50, 20)
        
    def test_drink_has_name(self):
        self.assertEqual("Jimmy's Lager", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(1.50, self.drink.price)

    def test_drink_has_alcohol_lvl(self):
        self.assertEqual(20, self.drink.alcohol_lvl)