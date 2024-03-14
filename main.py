from data_analyzer import DataAnalyzer
from database import DatabaseManager
from visualization import Graphics


class ProgramExecutor:

    def execute_program(self):

        #initialize DataAnalzyer instance and set up attributes for file loading
        data = DataAnalyzer(train_folder="datensaetze", train_file="train.csv",
                            ideal_folder="datensaetze", ideal_file="ideal.csv",
                            test_folder="datensaetze", test_file="test.csv"
                            )
        # load the train and ideal data
        data.load_train_data()
        # data.load_ideal_data()
        #
        # # find the best fit's
        # data.find_bestfit()
        #
        # # initialize Graphics instance
        # graphics = Graphics()
        #
        # # plot the train and best-fit data
        # graphics.plot_train_data(data= data)
        # graphics.plot_bestfit(data= data)
        #
        # # load the test data
        # data.load_test_data()
        #
        # # validate the testpoints
        # data.test_point_validation()
        #
        #
        #
        # graphics.plot_test_data(data= data)
        # graphics.plot_filtered_test_data(data= data)
        #
        # db_manager = DatabaseManager(database_name="database")
        # db_manager.create_train_table_from_df(data= data)
        # db_manager.create_ideal_table_from_df(data= data)
        # db_manager.create_validation_table_from_df(data= data)


if __name__ == "__main__":
    program = ProgramExecutor()
    program.execute_program()