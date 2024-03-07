import numpy as np
import pandas as pd
from df_constructor import DfConstructor
from file_loader import FileLoader

class DataAnalyzer(DfConstructor,FileLoader):

    def load_train_data(self):
        self.load_and_construct_file()

    def load_ideal_data(self):
        self.load_and_construct_file()

    def load_test_data(self):
        self.load_and_construct_file()

    def find_bestfit(self):
        pass

    def least_square(self):
        pass

    def test_point_validation(self):
        self.least_square()

    
