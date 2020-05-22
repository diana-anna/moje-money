import datetime
import copy
from tabulate import tabulate


class Price:
    """This is a class to represent data about the price of an item.

    Attributes
    __________
        listed_price : float
            The amount listed for the item on the receipt.
        tax_percent : float
            The tax percent for that particular item. Write 22 not 0.22.
        is_tax_included : bool, optional
            Whether the tax is already included in the amount.
        quantity : int
            How many of the same items were purchased.
        total:
            The total amount the item costs, including tax.
    """

    def __init__(self, listed_price, tax_percent, is_tax_included=False, quantity=1):
        self.listed_price = listed_price
        self.tax_percent = tax_percent
        self.is_tax_included = is_tax_included
        if not is_tax_included:
            self.total = listed_price * (100 + tax_percent) / 100
        else:
            self.total = listed_price
        self.quantity = quantity
        self.total *= quantity


class Item:
    """This is a class for products on a receipt.

    Attributes
    ----------
        name : str
            The name/description of the item.
        price : :obj:`Price`
        category : str
    """

    def __init__(self, name, price, category=None):
        """The constructor method.

        Parameters
        ----------
        name : str
            The name/description of the item.
        price : :obj:`Price`
        category : str
            The
        """
        self.name = name
        self.price = copy.deepcopy(price)
        self.category = category


class Receipt:
    """
    This is a class to represent receipts.

    Attributes
    ----------
        purchase_date : datetime
            The date printed on the receipt.
        store : str
            The store where the purchase was made.
        items : :obj:`list` of :obj:`Item`
            The list of Items which were bought.
        total : float
            The total amount spent at the store.
        payment_method_key : str
            The key for the payment method that was used with this receipt.
    """

    def __init__(self, purchase_date, store, total, payment_method_key):
        """The constructor method.

        Parameters
        ----------
        purchase_date : datetime
            The date when the receipt was issued.
        store : str
            The name of the store that issued the receipt.
        total : float
            The total amount paid.
        payment_method_key : str
            The key for the payment method that was used with this receipt.
        """
        self.purchase_date = copy.copy(purchase_date)
        self.store = store
        self.items = []
        self.total = total
        self.payment_method_key = payment_method_key

    def add_item(self, entry):
        """Adds an item to the receipt.

        Parameters
        ----------
        entry : Item
            The item to be added to the receipt.
        """
        self.items.append(copy.deepcopy(entry))

    def pretty_print(self):
        """Prints out the entire receipt nicely on the command line."""

        print("\nRECEIPT")
        print("Store:" + self.store)
        print("Date: " + self.purchase_date.isoformat())
        print("Total: $" + str(self.total))
        print("\nITEMS")

        item_printing_list = []
        item_headers = ["Name", "Subtotal", "Quantity", "Total"]
        for item in self.items:
            item_printing_list.append([item.name,
                                       "$" + str(item.price.listed_price),
                                       str(item.price.quantity),
                                       "$" + str(round(item.price.total, 2))])
        print(tabulate(item_printing_list, headers=item_headers))



