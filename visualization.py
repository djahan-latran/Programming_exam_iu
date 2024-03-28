import matplotlib.pyplot as plt
from exceptions import InvalidDataError, DataframeTypeError
import pandas as pd


class Graphics:

    def plot_train_data(self,data):

        try:
            if not isinstance(data.train_data, pd.DataFrame):
                raise DataframeTypeError

            if data.train_data.columns[0] != "x":
                raise InvalidDataError("Missing column 'x' at index 0.")

            for column_name in data.train_data.columns:
                for value in data.train_data[column_name]:
                    if not isinstance(value,float):
                        raise InvalidDataError

            for column in data.train_data.columns[1:]:
                plt.plot(data.train_data.iloc[:,0],data.train_data[column],label=column)


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

    def _plot_bestfit_helper(self,data):

        if not isinstance(data.train_data, pd.DataFrame):
            raise DataframeTypeError

        if not isinstance(data.ideal_data, pd.DataFrame):
            raise DataframeTypeError

        if data.train_data.columns[0] != "x":
            raise InvalidDataError("Missing column 'x' at index 0 in train dataframe.")

        for column_name in data.train_data.columns:
            for value in data.train_data[column_name]:
                if not isinstance(value, float):
                    raise InvalidDataError

        for train_idx, ideal_idx in data.bestfit_dict.items():
            func_name = data.ideal_data.columns[int(ideal_idx)]

            plt.plot(data.train_data["x"],data.ideal_data.iloc[:,int(ideal_idx)], label=f"{func_name}")

    def plot_bestfit(self, data):

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

    def plot_test_data(self,data):

        try:
            if not isinstance(data.test_data, pd.DataFrame):
                raise DataframeTypeError

            if data.test_data.columns[0] != "x":
                raise InvalidDataError("Missing column 'x' at index 0.")

            if data.test_data.columns[1] != "y":
                raise InvalidDataError("Missing column 'y' at index 1.")

            for column_name in data.test_data.columns:
                for value in data.test_data[column_name]:
                    if not isinstance(value, float):
                        raise InvalidDataError

            plt.plot(data.test_data["x"], data.test_data["y"], "bo")

            plt.axvline(color= "black", linestyle= "--")
            plt.axhline(color= "black", linestyle= "--")
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


    def plot_filtered_test_data(self,data):

        try:
            self._plot_bestfit_helper(data)

            plt.plot([point[0] for point in data.filtered_pts],
                     [point[1] for point in data.filtered_pts], "bo", label="Test points")

            plt.axvline(color= "black", linestyle= "--")
            plt.axhline(color= "black", linestyle= "--")
            plt.ylim(-20,None)

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