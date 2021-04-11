import unittest
from src.bar import Bar
from src.guest import Guest
from src.drink import Drink
from src.song import Song

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar()
        self.song = Song("Thunderstruck", "AC/DC", 292, 1990, "Rock")
        self.patron = Guest("Allen", 25, self.song)
        self.lager = Drink("Jimmy's Lager", 1.50, 20)
        self.wine = Drink("Red wine", 3.50, 25)
        self.bar.stock_bar(self.lager, 10)

    # test methods   
    def test_add_money_to_till(self):
        self.bar.add_to_till(10)
        self.assertEqual(10, self.bar.till)
    
    def test_add_drink_to_stock(self):
        self.bar.stock_bar(self.wine, 8)
        self.assertEqual(8, self.bar.drinks[self.wine])

    def test_drink_in_stock(self):
        self.assertTrue(self.bar.drink_in_stock(self.lager))

    def test_drink_out_of_stock(self):
        self.bar.stock_bar(self.wine, 0)
        self.assertFalse(self.bar.drink_in_stock(self.wine))

    def test_drink_not_on_drinks_menu(self):
        self.assertFalse(self.bar.drink_in_stock(self.wine))

    #integration test
    def test_sell_drink_to_guest(self):
        self.bar.sell_drink(self.patron, self.lager)
        self.assertEqual(1.50, self.bar.till)
        self.assertEqual(9, self.bar.drinks[self.lager])
        self.assertEqual(23.50, self.patron.wallet)


