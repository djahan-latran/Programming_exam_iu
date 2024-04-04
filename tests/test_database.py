import unittest
from database import DatabaseManager
from data_analyzer import DataAnalyzer
from sqlalchemy import inspect


class TestDatabaseManager(unittest.TestCase):

    def test_database_initialization(self):
        database = DatabaseManager(database_name="test_database")

        self.assertTrue(hasattr(database, "engine"))

    def test_create_table_from_df_valid(self):
        database = DatabaseManager(database_name="test_database")
        data = DataAnalyzer(train_folder="test_files", train_file="test_df.csv")
        data.load_train_data()

        database.create_train_table_from_df(data=data)
        table_name = "Train data"

        inspector = inspect(database.engine)
        test_value = inspector.has_table(table_name)

        self.assertTrue(test_value, f"Table {table_name} does not exist.")


if __name__ == "__main__":
    unittest.main()