from df_constructor import DfConstructor
from file_loader import FileLoader
from data_analyzer import DataAnalyzer
# from database import DataBase
# from visualization import Graphics


class ProgramExecutor:

    def execute_program(self):

        data = DataAnalyzer(train_folder="datensaetze", train_file="train.csv",
                            ideal_folder="datensaetze", ideal_file="ideal.csv")
        train_data = data.load_train_data()
        ideal_data = data.load_ideal_data()
        print(train_data)

if __name__ == "__main__":
    program = ProgramExecutor()
    program.execute_program()