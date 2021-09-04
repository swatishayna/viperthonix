import pyinputplus as pyip


import pandas as pd


def main():
    path = input("Enter path")
    class Dataframe:
        def __init__(self, path):
            self.path = path
            self.delimiter = ','
        def load(self):
            """
                This will load and read your csv file. Provide your datafile here
                :return:
                """
            return pd.read_csv(self.path)
    df = Dataframe(path).load()

    def head(df):
        """
        This will read the top rows of the dataset
        :param df:
        :return:
        """

        number_of_rows = int(input("Enter the number of rows "))
        try:
            print(df.head(number_of_rows))
        except IndexError as e:
            print(e)
            do(df)

    def tail(df):
        """
        This will read the last rows of the dataset
        :param df:
        :return:
        """
        number_of_rows = int(input("Enter the number of rows "))
        try:
            print(df.head(number_of_rows))
        except IndexError as e:
            print(e)
            do(df)

    def shape(df):
        print(df.shape)

    def describe(df):
        def selected():
            print(df.columns)
            f = list(input("Enter the names of columns: Follow cases").split(","))
            try:
                print(df.loc[:, f].describe())
            except Exception as e:
                print("invalid", e)

        def all():
            print(df.describe())

        def all_cat():
            print(df[df.dtypes[df.dtypes == 'object'].index].describe())

        choice = pyip.inputMenu(
            ['describe selected column', "describe all columns", "describe all categorical columns"], numbered=True)
        if choice == "describe selected column":
            print(selected())
        elif choice == "describe all columns":
            print(all())
        else:
            print(all_cat())

    def datatype(df):
        choice = pyip.inputMenu(("Dataframe", "Selected columns"), numbered=True)
        if choice == "Dataframe":
            print(df.dtypes)
        if choice == "Selected columns":
            print(df.columns)
            colnames = list(input("Enter the names of the columns-FollowCases").split(","))
            data_Types = df.loc[:, colnames].dtypes
            print(data_Types)

    def info(df):
        print(df.info)

    def do(df):

        choices = ("head", "tail", "View shape of the DataFrame", "View DataTypes of DataFrame-Columns",
                   "View info of the DataFrame", "describe the DataFrame", "View Categories of columns")

        choice = pyip.inputMenu(choices, numbered=True)
        if choice == "head":
            head(df)
        elif choice == "tail":
            tail(df)
        elif choice == "View shape of the DataFrame":
            shape(df)
        elif choice == "View DataTypes of DataFrame-Columns":
            datatype(df)
        elif choice == "View info of the DataFrame":
            info(df)
        elif choice == "describe the DataFrame":
            describe(df)

    def studydf(df):
        choice = ["Basic", "Advanced", "Visualization"]
        action = pyip.inputMenu(choice, numbered=True)
        if action == "Basic":
            do(df)
        # elif action == "Advanced":
        #     Advanced.do(df)
        # else:
        #     Visual.do(df)

    while True:
        decision = pyip.inputMenu(["NO", "YES"], prompt="do you want to analyse data", numbered=True)
        if decision == "YES":
            studydf(df)
        else:
            break



if __name__ == '__main__':
    main()






