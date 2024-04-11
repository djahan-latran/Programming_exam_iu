import unittest
import pandas as pd
from df_constructor import DfConstructor


class TestDfConstructor(unittest.TestCase):
    """An unittest class to test methods of the DfConstructor class

    Methods:
        test_construct_df_from_file_valid: tests if FileNotFoundError is raised
        test_construct_validation_df: tests if a valid dataframe is constructed
    """

    def test_construct_df_from_file_valid(self):
        """By using a file that does not exist this method checks if
        the FileNotFoundError is raised properly.
        """
        # create filepath that does not exist
        filepath = "datensaetze/filedoesnotexist.csv"

        dataframe = DfConstructor()

        # try to raise Error
        with self.assertRaises(FileNotFoundError):
            dataframe.construct_df_from_file(filepath)

    def test_construct_validation_df(self):
        """By using the construct_validation_df method of DfConstructor class,
        this method checks if the result is a valid dataframe object.
        """
        # create a validation dataframe
        df = DfConstructor()
        validation_df = df.construct_validation_df()

        # check if validation_df is of type 'dataframe'
        self.assertIsInstance(validation_df, pd.DataFrame)


if __name__ == "__main__":
    unittest.main()
