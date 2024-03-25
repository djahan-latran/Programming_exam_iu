import pandas as pd

class DfConstructor:

    def construct_df_from_file(self,filepath):

        try:
            df = pd.read_csv(filepath)
            return df

        except FileNotFoundError:
            raise FileNotFoundError("File or path does not exist!")

    def construct_validation_df(self):

        try:
            validation_df = pd.DataFrame(columns=["X", "Y", "Delta Y", "Ideal function name"])
            return validation_df

        except Exception as e:
            print(f"Error: {e}")