from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, ArgumentError


class DatabaseManager:
    """ a class to create and manage sqlite databases.

    Attributes:
        engine: creates a sqlite engine for a specific database

    Methods:
        __init__: creates engine
        create_train_table_from_df: creates table in database
        create_ideal_table_from_df: creates table in database
        create_validation_table_from_df: creates table in database
    """

    def __init__(self, database_name):
        """ initializes DatabaseManager

        :param database_name: name of the database to be created
        """
        try:
            # create engine
            self.engine = create_engine(f"sqlite:///{database_name}.db")
            print(f"Successfully initialized engine for database '{database_name}' ")

        except ArgumentError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")

    def create_train_table_from_df(self, data):
        """ creates a table for the train data inside the database

        :param data: must be a pandas dataframe
        """
        try:
            # create table in database from dataframe
            data.train_data.to_sql("Train data", self.engine, index=False, if_exists="replace")

        except OperationalError as e:
            print(f"Error while trying to create table: {e}")

        except Exception as e:
            print(f"Error: {e}")

        else:
            print("'Train' table successfully created.")

    def create_ideal_table_from_df(self, data):
        """ creates a table for the ideal data inside the database

        :param data: must be a pandas dataframe
        """
        try:
            # create table in database from dataframe
            data.ideal_data.to_sql("Ideal data", self.engine, index=False, if_exists="replace")

        except OperationalError as e:
            print(f"Error while trying to create table: {e}")

        except Exception as e:
            print(f"Error: {e}")

        else:
            print("'Ideal' table successfully created.")

    def create_validation_table_from_df(self, data):
        """ creates a table for the test data inside the database

        :param data: must be a pandas dataframe
        """
        try:
            # create table in database from dataframe
            data.df_filtered_pts.to_sql("Test point validation", self.engine, index=False, if_exists="replace")

        except OperationalError as e:
            print(f"Error while trying to create table: {e}")

        except Exception as e:
            print(f"Error: {e}")

        else:
            print("'Test point validation' table successfully created.")
