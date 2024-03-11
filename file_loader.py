import pandas as pd
from df_constructor import DfConstructor
import os

class FileLoader(DfConstructor):

    def __init__(self, foldername, filename):
        self.foldername = foldername
        self.filename = filename

    def load_and_construct_file(self):
        self.filepath = os.path.join(self.foldername,self.filename)

        loaded_file = self.construct_df_from_file(filepath= self.filepath)

        return loaded_file