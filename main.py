from data_analyzer import DataAnalyzer
from database import DatabaseManager
from visualization import Graphics


class ProgramExecutor:
    """A class that runs the program

    Methods:
        execute_program: runs the program
    """

    def execute_program(self):
        """Contains the algorithm to successfully get and visualize
        all the data that is requested in the assignment.
        """

        # initialize DataAnalyzer instance and set up attributes for file loading
        data = DataAnalyzer(train_folder="datensaetze", train_file="train.csv",
                            ideal_folder="datensaetze", ideal_file="ideal.csv",
                            test_folder="datensaetze", test_file="test.csv"
                           )

        # load all data sets
        data.load_train_data()
        data.load_ideal_data()
        data.load_test_data()

        # analyze the data by finding the best-fit functions
        data.find_bestfit()

        # filter the test points and assign one of the best-fit functions to each point
        data.test_point_validation()

        # visualize the data
        visual = Graphics()
        visual.plot_train_data(data=data)
        visual.plot_bestfit(data=data)
        visual.plot_test_data(data=data)
        visual.plot_filtered_test_data(data=data)

        # save the data in a local sqlite database
        database = DatabaseManager(database_name="database_final")
        database.create_train_table_from_df(data=data)
        database.create_ideal_table_from_df(data=data)
        database.create_validation_table_from_df(data=data)


if __name__ == "__main__":
    program = ProgramExecutor()
    program.execute_program()
