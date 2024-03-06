import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import os


class TrainFunctions:
    """
    The TrainFunctions class is used to construct, \
    load, print and plot a dataframe that will be used for test data.
    """

    def __init__(self, folder, filename):
        """
        This method contains the information for the data to be loaded. E.g. the filename and the folder \
        where it is stored.

        :param folder: This parameter stores the foldername in which the file is found. The folder must be \
        in the same directory as the script.

        :param filename: This parameter stores the filename which must be a csv file and end with .csv

        The method raises a TypeError if the format of the file is wrong. \
        If execution is successful, the method will create the attribute dataframe.
        """

        self.filename = filename

        if not self.filename.endswith(".csv"):

            raise TypeError("The file must be a CSV file with the extension '.csv'")

        self.folder = folder
        self.dataframe = None

    def load(self):
        """
        The 'load' method will load the file from the instance that was created with the class.
        It constructs the 'filepath' from the parameters 'folder' and 'filename' of the class and creates a pandas \
        dataframe that is stored in the dataframe attribute. \
        If file is not found it raises FileNotFoundError.
        """

        filepath = os.path.join(self.folder,self.filename)

        try:
            self.dataframe = pd.read_csv(filepath)

            print("The file loaded successfully.")

            self.x_max = self.dataframe["x"].max()
            self.x_min = self.dataframe["x"].min()

            self.y_max = max(self.dataframe.max()[1:])
            self.y_min = min(self.dataframe.min()[1:])


        except FileNotFoundError:

            print(f"File '{self.filename}' does not exist in the folder '{self.folder}'" \
                  "or maybe the folder name is incorrect. Please check for typos")

    def display(self):
        """
        The 'display' method prints the dataframe attribute of the class.
        """

        try:
            print(self.dataframe)

        except AttributeError:
            print("'dataframe' attribute is 'None'. Please use the 'load'-method before trying to plot.")

    def plot(self):
        """
        The 'plot' method will show the values stored in dataframe as graphs in a matplotlib axes.
        For printing the x/y-values it uses the first column of the dataframe for the x-values \
        and each additional column for the y-values.
        It iterates through each column and therefore plots every function that is stored in the dataframe.
        """

        try:
            for column in self.dataframe.columns[1:]:

                plt.plot(self.dataframe["x"],self.dataframe[column],label= column)

            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")
            plt.legend()
            plt.show()

        except AttributeError:
            print("'dataframe' attribute is 'None'. Please use the 'load'-method before trying to plot.")


    def find_bestfit(self, ideal):
        """
        It compares the stored values in self.dataframe \
        with the values of the ideal.dataframe of the IdealFunctions instance

        CAUTION: This method needs an instance of IdealFunctions

        :param ideal: Takes in an instance of the IdealFunctions class which has to be loaded by its 'load()' method \
        beforehand.

        :return: Returns a dictionary which stores the index(in the TrainFunctions dataframe) of the train function  \
        as the key and the index(in the IdealFunction dataframe) of the corresponding best-fitting ideal function  \
        as the value.
        """
        try:
            self.bestfit = {}

            count_train_func = self.dataframe.shape[1]
            count_ideal_func = ideal.dataframe.shape[1]

            for i in range(1, count_train_func):

                min_diff = float("inf")
                curr_tfunc_idx = i

                for j in range(1, count_ideal_func):

                    curr_diff = abs(self.dataframe.iloc[:, i] - ideal.dataframe.iloc[:, j])
                    curr_diff_sum = curr_diff.sum()

                    min_diff = min(min_diff, curr_diff_sum)

                    if min_diff == curr_diff_sum:
                        best_fit_idx = j

                self.bestfit[f"{curr_tfunc_idx}"] = best_fit_idx

            if len(self.bestfit) == 0:
                print("There are no best fits.")

            else:
                return self.bestfit

        except AttributeError:
            print("Missing attribute 'dataframe'. Use 'load'-method first.")


    def plot_bestfit(self,ideal):
        """
        This method plots the best-fitting functions of the ideal-function set.
        Therefore it takes the IdealFunctions instance as parameter to properly label the graphs in the plot.

        CAUTION: This method only works after 'find_bestfit()' has been used on the instance, since the method needs \
        the attribute 'self.bestfit' which is created in the 'find_bestfit()' method.

        :param ideal: Takes in an instance of the IdealFunctions class which has to be loaded by its 'load()' method \
        beforehand.

        :return: plots a matplotlib axis that shows the best-fitting functions
        """
        try:
            for train_idx, ideal_idx in self.bestfit.items():

                ideal_func_name = ideal.dataframe.columns[int(ideal_idx)]

                plt.plot(self.dataframe["x"], ideal.dataframe.iloc[:, int(ideal_idx)], label=f"{ideal_func_name}")

            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")

            plt.title("Best-fit ideal functions")
            plt.grid()
            plt.legend()

            plt.show()

        except AttributeError:

            if not hasattr(self, "dataframe"):
                print("Missing attribute 'dataframe'. Use 'load'-method first.")

            if not hasattr(self, "bestfit"):
                print("Missing attribute 'bestfit'. Use 'find_bestfit'-method first.")

    def plot_bestfit_overlay(self,ideal):
        """
        This method plots the train functions overlaid with the best-fitting functions of the ideal-function set.
        Therefore it takes the IdealFunctions instance as parameter to properly label the graphs in the plot.

        CAUTION: This method only works after 'find_bestfit()' has been used on the instance, since the method needs \
        the attribute 'self.bestfit' which is created in the 'find_bestfit()' method.

        :param ideal: Takes in an instance of the IdealFunctions class which has to be loaded by its 'load()' method \
        beforehand.

        :return: plots a matplotlib axis
        """
        try:
            for train_idx, ideal_idx in self.bestfit.items():

                plt.plot(self.dataframe["x"], self.dataframe.iloc[:, int(train_idx)],label=None)
                plt.plot(ideal.dataframe["x"], ideal.dataframe.iloc[:, int(ideal_idx)], label=None)

            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")

            plt.title("Train functions and their best-fits on top")
            plt.grid()

            plt.show()

        except AttributeError:

            if not hasattr(self, "dataframe"):
                print("Missing attribute 'dataframe'. Use 'load'-method first.")

            if not hasattr(self, "bestfit"):
                print("Missing attribute 'bestfit'. Use 'find_bestfit'-method first.")


