import matplotlib.pyplot as plt
from exceptions import InvalidDataError, DataframeTypeError
import pandas as pd


class Graphics:
    """A class to visualize the different data sets and results of the data analysis

    Methods:
        plot_train_data: visualizes the train data
        _plot_bestfit_helper: is only used as a helper function for 'plot_bestfit'
        plot_bestfit: visualizes the best-fitting ideal functions
        plot_test_data: visualizes the unfiltered test data
        plot_filtered_test_data: visualizes the filtered test data
    """

    def plot_train_data(self, data):
        """Visualizes the train data by using the matplotlib library.

        It iterates the rows of the dataframe and plots each x-y-pair as a graph diagram.

        :param data: DataAnalyzer instance with attribute 'train_data'
        :return: plots train data as matplotlib figure
        """

        try:
            # check if train_data is a pandas dataframe
            if not isinstance(data.train_data, pd.DataFrame):
                raise DataframeTypeError

            # check if first column is named 'x'
            if data.train_data.columns[0] != "x":
                raise InvalidDataError("Missing column 'x' at index 0.")

            # check if values are 'FLOAT's
            for column_name in data.train_data.columns:
                for value in data.train_data[column_name]:
                    if not isinstance(value, float):
                        raise InvalidDataError

            # plot the train data
            for column in data.train_data.columns[1:]:
                plt.plot(data.train_data.iloc[:, 0], data.train_data[column], label=column)

            plt.title("Train functions")
            plt.legend()
            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")

            plt.show()

        except DataframeTypeError as e:
            print(f"Error: {e.message}")

        except AttributeError as e:
            print(f"Error: Data might be missing the 'dataframe' attribute. Please load data first. {e}")

        except InvalidDataError as e:
            print(f"Error: {e.message}")

        except Exception as e:
            print(f"Error: {e}")

    def _plot_bestfit_helper(self, data):
        """The helper method to visualize the best-fitting functions

        Iterates through self.bestfit_dict and plots the ideal functions based on the index that is stored
        in the dictionary

        :param data: DataAnalyzer instance that has attributes 'train_data' and 'ideal_data' not None
        """
        # check if train_data is a dataframe
        if not isinstance(data.train_data, pd.DataFrame):
            raise DataframeTypeError

        # check if ideal_data is a dataframe
        if not isinstance(data.ideal_data, pd.DataFrame):
            raise DataframeTypeError

        # check if first column in train_data is named 'x'
        if data.train_data.columns[0] != "x":
            raise InvalidDataError("Missing column 'x' at index 0 in train dataframe.")

        # check if data in dataframe is of type 'FLOAT'
        for column_name in data.train_data.columns:
            for value in data.train_data[column_name]:
                if not isinstance(value, float):
                    raise InvalidDataError

        # plot the bestfit functions
        for train_idx, ideal_idx in data.bestfit_dict.items():
            func_name = data.ideal_data.columns[int(ideal_idx)]

            plt.plot(data.train_data["x"], data.ideal_data.iloc[:, int(ideal_idx)], label=f"{func_name}")

    def plot_bestfit(self, data):
        """Visualizes the best-fitting functions.

        Uses helper function '_plot_bestfit_helper' to plot the best fitting functions
        as a matplotlib graph diagram

        :param data: DataAnalyzer instance that has attributes 'train_data' and 'ideal_data' not None
        :return: matplotlib figure
        """

        # plot the best-fitting functions
        try:
            self._plot_bestfit_helper(data)

            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")
            plt.title("Best-fitting functions of 50 ideal functions")
            plt.legend()

            plt.show()

        except DataframeTypeError as e:
            print(f"Error: {e.message}")

        except InvalidDataError as e:
            print(f"Error: {e.message}")

        except AttributeError as e:
            print(f"Error: {e} "
                  "Please make sure that train and ideal data are loaded " 
                  "and the find_bestfit method has been used.")

        except Exception as e:
            print(f"Error: {e}")

    def plot_test_data(self, data):
        """Visualizes the test data by using the matplotlib library.

        It iterates the rows of the dataframe and plots each x-y-pair as points in a diagram.

        :param data: DataAnalyzer instance with attribute 'test_data'
        :return: plots test data as matplotlib figure
        """
        try:
            # check if test_data is a pandas dataframe
            if not isinstance(data.test_data, pd.DataFrame):
                raise DataframeTypeError

            # check if first dataframe column is named 'x'
            if data.test_data.columns[0] != "x":
                raise InvalidDataError("Missing column 'x' at index 0.")

            # check if second dataframe column is named 'y'
            if data.test_data.columns[1] != "y":
                raise InvalidDataError("Missing column 'y' at index 1.")

            # check if values are 'FLOAT's
            for column_name in data.test_data.columns:
                for value in data.test_data[column_name]:
                    if not isinstance(value, float):
                        raise InvalidDataError

            # plot the test points
            plt.plot(data.test_data["x"], data.test_data["y"], "bo")

            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")
            plt.title("Unfiltered testpoints")

            plt.show()

        except DataframeTypeError as e:
            print(f"Error: {e.message}")

        except InvalidDataError as e:
            print(f"Error: {e.message}")

        except AttributeError as e:
            print("Error: Data is missing an attribute. " 
                  f"Please make sure that data is loaded. {e}")

        except Exception as e:
            print(f"Error: {e}")

    def plot_filtered_test_data(self, data):
        """Visualizes the filtered test data by using the matplotlib library.

        It iterates the set of filtered points and plots each pair as points in a diagram.

        :param data: DataAnalyzer instance with attribute 'self.filtered_pts'
        :return: plots filtered test data as matplotlib figure
        """
        try:
            # plot the best-fitting functions
            self._plot_bestfit_helper(data)

            # plot the filtered points
            plt.plot([point[0] for point in data.filtered_pts],
                     [point[1] for point in data.filtered_pts], "bo", label="Test points")

            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")
            plt.ylim(-20, None)

            plt.title("Best-fitting ideal functions and filtered test points")
            plt.legend()

            plt.show()

        except DataframeTypeError as e:
            print(f"Error: {e.message}")

        except InvalidDataError as e:
            print(f"Error: {e.message}")

        except AttributeError as e:
            print(f"Error: Data is missing an attribute. " 
                  f"Please make sure that data is loaded and " 
                  f"the find_bestfit and test_point_validation "
                  f"methods have both been used. {e}")

        except Exception as e:
            print(f"Error: {e}")
