import unittest
from df_constructor import DfConstructor


class TestDfConstructor(unittest.TestCase):

    def test_construct_df_from_file_valid(self):
        filepath = "datensaetze/filedoesnotexist.csv"
        dataframe = DfConstructor()

        with self.assertRaises(FileNotFoundError):
            dataframe.construct_df_from_file(filepath)

    def test_construct_validation_df(self):
        df = DfConstructor()
        validation_df = df.construct_validation_df()

        self.assertIsNotNone(validation_df)



if __name__ == '__main__':
    unittest.main()