from df_constructor import DfConstructor
import os


class FileLoader(DfConstructor):
    """a class to load files

    Attributes:
        foldername: directory where the file is saved
        (directory must be in the same directory as the main.py file)
        filename: name of the file (must be stored in directory foldername)
        filepath: stores the filepath by combining foldername and filename

    Methods:
        __init__: initializes FileLoader, takes attributes 'foldername' and 'filename'
        load_and_construct_csv: loads and constructs a dataframe by inheriting from DfConstructor
    """

    def __init__(self, foldername, filename):
        """initialize FileLoader

        Args:
            foldername (str): name of folder
            filename (str): name of file
        """
        self.foldername = foldername
        self.filename = filename

    def load_and_construct_csv(self):
        """loads csv-file and constructs a dataframe

        :return: a pandas dataframe
        """
        # check if attributes are 'None'
        if self.filename is None or self.foldername is None:
            raise AttributeError("Missing attribute 'foldername' or 'filename'.")

        # check if filename ends with .csv
        if not self.filename.endswith(".csv"):
            raise ValueError("The file must be a csv-file and end with '.csv'")

        # create the filepath
        self.filepath = os.path.join(self.foldername, self.filename)

        loaded_file = self.construct_df_from_file(filepath=self.filepath)

        return loaded_file
