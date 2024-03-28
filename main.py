from data_analyzer import DataAnalyzer
from database import DatabaseManager
from visualization import Graphics
from df_constructor import DfConstructor


class ProgramExecutor:

    def execute_program(self):

        # initialize DataAnalyzer instance and set up attributes for file loading
        data = DataAnalyzer(train_folder="datensaetze", train_file="train.csv",
                            ideal_folder="datensaetze", ideal_file="ideal.csv",
                            test_folder="datensaetze", test_file="test.csv"
                           )

        # loading all data sets
        data.load_train_data()
        data.load_ideal_data()
        data.load_test_data()

        # analyzing the data by finding the best fit functions \
        # and validate with test points
        data.find_bestfit()
        data.test_point_validation()

        # visualizing the data and saving it in a sqlite database
        visual = Graphics()
        visual.plot_train_data(data=data)
        visual.plot_bestfit(data=data)
        visual.plot_test_data(data=data)
        visual.plot_filtered_test_data(data=data)
        database = DatabaseManager(database_name="database_final")
        database.create_train_table_from_df(data=data)
        database.create_ideal_table_from_df(data=data)
        database.create_validation_table_from_df(data=data)


if __name__ == "__main__":
    program = ProgramExecutor()
    program.execute_program()