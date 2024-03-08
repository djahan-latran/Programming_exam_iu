from df_constructor import DfConstructor
from file_loader import FileLoader
# from data_analyzer import DataAnalyzer
# from database import DataBase
# from visualization import Graphics


class ProgramExecutor:

    def execute_program(self):

        file_loader = FileLoader(foldername="datensaetze", filename="train.csv")
        train_data = file_loader.load_and_construct_file()
        for index, data in train_data.iterrows():
            print(index,data)
            break

if __name__ == "__main__":
    program = ProgramExecutor()
    program.execute_program()