from df_constructor import DfConstructor
from file_loader import FileLoader
from data_analyzer import DataAnalyzer
# from database import DataBase
from visualization import Graphics


class ProgramExecutor:

    def execute_program(self):

        data = DataAnalyzer(train_folder="datensaetze", train_file="train.csv",
                            ideal_folder="datensaetze", ideal_file="ideal.csv",
                            test_folder="datensaetze", test_file="test.csv"
                            )

        data.load_train_data()
        data.load_ideal_data()

        data.find_bestfit()

        graphics = Graphics()


        graphics.plot_train_data(data= data)
        graphics.plot_bestfit(data= data)


        data.load_test_data()
        data.test_point_validation()

        graphics.plot_test_data(data= data)
        graphics.plot_filtered_test_data(data= data)


if __name__ == "__main__":
    program = ProgramExecutor()
    program.execute_program()