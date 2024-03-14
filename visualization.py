import matplotlib.pyplot as plt
import numpy as np
import pandas as dp

class Graphics:

    def plot_train_data(self,data):

        try:
            for column in data.train_data.columns[1:]:
                plt.plot(data.train_data["x"],data.train_data[column],label=column)

            plt.title("Train functions")
            plt.legend()
            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")

            plt.show()

        except AttributeError as e:
            print("Error: Data is missing the dataframe-attribute. Please load data first.", e)
        except KeyError as e:
            print("Error: A dataframe column is missing. Make sure the csv-file has "
                  "a 'x'-coordinate column", e)


    def _plot_bestfit_helper(self,data):

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

        except AttributeError as e:
            print("Error: Data is missing an attribute."
                  "Could be self.bestfit_dict. "
                  "Please make sure that data is loaded " 
                  "and the find_bestfit method has been used.", e)

    def plot_test_data(self,data):

        try:
            plt.plot(data.test_data["x"], data.test_data["y"], "bo")

            plt.axvline(color= "black", linestyle= "--")
            plt.axhline(color= "black", linestyle= "--")
            plt.title("Unfiltered testpoints")

            plt.show()

        except AttributeError as e:
            print("Error: Data is missing an attribute. " 
                  "Please make sure that data is loaded ", e)
        except KeyError as e:
            print("Error: A dataframe column is missing. "
                  "Make sure the dataframe has a 'x'- and 'y'-coordinate column", e)


    def plot_filtered_test_data(self,data):

        try:
            self._plot_bestfit_helper(data)

            plt.plot([point[0] for point in data.filtered_pts],
                     [point[1] for point in data.filtered_pts], "bo", label="Testpoints")

            plt.axvline(color= "black", linestyle= "--")
            plt.axhline(color= "black", linestyle= "--")
            plt.ylim(-20,None)

            plt.title("Best-fitting ideal functions and filtered testpoints")
            plt.legend()

            plt.show()

        except AttributeError as e:
            print("Error: Data is missing an attribute. " 
                  "Please make sure that data is loaded and " 
                  "the find_bestfit and test_point_validation "
                  "methods have both been used. ", e)