import datetime


class Item:
    """This is a class for products on a receipt.

    :param name: The name/description of the item.
    :type name: string
    :param amount: The amount listed for the product on the receipt.
    :type amount: float
    :param tax_percent: The tax percent for that particular item.
    :type tax_percent: float
    :param is_tax_included: Whether the tax is already included in the amount
    :type is_tax_included: boolean, optional
    :param quantity: How many of the same items were purchased.
    :type: int, optional
    """

    def __init__(self, name, amount, tax_percent, is_tax_included=False, quantity=1):
        """The constructor method.
        """
        self.name = name
        self.is_tax_included = is_tax_included
        self.quantity = quantity
        if not is_tax_included:
            self.subtotal = amount
            self.tax_percent = tax_percent
            self.total = amount * (100 + tax_percent) / 100

        else:
            self.total = amount
            self.tax_percent = tax_percent
            self.subtotal = amount * 100 / (100 + tax_percent)


class Receipt:
    """
    This is a class to represent receipts.

    :param purchase_date: The date printed on the receipt.
    :type: datetime
    :param store: The store where the purchase was made.
    :type: string
    :param items: The list of Items which were bought.
    :type: list
    :param total: The total amount spent at the store.
    :type: float, optional
    """

    def __init__(self, purchase_date, store, total=0):
        self.purchase_date = purchase_date
        self.store = store
        self.items = []
        self.total = total

    def add_item(self, entry):
        """
        Add an item to the receipt.

        :param entry: The entry which you wish to add to the receipt.
        :type entry: Item
        """
        self.items.append(entry)

