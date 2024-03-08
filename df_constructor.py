import pandas as pd

class DfConstructor:

    def construct_df(self,filepath):
        df = pd.read_csv(filepath)

        return df

