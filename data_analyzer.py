import numpy as np
import pandas as pd
from df_constructor import DfConstructor
from file_loader import FileLoader

class DataAnalyzer(DfConstructor):

    # initiate with parameters set to 'None', so different data can be loaded/added at different times
    def __init__(self, train_folder= None, train_file= None,
                 ideal_folder= None, ideal_file= None,
                 test_folder= None, test_file= None):

        self.train_folder = train_folder
        self.train_file = train_file
        self.ideal_folder = ideal_folder
        self.ideal_file = ideal_file
        self.test_folder = test_folder
        self.test_file = test_file

        # create instances of FileLoader to load the train-/ideal- and testdata
        self.train_data_loader = FileLoader(foldername= self.train_folder,
                                            filename= self.train_file)
        self.ideal_data_loader = FileLoader(foldername= self.ideal_folder,
                                            filename= self.ideal_file)
        self.test_data_loader = FileLoader(foldername= self.test_folder,
                                           filename= self.test_file)

    def load_train_data(self):
        self.train_data = self.train_data_loader.load_and_construct_file()

        return self.train_data

    def load_ideal_data(self):
        self.ideal_data = self.ideal_data_loader.load_and_construct_file()

        return self.ideal_data

    def load_test_data(self):
        self.test_data = self.test_data_loader.load_and_construct_file()

        return self.test_data

    def find_bestfit(self):

        self.bestfit_dict = {}

        count_train_func = self.train_data.shape[1]
        count_ideal_func = self.ideal_data.shape[1]

        for i in range(1, count_train_func):

            min_diff = float("inf")
            curr_tfunc_idx = i

            for j in range(1, count_ideal_func):

                curr_diff = abs(self.train_data.iloc[:, i] - self.ideal_data.iloc[:, j])
                curr_diff_sum = curr_diff.sum()

                min_diff = min(min_diff, curr_diff_sum)

                if min_diff == curr_diff_sum:
                    best_fit_idx = j

            self.bestfit_dict[f"{curr_tfunc_idx}"] = best_fit_idx  # stores both indexes of the train-func \
                                                                   # and the 'best-fitting'  ideal-func

        if len(self.bestfit_dict) == 0:
            print("There are no best fits.")

        else:
            return self.bestfit_dict


    def test_point_validation(self):

        def least_square():

            self.filtered_pts = set()  # stores individual filtered points without duplicates

            self.df_filtered_pts = pd.DataFrame(columns=["X", "Y", "Delta Y", "Ideal function name"])

            for train_idx, ideal_idx in self.bestfit_dict.items():
                ideal_func_name = self.ideal_data.columns[int(ideal_idx)]

                new_dataframe = self.construct_validation_df(ideal_func_name=ideal_func_name)

                for i in range(len(self.test_data)):
                    x_val_test = self.test_data.iloc[i, 0]
                    y_val_test = self.test_data.iloc[i, 1]

                    x_val_ideal_idx = (self.ideal_data.iloc[:, 0] == x_val_test).idxmax()
                    y_val_ideal = self.ideal_data.iloc[x_val_ideal_idx, int(ideal_idx)]

                    y_coords_diff = (abs(y_val_test - y_val_ideal)) ** 2

                    max_distance = np.sqrt(2) * y_val_test

                    if y_coords_diff < max_distance:
                        new_row = {"X": x_val_test, "Y": y_val_test, "Delta Y": y_coords_diff,
                                   "Ideal function name": ideal_func_name
                                   }
                        self.df_filtered_pts = self.df_filtered_pts.append(new_row, ignore_index=True)

                        testpoint = [x_val_test, y_val_test]

                        self.filtered_pts.add(tuple(testpoint))

                    else:
                        continue

            return self.df_filtered_pts

        validation = least_square()

        return validation