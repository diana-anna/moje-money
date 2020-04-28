import json


class Payment:
    """A class to keep track of payment methods for users.

    Attributes
    ----------
    options : :obj:`dict`of {str:str}
    """

    def __init__(self, input_path=None):
        """Constructor method.

        Creates a new Payment object from a JSON file. If no file is specified, then
        a new object is created with only a cash option.

        Parameters
        ----------
        input_path : str, optional
            The path to the JSON file that contains the payment options
        """
        if input_path is None:
            self.options = {"CASH": "Cash"}
        else:
            with open(input_path) as input_file:
                self.options = json.loads(input_file)

    def add_option(self, option_key, option_name):
        """Adds a payment option.

        Parameters
        ----------
        option_key : str
            A short representation of the payment option.
        option_name : str
            The full name of the payment option.
        """
        self.options[option_key] = option_name

    def del_option(self, option_key):
        """Deletes a payment option.

        Parameters
        ----------
        option_key : str
            The shorthand representation of the payment option to be deleted.
        """
        del self.options[option_key]

    def rename_option(self, option_key, new_name):
        """Renames a payment option.

        Parameters
        ----------
        option_key : str
            The shorthand representation of the payment option to be renamed.
        new_name : str
            The new name of the specified payment option.
        """
        self.options[option_key] = new_name

    def save_to_json(self, out_path):
        """Saves the payment options to a JSON file.

        Parameters
        ----------
        out_path : str
            The path to the JSON file that will store the payment options.
        """
        with open(out_path, 'w') as out_file:
            json.dumps(self.options, out_file)
