import unittest
from datetime import date
from receipt import Price, Item, Receipt


class TestReceipt(unittest.TestCase):

    def setUp(self):
        test_date = date(2020, 5, 1)
        self.test_receipt = Receipt(test_date, "Home Depot", 55.19, "DISC")
        price_orchid = Price(22.98, 9)
        orchid = Item("Orchid", price_orchid)
        self.test_receipt.add_item(orchid)
        price_lamp_holder = Price(3.78, 9)
        lamp_holder = Item("Lamp Holder", price_lamp_holder)
        self.test_receipt.add_item(lamp_holder)
        price_compressed_air = Price(5.98, 9)
        compressed_air = Item("Compressed Air Can", price_compressed_air)
        self.test_receipt.add_item(compressed_air)
        price_softener = Price(5.97, 9, quantity=3)
        softener_pellets = Item("Softener Pellets", price_softener)
        self.test_receipt.add_item(softener_pellets)

    def test_print(self):
        self.test_receipt.pretty_print()
        return True
