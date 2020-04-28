from unittest import TestCase
from payment import Payment


class TestPayment(TestCase):

    def setUp(self):
        self.payment = Payment()


class TestChanges(TestPayment):

    def test_add_payment_option(self):
        self.payment.add_option("BOA", "Bank of America")
        self.assertEqual(self.payment.options, {"CASH": "Cash", "BOA": "Bank of America"})

    def test_delete_option(self):
        self.payment.del_option("CASH")
        self.assertEqual(self.payment.options, {})

    def test_rename_payment_option(self):
        self.payment.rename_option("BOA", "BOA")
        self.assertEqual(self.payment.options, {"CASH": "Cash", "BOA": "BOA"})
