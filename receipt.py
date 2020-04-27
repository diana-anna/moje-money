import datetime


class Item:
    """This is a class for products on a receipt.

    Attributes
    ----------
        name : str
            The name/description of the item.
        amount : float
            The amount listed for the product on the receipt.
        tax_percent : float
            The tax percent for that particular item.
        is_tax_included : bool
            Whether the tax is already included in the amount.
        quantity : int
            How many of the same items were purchased.
    """

    def __init__(self, name, amount, tax_percent, is_tax_included=False, quantity=1):
        """The constructor method.

        Parameters
        ----------
        name : str
            The name/description of the item.
        amount : float
            The amount listed for the item on the receipt.
        tax_percent : float
            The tax percent for that particular item. Write 22 not 0.22.
        is_tax_included : bool, optional
            Whether the tax is already included in the amount.
        quantity : int
            How many of the same items were purchased.
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

    purchase_date : datetime
        The date printed on the receipt.
    store : str
        The store where the purchase was made.
    items : :obj:`list` of :obj:`Item`
        The list of Items which were bought.
    total : float
        The total amount spent at the store.
    """

    def __init__(self, purchase_date, store, total):
        """The constructor method.

        Parameters
        ----------
        purchase_date : datetime
            The date when the receipt was issued.
        store : str
            The name of the store that issued the receipt.
        total : float
            The total amount paid.
        """
        self.purchase_date = purchase_date
        self.store = store
        self.items = []
        self.total = total

    def add_item(self, entry):
        """Adds an item to the receipt.

        Parameters
        ----------
        entry : Item
            The item to be added to the receipt.
        """
        self.items.append(entry)

