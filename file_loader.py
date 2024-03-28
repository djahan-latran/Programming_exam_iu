from df_constructor import DfConstructor
import os


class FileLoader(DfConstructor):

    def __init__(self, foldername, filename):
        self.foldername = foldername
        self.filename = filename

    def load_and_construct_csv(self):

        if self.filename is None or self.foldername is None:
            raise AttributeError("Missing attribute 'foldername' or 'filename'.")

        if not self.filename.endswith(".csv"):
            raise ValueError("The file must be a csv-file and end with '.csv'")

        self.filepath = os.path.join(self.foldername, self.filename)
        loaded_file = self.construct_df_from_file(filepath=self.filepath)

        return loaded_file

