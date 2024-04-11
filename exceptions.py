class InvalidDataError(Exception):
    """A custom exception class.

    Handles cases when a wrong data format is given.
    E.g. when the values in data are not of type 'FLOAT'.

    Attributes:
         message: contains the error message
    """

    def __init__(self, message="The data has the wrong format. Please make sure "
                               "that the first column is named 'x' and contains all the x-values "
                               "and each other column contains the y-values of the functions "
                               "or test points. All values must be of type 'FLOAT'! "):
        self.message = message


class DataframeTypeError(Exception):
    """A custom exception class.

    Handles cases when the data type is not a pandas dataframe.

    Attributes:
        message: contains the error message
    """

    def __init__(self, message="The data is not a dataframe type. Please ensure that the data is "
                               "primarily loaded correctly using the respective load- method"):
        self.message = message
