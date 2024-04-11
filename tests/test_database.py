import unittest
from database import DatabaseManager
from data_analyzer import DataAnalyzer
from sqlalchemy import inspect


class TestDatabaseManager(unittest.TestCase):
    """An unittest class to test methods of the DatabaseManager class.

    Methods:
        test_database_initialization: tests if 'engine' gets initialized
        test_create_table_from_df_valid: tests if a table is created properly
    """

    def test_database_initialization(self):
        """The method creates an instance of DatabaseManager and tests,
        if the instance owns the attribute 'engine'.
        """

        # create database
        database = DatabaseManager(database_name="test_database")

        # check if it has attribute 'engine'
        self.assertTrue(hasattr(database, "engine"))

    def test_create_table_from_df_valid(self):
        """The method creates and instance of DatabaseManager and DataAnalyzer.
        It then loads data with DataAnalyzer and creates a table from that data
        in DatabaseManager.
        Then an inspector is created to check if the database contains the table.
        """

        # initialize DatabaseManager instance
        database = DatabaseManager(database_name="test_database")

        # initialize DataAnalyzer instance and load train data
        data = DataAnalyzer(train_folder="test_files", train_file="test_df.csv")
        data.load_train_data()

        # create table in the database
        database.create_train_table_from_df(data=data)
        table_name = "Train data"

        # create inspector and pass the table name
        inspector = inspect(database.engine)
        test_value = inspector.has_table(table_name)

        # check if table is in database
        self.assertTrue(test_value, f"Table {table_name} does not exist.")


if __name__ == "__main__":
    unittest.main()
