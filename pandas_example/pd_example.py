import pandas as pd

class Demo():

    count = []

    def __init__(self, table):
        " Input datas <- csv tables "
        self.tab = self.__readCsv(table)
        self.tab_A = self.__groupBy(self.tab,'my_id')
        self.resInDataframe().to_excel("c:\\Python\\Python38-32\\myprojects\\pandas_example\\results\\avg.xlsx",sheet_name='Means')

    def __readCsv(self, csvfile):
        " Read csv file ... "
        return pd.read_csv(csvfile, sep=';', decimal='.', encoding="iso-8859-2")

    def __groupBy(self, df,by):
        " Means of grouped (groupby) numbers "
        self.count =list(df.groupby(by).size().values)
        df = df.groupby(by, as_index=False, sort=False).mean()
        return df.round(2)

    def resInDataframe(self):
        """ 1. Results go to dictionary
            2. Return value: pandas DataFrame """
        d = {'my_id': self.tab_A['my_id'], 'sample': self.count, 'my_value': self.tab_A['my_value']}
        df = pd.DataFrame(data=d)
        return df

    def main(self):
        print('\nMeans: ')
        print(self.resInDataframe())


if __name__ == "__main__":
    table = "c:\\Python\\Python38-32\\myprojects\\pandas_example\\my_table.csv" 
    c = Demo(table)
    c.main()