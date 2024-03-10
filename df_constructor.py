import pandas as pd

class DfConstructor:

    def construct_df(self,filepath):
        dataframe = pd.read_csv(filepath)

        return dataframe

