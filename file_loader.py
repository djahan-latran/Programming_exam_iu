from df_constructor import DfConstructor
import os

class FileLoader(DfConstructor):

    def __init__(self, foldername, filename):
        self.foldername = foldername
        self.filename = filename

    def load_and_construct_file(self):

        try:
            self.filepath = os.path.join(self.foldername, self.filename)

            if not self.filename.endswith(".csv"):
                raise ValueError("The file is not a csv file")

            loaded_file = self.construct_df_from_file(filepath=self.filepath)

            return loaded_file

        except FileNotFoundError as e:
            print(f"Error: {e}")

        except ValueError as e:
            print(f"Error: {e}")

