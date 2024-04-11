import pandas as pd
from exceptions import DataframeTypeError


class DfConstructor:
    """A class to construct and manage pandas dataframes.

    Methods:
        construct_df_from_file: construct a dataframe from a csv-file by a given filepath.
        construct_validation_df: construct a specific dataframe for testpoint validation.
    """

    def construct_df_from_file(self, filepath):
        """constructs a dataframe from a csv-file by a given filepath

        :param filepath: the filepath to the csv-file
        :return: a pandas dataframe
        """
        try:
            # construct dataframe
            df = pd.read_csv(filepath)

            # check if dataframe is constructed
            if not isinstance(df, pd.DataFrame):
                raise DataframeTypeError("Something went wrong "
                                         "while constructing the dataframe")
            return df

        except FileNotFoundError:
            raise FileNotFoundError("File or path does not exist!")

    def construct_validation_df(self):
        """constructs a dataframe with specific column names
        that will be used for the testpoint-validation

        :return: validation dataframe
        """
        try:
            # construct validation dataframe
            validation_df = pd.DataFrame(columns=["X", "Y", "Delta Y", "Ideal function name"])

            # check if dataframe is constructed
            if not isinstance(validation_df, pd.DataFrame):
                raise DataframeTypeError("Something went wrong "
                                         "while constructing the dataframe")
            return validation_df

        except Exception as e:
            print(f"Error: {e}")
