import unittest
from file_loader import FileLoader


class TestFileLoader(unittest.TestCase):
    """An unittest class to test methods of the FileLoader class.

    Methods:
        test_load_and_construct_csv_attribute: tests if AttributeError is raised
        test_load_and_construct_csv_file_format: tests if ValueError is raised
        test_load_and_construct_csv_file: tests if data is properly loaded
    """

    def test_load_and_construct_csv_attribute(self):
        """The method sets attributes 'foldername' and 'filename' to 'None',
        then creates a FileLoader instance and tries to load the data.
        It then checks if the AttributeError is raised
        """
        # create instance of FileLoader with 'None' attributes
        foldername = None
        filename = None
        fileloader = FileLoader(foldername=foldername, filename=filename)

        # test if error is raised
        with self.assertRaises(AttributeError):
            fileloader.load_and_construct_csv()

    def test_load_and_construct_csv_file_format(self):
        """The method uses a wrong format for the file (.txt) and checks
        if ValueError is raised when trying to load the data.
        """
        # initialize FileLoader instance with wrong file format
        foldername = "test_files"
        filename = "unittest_fileloader.txt"
        fileloader = FileLoader(foldername=foldername, filename=filename)

        # check if error is raised
        with self.assertRaises(ValueError):
            fileloader.load_and_construct_csv()

    def test_load_and_construct_csv_file(self):
        """The method tests, if a file in correct format is loaded and constructed properly.
        (Is not 'None')
        """
        foldername = "test_files"
        filename = "test_df.csv"

        # initialize FileLoader instance with test file
        fileloader = FileLoader(foldername=foldername, filename=filename)
        file = fileloader.load_and_construct_csv()

        # check if file is None
        self.assertIsNotNone(file)


if __name__ == '__main__':
    unittest.main()
