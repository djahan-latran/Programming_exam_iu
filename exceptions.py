class InvalidDataError(Exception):

    def __init__(self, message="The data has the wrong format. Please make sure "
                               "that the first column is named 'x' and contains all the x-values "
                               "and each other column contains the y-values of the functions "
                               "or test points. All values must be of type 'FLOAT'! "):
        self.message = message


class DataframeTypeError(Exception):

    def __init__(self, message="The data is not a dataframe type. Please ensure that the data is "
                               "primarily loaded correctly using the respective load- method"):
        self.message = message
