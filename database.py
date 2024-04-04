from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, ArgumentError


class DatabaseManager:

    def __init__(self, database_name):
        try:
            self.engine = create_engine(f"sqlite:///{database_name}.db")
            print(f"Successfully initialized engine for database '{database_name}' ")

        except ArgumentError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")

    def create_train_table_from_df(self, data):
        try:
            data.train_data.to_sql("Train data", self.engine, index=False, if_exists="replace")

        except OperationalError as e:
            print(f"Error while trying to create table: {e}")

        except Exception as e:
            print(f"Error: {e}")

        else:
            print("'Train' table successfully created.")

    def create_ideal_table_from_df(self, data):
        try:
            data.ideal_data.to_sql("Ideal data", self.engine, index=False, if_exists="replace")

        except OperationalError as e:
            print(f"Error while trying to create table: {e}")

        except Exception as e:
            print(f"Error: {e}")

        else:
            print("'Ideal' table successfully created.")

    def create_validation_table_from_df(self, data):
        try:
            data.df_filtered_pts.to_sql("Test point validation", self.engine, index=False, if_exists="replace")

        except OperationalError as e:
            print(f"Error while trying to create table: {e}")

        except Exception as e:
            print(f"Error: {e}")

        else:
            print("'Test point validation' table successfully created.")
