import pandas as pd

class DfConstructor:

    def construct_df_from_file(self,filepath):

        try:
            df = pd.read_csv(filepath)
            return df

        except FileNotFoundError:
            raise FileNotFoundError(f"File could not be found in {filepath}")

    def construct_validation_df(self):

        validation_df = pd.DataFrame(columns=["X", "Y", "Delta Y", "Ideal function name"])

        return validation_df

