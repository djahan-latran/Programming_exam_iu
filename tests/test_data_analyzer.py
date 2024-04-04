import unittest
import pandas as pd
from data_analyzer import DataAnalyzer


class TestDataAnalyzer(unittest.TestCase):

    test_analyzer = DataAnalyzer(train_folder="test_files",
                                 train_file="test_df.csv",
                                 ideal_folder="test_files",
                                 ideal_file="test_df.csv",
                                 test_folder="test_files",
                                 test_file="test_df.csv"
                                 )

    def test_load_train_data_valid(self):
        test_dataframe = self.test_analyzer.load_train_data()

        self.assertIsInstance(test_dataframe, pd.DataFrame)

    def test_load_ideal_data_valid(self):
        test_dataframe = self.test_analyzer.load_ideal_data()

        self.assertIsInstance(test_dataframe, pd.DataFrame)

    def test_load_test_data_valid(self):
        test_dataframe = self.test_analyzer.load_test_data()

        self.assertIsInstance(test_dataframe, pd.DataFrame)

    def test_find_bestfit_valid_dict(self):
        self.test_analyzer.load_train_data()
        self.test_analyzer.load_ideal_data()
        test_dict = self.test_analyzer.find_bestfit()

        self.assertIsNotNone(test_dict)
        self.assertIsInstance(test_dict, dict)

    def test_find_bestfit_valid_train_data(self):

        self.test_analyzer.load_train_data()
        self.test_analyzer.train_data = None
        self.test_analyzer.load_ideal_data()

        with self.assertRaises(AttributeError):
            self.test_analyzer.find_bestfit()

    def test_find_bestfit_valid_ideal_data(self):

        self.test_analyzer.load_ideal_data()
        self.test_analyzer.ideal_data = None
        self.test_analyzer.load_train_data()

        with self.assertRaises(AttributeError):
            self.test_analyzer.find_bestfit()

    def test_test_point_validation_valid(self):
        self.test_analyzer.load_train_data()
        self.test_analyzer.load_ideal_data()
        self.test_analyzer.load_test_data()
        self.test_analyzer.find_bestfit()
        test_dataframe = self.test_analyzer.test_point_validation()

        self.assertIsNotNone(test_dataframe)
        self.assertIsInstance(test_dataframe, pd.DataFrame)

if __name__ == "__main__":
    unittest.main()