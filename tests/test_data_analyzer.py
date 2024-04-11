import unittest
import pandas as pd
from data_analyzer import DataAnalyzer


class TestDataAnalyzer(unittest.TestCase):
    """An unittest class to test methods of the DataAnalyzer class.

    Attributes:
        test_analyzer: Instance of DataAnalyzer. Contains the files to test the methods.

    Methods:
        test_load_train_data_valid: checks if a dataframe type is created
        test_load_ideal_data_valid: checks if a dataframe type is created
        test_load_test_data_valid: checks if a dataframe type is created
        test_find_bestfit_valid_dict:
        test_find_bestfit_valid_train_data:
        test_find_bestfit_valid_ideal_data:
        test_test_point_validation_valid:
    """

    # initialize DataAnalyzer instance with test files
    test_analyzer = DataAnalyzer(train_folder="test_files",
                                 train_file="test_df.csv",
                                 ideal_folder="test_files",
                                 ideal_file="test_df.csv",
                                 test_folder="test_files",
                                 test_file="test_df.csv"
                                 )

    def test_load_train_data_valid(self):
        """This method uses the load_train_data method on a DataAnalyzer instance
        and checks if the attribute is a pandas dataframe"""

        # load test train data
        test_dataframe = self.test_analyzer.load_train_data()

        # check if data is type dataframe after loading
        self.assertIsInstance(test_dataframe, pd.DataFrame)

    def test_load_ideal_data_valid(self):
        """This method uses the load_ideal_data method on a DataAnalyzer instance
        and checks if the attribute is a pandas dataframe"""

        # load test ideal data
        test_dataframe = self.test_analyzer.load_ideal_data()

        # check if data is type dataframe after loading
        self.assertIsInstance(test_dataframe, pd.DataFrame)

    def test_load_test_data_valid(self):
        """This method uses the load_test_data method on a DataAnalyzer instance
        and checks if the attribute is a pandas dataframe"""

        # load test test data
        test_dataframe = self.test_analyzer.load_test_data()

        # check if data is type dataframe after loading
        self.assertIsInstance(test_dataframe, pd.DataFrame)

    def test_find_bestfit_valid_dict(self):
        """This method loads the train and ideal data and then tests if the
        'find_bestfit'-method returns a valid dictionary.
        """

        # load ideal and train data and find the best-fitting functions
        self.test_analyzer.load_train_data()
        self.test_analyzer.load_ideal_data()
        test_dict = self.test_analyzer.find_bestfit()

        # check if dictionary is created and attribute is not 'None'
        self.assertIsNotNone(test_dict)
        self.assertIsInstance(test_dict, dict)

    def test_find_bestfit_valid_train_data(self):
        """The method tests if when 'train_data'-attribute,
        that is needed by the 'find_bestfit'-method, is missing,
        the AttributeError gets raised properly when trying to use 'find_bestfit'.
        """

        # load ideal data and set train data to 'None'
        self.test_analyzer.load_train_data()
        self.test_analyzer.train_data = None
        self.test_analyzer.load_ideal_data()

        # check if error is raised
        with self.assertRaises(AttributeError):
            self.test_analyzer.find_bestfit()

    def test_find_bestfit_valid_ideal_data(self):
        """The method tests if when 'ideal_data'-attribute,
        that is needed by the 'find_bestfit'-method, is missing,
        the AttributeError gets raised properly when trying to use 'find_bestfit'.
        """

        # load train data and set ideal data to 'None'
        self.test_analyzer.load_ideal_data()
        self.test_analyzer.ideal_data = None
        self.test_analyzer.load_train_data()

        # check if error is raised
        with self.assertRaises(AttributeError):
            self.test_analyzer.find_bestfit()

    def test_test_point_validation_valid(self):
        """The method tests if the 'test_point_validation'-method
        returns an attribute that is not 'None' and that is a dataframe.
        """

        # load train, ideal and test data
        self.test_analyzer.load_train_data()
        self.test_analyzer.load_ideal_data()
        self.test_analyzer.load_test_data()

        # find best-fit functions
        self.test_analyzer.find_bestfit()

        # validate test points
        test_dataframe = self.test_analyzer.test_point_validation()

        # check if test_dataframe is not 'None' and if it is of type 'dataframe'
        self.assertIsNotNone(test_dataframe)
        self.assertIsInstance(test_dataframe, pd.DataFrame)

if __name__ == "__main__":
    unittest.main()
