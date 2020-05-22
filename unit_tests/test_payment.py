from unittest import TestCase
import json
from budget_options import Payment


class TestPaymentSmall(TestCase):

    def setUp(self):
        self.payment = Payment()


class TestPaymentMedium(TestCase):

    def setUp(self):
        self.payment = Payment()
        self.payment.add_option("Capital One")
        self.payment.add_option("Bank of America")
        self.payment.add_option("American Express")
        self.payment.add_option("Chase Freedom")
        self.payment.add_option("Chase Sapphire")


class TestChanges(TestPaymentSmall):

    def test_add_payment_option(self):
        self.payment.add_option("Bank of America")
        self.assertEqual(self.payment.options, ["Cash", "Bank of America"])

    def test_delete_option(self):
        self.payment.del_option("Cash")
        self.assertEqual(self.payment.options, [])

    def test_rename_payment_option(self):
        self.payment.rename_option("Cash", "Dollars")
        self.assertEqual(self.payment.options, ["Dollars"])


class TestJSON(TestPaymentMedium):

    def test_to_json(self):
        self.payment.save_to_json("example_payments.json")
        return True
