import json


class EnhancedList:
    """A class to help build the classes to keep track of user options.

    This class is used to build other classes, such as a class for keeping
    track of a user's payment methods, and a class to keep track of a user's
    self-defined budgeting categories.

    Attributes
    ----------
    options : :obj:`list`of str
    """

    def __init__(self, input_path=None):
        """Constructor method.

        Creates a new Payment object from a JSON file. If no file is specified,
        then a new object is created with only an empty dictionary.

        Parameters
        ----------
        input_path : str, optional
            The path to the JSON file that contains the user's options.
        """
        if input_path is None:
            self.options = []
        else:
            with open(input_path) as input_file:
                self.options = json.loads(input_file)

    def add_option(self, option_name):
        """Adds an option.

        Parameters
        ----------
        option_name : str
            The full name of the option.
        """
        self.options.append(option_name)

    def del_option(self, option_name):
        """Deletes an option.

        Parameters
        ----------
        option_name : str
            The option to be deleted.
        """
        option_index = self.options.index(option_name)
        self.options.pop(option_index)

    def rename_option(self, old_name, new_name):
        """Renames an option.

        Parameters
        ----------
        old_name : str
            The old name of the option.
        new_name : str
            The new name of the option.
        """
        self.del_option(old_name)
        self.add_option(new_name)

    def save_to_json(self, out_path):
        """Saves the options to a JSON file.

        Parameters
        ----------
        out_path : str
            The path to the JSON file that will store the options.
        """
        with open(out_path, 'w') as out_file:
            json.dump(self.options, out_file)


class Payment(EnhancedList):
    """A class to keep track of a user's payment methods.

    Attributes
    ----------
        options : :obj:`list`of str
    """

    def __init__(self, input_path=None):
        super().__init__(input_path)
        if input_path is None:
            self.options.append("Cash")


class Categories(EnhancedList):
    """A class to keep track of a user's budgeting categories.

    Attributes
    ----------
        options : :obj:`list`of str
    """
