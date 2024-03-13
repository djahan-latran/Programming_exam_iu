import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


class DatabaseManager:

    def __init__(self,database_name):

        self.engine = create_engine(f"sqlite:///{database_name}.db")

    def create_train_table_from_df(self,data):
        try:
            data.train_data.to_sql("Train data", self.engine, index= False, if_exists= "replace")
        except OperationalError as e:
            print(f"Error while trying to create table: {e}")

    def create_ideal_table_from_df(self,data):
        try:
            data.ideal_data.to_sql("Ideal data", self.engine, index=False, if_exists="replace")
        except OperationalError as e:
            print(f"Error while trying to create table: {e}")

    def create_validation_table_from_df(self,data):
        try:
            data.df_filtered_pts.to_sql("Test point validation", self.engine, index=False, if_exists="replace")
        except OperationalError as e:
            print(f"Error while trying to create table: {e}")