class IdealFunctions(TrainFunctions):
    """
    The IdealFunctions class inherits from the TrainFunctions class and is used to construct, \
    load, print and plot a dataframe that will be used to compare its functions to the train-functions.
    """

    def plot(self,x_min,x_max,y_min,y_max):
        """
        The 'plot' method plots a matplotlib axis that shows each function stored in the IdealFunctions.dataframe \
        instance.

        :param x_min: minimum x-value on axis
        :param x_max: maximum x-value on axis
        :param y_min: minimum y-value on axis
        :param y_max: maximum y-value on axis
        :return: plots the axis
        """

        try:
            plt.plot(self.dataframe["x"], self.dataframe)

            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")

            plt.ylim(y_min, y_max)
            plt.xlim(x_min, x_max)

            plt.grid()
            plt.title("All ideal functions")
            plt.show()

        except AttributeError:
            print("Missing attribute 'dataframe'. Use 'load'-method first.")

class TestPoints(TrainFunctions):
    """
    The TestPoints class inherits from the TrainFunctions class and is used to construct, \
    load, print and plot the values of the test-data.
    It also allows to filter the test-data by the train-data based on the least-square technique.
    """

    def plot_pts(self,train):
        """
        This method plots the points of the TestPoints instance in a matplotlib axis.

        :param train: Takes in an instance of the TrainFunctions class which has to be loaded by its 'load()' method \
        beforehand.

        :return: plots a matplotlib axis
        """
        try:
            plt.plot(self.dataframe["x"], self.dataframe["y"],"go")

            plt.axvline(color="black", linestyle="--")
            plt.axhline(color="black", linestyle="--")

            plt.ylim(train.y_min, train.y_max)
            plt.xlim(train.x_min, train.x_max)

            plt.show()

        except AttributeError:
            print("Missing attribute 'dataframe'. Use 'load'-method first.")

    def filter_pts(self, train, ideal):
        """
        This method evaluates if a point of the TestPoints instance 'belongs' to one of the best-fitting functions \
        that were found in the 'find_bestfit' method of the TrainFunctions class.
        It does so by comparing the absolute distance of the y-value of a testpoint and the y-value of a function \
        at x to the squareroot of 2 times the y-value of the testpoint. If the distance of the testpoint's y-value \
        to the function's y-value is greater than sqrt(2) * y-value(of testpoint) then the point does not belong to \
        the function that it is compared to.
        It compares each function to each point and saves the differences in a dataframe.

        CAUTION: Use "find_bestfit" on TrainFunctions instance before using this method!

        :param train: Takes in an instance of the TrainFunctions class which has to be loaded by its 'load()' method \
        beforehand.

        :param ideal: Takes in an instance of the IdealFunctions class which has to be loaded by its 'load()' method \
        beforehand.

        :return: Returns a list of pandas dataframes (one for each best-fitting function) \
        with the testpoints that belong to it and the absolute difference stored.
        It also creates an attribute called "filtered_pts" that stores all the individual points as a set (so there \
        are no duplicates) which can be used to plot the filtered points.
        """

        try:
            if self.dataframe is None:
                raise AttributeError("Missing attribute 'dataframe'. Use 'load'-method first.")

            if not hasattr(train,"bestfit"):
                raise AttributeError("Missing attribute 'bestfit'. Either there is no best-fitting function or " \
                                     "the 'find_bestfit'-method has not been used on 'train' yet.")

            self.filtered_pts = set()
            self.dataframes_filtered = []

            for train_idx, ideal_idx in train.bestfit.items():

                ideal_func_name = ideal.dataframe.columns[int(ideal_idx)]

                new_dataframe = pd.DataFrame(columns=["x_test","y_test","delta_y",f"{ideal_func_name}"])

                for i in range(len(self.dataframe)):
                    x_val_test = self.dataframe.iloc[i, 0]
                    y_val_test = self.dataframe.iloc[i, 1]

                    x_val_ideal_idx = (ideal.dataframe.iloc[:,0] == x_val_test).idxmax()
                    y_val_ideal = ideal.dataframe.iloc[x_val_ideal_idx, int(ideal_idx)]

                    y_coords_diff = (abs(y_val_test - y_val_ideal)) ** 2

                    max_distance = np.sqrt(2) * y_val_test

                    if y_coords_diff < max_distance:
                        new_row = {"x_test" : x_val_test, "y_test" : y_val_test, "delta_y" : y_coords_diff,
                                   f"{ideal_func_name}" : y_val_ideal
                                   }
                        new_dataframe = new_dataframe.append(new_row,ignore_index=True)

                        testpoint = [x_val_test,y_val_test]

                        self.filtered_pts.add(tuple(testpoint))

                    else:
                        continue

                self.dataframes_filtered.append(new_dataframe)

            return self.dataframes_filtered

        except Exception as e:
            print(f"Error: {e}")

    def plot_filtered_pts(self):
        """
        This method plots the points that were filtered by the best-fitting functions of IdealFunctions.

        CAUTION: Can only be used after 'filter_pts' has been executed.

        :return: Plots the axis showing the filtered points.
        """

        try:
            plt.plot([point[0] for point in self.filtered_pts],
                     [point[1] for point in self.filtered_pts], "bo")
            plt.grid()
            plt.show()

        except AttributeError:
            print("'filtered_pts'-attribute missing. Use 'filter_pts'-method first.")


    def find_bestfit(self, ideal):

        print("This method is only meant for the TrainFunctions class and therefore returns: 'None'")

        return None


