import numpy as np
import pandas as pd
from df_constructor import DfConstructor
from file_loader import FileLoader

class DataAnalyzer:

    def __init__(self, train_folder= None, train_file= None,
                 ideal_folder= None, ideal_file= None,
                 test_folder= None, test_file= None):

        self.train_folder = train_folder
        self.train_file = train_file
        self.ideal_folder = ideal_folder
        self.ideal_file = ideal_file
        self.test_folder = test_folder
        self.test_file = test_file

        self.train_data_loader = FileLoader(foldername= self.train_folder,
                                            filename= self.train_file)
        self.ideal_data_loader = FileLoader(foldername= self.ideal_folder,
                                            filename= self.ideal_file)
        self.test_data_loader = FileLoader(foldername= self.test_folder,
                                           filename= self.test_file)

    def load_train_data(self):
        train_data = self.train_data_loader.load_and_construct_file()

        return train_data

    def load_ideal_data(self):
        ideal_data = self.ideal_data_loader.load_and_construct_file()

        return ideal_data

    def load_test_data(self):
        test_data = self.test_data_loader.load_and_construct_file()

        return test_data

    def find_bestfit(self):
        pass



        # self.bestfit = {}
        #
        # count_train_func = self.dataframe.shape[1]
        # count_ideal_func = ideal.dataframe.shape[1]
        #
        # for i in range(1, count_train_func):
        #
        #     min_diff = float("inf")
        #     curr_tfunc_idx = i
        #
        #     for j in range(1, count_ideal_func):
        #
        #         curr_diff = abs(self.dataframe.iloc[:, i] - ideal.dataframe.iloc[:, j])
        #         curr_diff_sum = curr_diff.sum()
        #
        #         min_diff = min(min_diff, curr_diff_sum)
        #
        #         if min_diff == curr_diff_sum:
        #             best_fit_idx = j
        #
        #     self.bestfit[f"{curr_tfunc_idx}"] = best_fit_idx
        #
        # if len(self.bestfit) == 0:
        #     print("There are no best fits.")
        #
        # else:
        #     return self.bestfit


    def test_point_validation(self):

        def least_square():
            pass

        #least_square()
        pass
    
