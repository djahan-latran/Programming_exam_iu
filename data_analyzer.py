import numpy as np
from df_constructor import DfConstructor
from file_loader import FileLoader
from exceptions import InvalidDataError, DataframeTypeError


class DataAnalyzer(DfConstructor):
    """A class that manages the train, ideal and test data as dataframes,
    finds the best fitting ideal functions and validates them with testpoints.

    Attributes:
        train_folder: directory where train data is stored
        train_file: train data csv-file
        ideal_folder: directory where ideal data is stored
        ideal_file: ideal data csv-file
        test_folder: directory where test data is stored
        test_file: test data csv-file
        train_data: train data dataframe
        ideal_data: ideal data dataframe
        test_data: test data dataframe
        bestfit_dict: stores the best fitting ideal functions to the train set
        filtered_pts: a set of the filtered test points
        df_filtered_pts: dataframe that stores the test points and their belonging bestfit functions

    Methods:
        __init__: initializes DataAnalyzer with directory and file names
        load_train_data: loads train data and constructs a dataframe
        load_ideal_data: loads ideal data and constructs a dataframe
        load_test_data: loads test data and constructs a dataframe
        find_bestfit: finds best fitting ideal functions
        test_point_validation: filters testpoints by their maximum distance
        to the best fitting ideal functions
    """

    def __init__(self, train_folder=None, train_file=None,
                 ideal_folder=None, ideal_file=None,
                 test_folder=None, test_file=None):
        """Initializes DataAnalyzer instance

        When given the needed parameters creates instances of FileLoader that
        can be used by other methods of the class to load data and create dataframes

        :param train_folder: directory (must be in same directory as main.py) where train data is stored
        :param train_file: name of train data csv-file
        :param ideal_folder: directory (must be in same directory as main.py) where ideal data is stored
        :param ideal_file: name of ideal data csv-file
        :param test_folder: directory (must be in same directory as main.py) where test data is stored
        :param test_file: name of test data csv-file
        """
        self.train_folder = train_folder
        self.train_file = train_file
        self.ideal_folder = ideal_folder
        self.ideal_file = ideal_file
        self.test_folder = test_folder
        self.test_file = test_file

        # create instances of FileLoader to load the train-/ideal- and testdata
        self.train_data_loader = FileLoader(foldername=self.train_folder,
                                            filename=self.train_file)
        self.ideal_data_loader = FileLoader(foldername=self.ideal_folder,
                                            filename=self.ideal_file)
        self.test_data_loader = FileLoader(foldername=self.test_folder,
                                           filename=self.test_file)

    def load_train_data(self):
        """Loads the train data and creates a dataframe out of it

        :return: a pandas dataframe
        """
        try:
            # load the data
            self.train_data = self.train_data_loader.load_and_construct_csv()

        except FileNotFoundError as e:
            print(f"Error (train data): {e}")

        except ValueError as e:
            print(f"Error (train data): {e}")

        except AttributeError as e:
            print(f"Error (train data): {e}")

        except DataframeTypeError as e:
            print(f"Error: {e}")

        else:
            print("Train data successfully loaded")
            return self.train_data

    def load_ideal_data(self):
        """Loads the ideal data and creates a dataframe out of it

        :return: a pandas dataframe
        """
        try:
            # load the data
            self.ideal_data = self.ideal_data_loader.load_and_construct_csv()

        except FileNotFoundError as e:
            print(f"Error (ideal data): {e}")

        except ValueError as e:
            print(f"Error (ideal data): {e}")

        except AttributeError as e:
            print(f"Error (ideal data): {e}")

        except DataframeTypeError as e:
            print(f"Error: {e}")

        else:
            print("Ideal data successfully loaded")
            return self.ideal_data

    def load_test_data(self):
        """Loads the test data and creates a dataframe out of it

        :return: a pandas dataframe
        """
        try:
            # load the data
            self.test_data = self.test_data_loader.load_and_construct_csv()

        except FileNotFoundError as e:
            print(f"Error (test data): {e}")

        except ValueError as e:
            print(f"Error (test data): {e}")

        except AttributeError as e:
            print(f"Error (test data: {e}")

        except DataframeTypeError as e:
            print(f"Error: {e}")

        else:
            print("Test data successfully loaded")
            return self.test_data

    def find_bestfit(self):
        """Finds the best-fitting ideal functions


        :return: a dictionary that contains the index of the train function paired with the index
        of the best fitting ideal function. The indeces correspond to the index in the dataframes.
        """
        try:
            # create empty dictionary
            self.bestfit_dict = {}

            # check if ideal_data is None
            if self.ideal_data is None:
                raise AttributeError("Attribute 'ideal_data' is None.")

            # check if train_data is None
            if self.train_data is None:
                raise AttributeError("Attribute 'train_data' is None.")

            # check if values are of type 'FLOAT's
            for column_name in self.train_data.columns:
                for value in self.train_data[column_name]:
                    if not isinstance(value,(float, int)):
                        raise InvalidDataError

            # get the amount of train- and ideal functions
            count_train_func = self.train_data.shape[1]
            count_ideal_func = self.ideal_data.shape[1]

            # Find the best-fitting functions.
            # Start iterating through the train functions
            # at index 1 to skip the 'x'-column
            for i in range(1, count_train_func):

                # set an infinite large starting value for the minimum
                min_diff = float("inf")
                curr_tfunc_idx = i

                # for each train function, iterate through all the ideal functions
                for j in range(1, count_ideal_func):

                    # calculate the absolute difference between all y-values
                    # of the current train-function and the current ideal-function
                    curr_diff = abs(self.train_data.iloc[:, i] - self.ideal_data.iloc[:, j])
                    curr_diff_sum = curr_diff.sum()

                    # keep track of the minimum value
                    min_diff = min(min_diff, curr_diff_sum)

                    # whenever a new minimum is found,
                    # save the index of the function
                    if min_diff == curr_diff_sum:
                        best_fit_idx = j

                # store indices of the train function (key)
                # and the correlating best-fitting ideal function (value)
                # in a dictionary
                self.bestfit_dict[f"{curr_tfunc_idx}"] = best_fit_idx

        except AttributeError as e:
            print(f"Error: Please make sure train- and ideal data are loaded. {e}")
            raise

        except KeyError as e:
            print(f"Error: The data doesn't have the proper structure. "
                  f"Make sure x-values are in first column "
                  f"and y-values in others. {e}")

        except InvalidDataError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"An Error occurred: {e}")

        else:
            print("The best-fitting functions have been found and stored in 'self.bestfit_dict'.")
            return self.bestfit_dict

    def test_point_validation(self):
        """filters the test points based on their total distance to the best fitting functions
        and assigns one of the best fitting functions to the test point if a criteria is met.

        The method compares the distance of the best fitting functions' y-values
        to the test point's y-values. If the absolute distance between test-point-y-coordinate
        and function's y-coordinate is smaller than the square root of 2 times the y-value of test point,
        then the criteria is met and the point get's assigned to the current function that is tested.

        :return: dataframe
        """
        def _least_square():
            """The helper function that filters and assigns the test points
            """
            # check for attribute 'bestfit_dict'
            if not self.bestfit_dict:
                raise AttributeError

            # initialize empty set
            self.filtered_pts = set()

            # initialize validation dataframe
            self.df_filtered_pts = self.construct_validation_df()

            # compare the best fitting function's y-values with the test point y-values
            for train_idx, ideal_idx in self.bestfit_dict.items():
                ideal_func_name = self.ideal_data.columns[int(ideal_idx)]

                # iterate over each row in test dataframe
                for i in range(len(self.test_data)):

                    # save current x- and y-value in variable
                    x_val_test = self.test_data.iloc[i, 0]
                    y_val_test = self.test_data.iloc[i, 1]

                    # find the same x-value (row) in the ideal functions dataframe
                    x_val_ideal_idx = (self.ideal_data.iloc[:, 0] == x_val_test).idxmax()

                    # save the y-value from the ideal functions dataframe at the current x-value
                    y_val_ideal = self.ideal_data.iloc[x_val_ideal_idx, int(ideal_idx)]

                    # calculate the y-value difference to the power of 2, to get rid of negative values
                    y_coords_diff = (y_val_test - y_val_ideal) ** 2

                    # calculate the maximum distance criteria
                    # by multiplying the square root of 2 times the y-value of the current test point
                    max_distance = np.sqrt(2) * y_val_test

                    # if the distance between the y-values is smaller than the criteria,
                    # assign the current ideal function to the current test point
                    # and create a new row for the validation dataframe
                    if y_coords_diff < max_distance:
                        new_row = {"X": x_val_test, "Y": y_val_test, "Delta Y": y_coords_diff,
                                   "Ideal function name": ideal_func_name
                                   }

                        self.df_filtered_pts = self.df_filtered_pts.append(new_row, ignore_index=True)

                        # add the test point to the set
                        testpoint = [x_val_test, y_val_test]
                        self.filtered_pts.add(tuple(testpoint))

                    else:
                        continue

            return self.df_filtered_pts

        try:
            validation = _least_square()
            return validation

        except AttributeError:
            print("Error: Missing an attribute. "
                  "First load the data and find the best-fitting ideal functions.")

        except Exception as e:
            print(f"Error: {e}")