class Database:
    """
    Creates a mysql-database to store the resulting deviations of the test points \
    with the best-fitting functions in a table.
    The class allows to create, edit and delete tables as well as data.
    """

    def __init__(self, host, user, password, database):
        """
        This method takes all the data that is then used in the 'connect' method to connect to the database.
        """

        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """
        This method establishes a connection to the database.

        :return: It creates the attribute self.mycursor which is used in other methods to make changes \
        to the database.
        """
        try:
            self.db = mysql.connector.connect(
                host= self.host,
                user= self.user,
                password= self.password,
                database= self.database
            )

            self.mycursor = self.db.cursor()

        except Exception as e:
            print(f"Error: {e}")

    def add_table(self, testdata):
        """
        This method creates a table/tables. After using the 'filter_pts' method on a TestPoints instance, \
        the instance returns a list of dataframes on which this method will base the tables on.
        E.g.: testpoints.filter_pts() -> testpoints.add_table().

        The name of the table depends on the fourth column name of the dataframe which is constructed \
        in the 'filter_pts' method.

        :param: Instance of TestPoints.filter_pts()

        :return: new tables in the database
        """
        try:
            for dataframe in testdata.dataframes_filtered:
                col1 = dataframe.columns[0]
                col2 = dataframe.columns[1]
                col3 = dataframe.columns[2]
                col4 = dataframe.columns[3]
                self.mycursor.execute(f"CREATE TABLE IF NOT EXISTS Function_{col4} " \
                                      f"({col1} FLOAT, " \
                                      f"{col2} FLOAT, " \
                                      f"{col3} FLOAT, " \
                                      f"{col4} FLOAT, " \
                                      f"UNIQUE ({col3}))")

        except AttributeError:
            print("Missing attribute. Check if 'filter_pts' has been used on TestPoint instance.")

    def delete_table(self, table_name=None, table_list=None):

        """
        This method is used to delete a specific table or multiple tables from the database.

        :param table_name: Name of the table to be deleted.

        :param table_list: Names of tables to be deleted as a list.
        """

        if table_list is not None:
            for table in table_list:
                delete_query = f"DROP TABLE {table}"
                self.mycursor.execute(delete_query)
                self.db.commit()
                print(f"Table '{table}' has been successfully deleted")

        else:
            delete_query = f"DROP TABLE {table_name}"
            self.mycursor.execute(delete_query)
            self.db.commit()
            print(f"Table '{table_name}' has been successfully deleted")


    def add_data(self,testdata):
        """
        The method is used to add data to tables that have been created by 'create_table'.
        It uses the data that is stored in the 'self.dataframes_filtered' attribute and puts the data \
        into the equivalent table.
        """

        for dataframe in testdata.dataframes_filtered:
            func_name = dataframe.columns[3]
            for index, values in dataframe.iterrows():
                x_test_val = float(values.iloc[0])
                y_test_val = float(values.iloc[1])
                delta_y_val = float(values.iloc[2])
                y_ideal_val = float(values.iloc[3])

                new_query = (f"INSERT IGNORE INTO Function_{func_name} \
                            (x_test, y_test, delta_y, {func_name}) VALUES (%s,%s,%s,%s)")

                self.mycursor.execute(new_query, (x_test_val, y_test_val, delta_y_val, y_ideal_val))

            self.db.commit()

    def delete_data(self,table_name=None, table_list= None):
        """
        Deletes all data from a table.

        :param table_name: Name of the table to be deleted

        :param table_list: List of names of tables to be deleted
        """

        if table_list is not None:
            for table in table_list:
                new_query = f"DELETE FROM {table}"
                self.mycursor.execute(new_query)
                self.db.commit()
                print(f"{table}'s data has been cleared")
        else:
            new_query = f"DELETE FROM {table_name}"
            self.mycursor.execute(new_query)
            self.db.commit()
            print(f"{table_name}'s data has been cleared")

    def table_names(self):
        """
        Creates a list of all the table names in the database

        :return: a list of table names
        """

        self.mycursor.execute("SHOW TABLES")
        tables = self.mycursor.fetchall()
        names = []

        for name in tables:
            names.append(name[0])

        return names

    def disconnect(self):
        """
        The method closes connection to the database
        """

        self.db.close()
        print("Successfully disconnected")





train_funcs = TrainFunctions(folder= "datensaetze", filename= "train.csv")
ideal_funcs = IdealFunctions(folder= "datensaetze", filename= "ideal.csv")
test_points = TestPoints(folder="datensaetze",filename="test.csv")

train_funcs.load()
ideal_funcs.load()
test_points.load()

train_funcs.find_bestfit(ideal=ideal_funcs)


test_points.filter_pts(train=train_funcs, ideal=ideal_funcs)

database = Database(host="localhost",user="Djahan",password="Mysql@4202",database="database_test")
database.connect()

#database.delete_table(table_name="function_y33")



