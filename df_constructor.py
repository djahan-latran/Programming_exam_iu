import pandas as pd
from exceptions import DataframeTypeError


class DfConstructor:

    def construct_df_from_file(self,filepath):

        try:
            df = pd.read_csv(filepath)

            if not isinstance(df, pd.DataFrame):
                raise DataframeTypeError("Something went wrong "
                                         "while constructing the dataframe")
            return df

        except FileNotFoundError:
            raise FileNotFoundError("File or path does not exist!")

    def construct_validation_df(self):

        try:
            validation_df = pd.DataFrame(columns=["X", "Y", "Delta Y", "Ideal function name"])

            if not isinstance(validation_df, pd.DataFrame):
                raise DataframeTypeError("Something went wrong "
                                         "while constructing the dataframe")
            return validation_df

        except Exception as e:
            print(f"Error: {e}")