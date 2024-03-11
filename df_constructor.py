import pandas as pd

class DfConstructor:

    def construct_df_from_file(self,filepath):
        df = pd.read_csv(filepath)

        return df

    def construct_validation_df(self,ideal_func_name):
        validation_df = pd.DataFrame(columns=["X","Y","Delta Y",f"{ideal_func_name}"])

        return validation_df

