import pandas as pd


class groupData():
    
    def __init__(self, table,colname):
        " Input datas <- csv tables "
        self.col = colname
        self.tab = self.__readCsv(table)
        " Counting used by groupby method "
        # Sample number of set
        self.sample = list(self.tab.groupby(self.col).size().values)
        # Get minimum value of set
        self.tab_MIN = self.__group(self.tab,self.col).min().round(2)
        # Get maximum value of set   
        self.tab_MAX = self.__group(self.tab,self.col).max().round(2)
        # Get mean
        self.tab_MEAN = self.__group(self.tab,self.col).mean().round(2)
        # Get standart deviation
        self.tab_STD = self.__group(self.tab,self.col).std().round(2)

        # You can add more pandas statistical functions here ...

        " Save datas to excel file with sheet name 'results' "        
        self.resInDataframe().to_excel("c:\\Python\\Python38-32\\mycodes\\pandas_example2\\results.xlsx",sheet_name='results')


    def __readCsv(self, csvfile):
        " Read csv file ... "
        return pd.read_csv(csvfile, sep=';', decimal=',', encoding="iso-8859-2")

    def __group(self, df,by):
        " Grouped (groupby) values by column name "
        return df.groupby(by, as_index=False, sort=False)
        
    def resInDataframe(self):
        # Results go to dictionary
        # Columns: table name, sum of samples, maximum value, minimum value, mean, standard deviation, coefficient of variation: (std/mean)*100
        # Return value: pandas DataFrame    
        d = {
            'Tábla': self.tab_MEAN['TÁBLA'], 'Adatszám': self.sample, \

            # You can add more lines <- columns here ...
        
            'Na_min': self.tab_MIN['Na'], 'Na_max': self.tab_MAX['Na'], 'Na_mean': self.tab_MEAN['Na'], 'Na_std': self.tab_STD['Na'], 'Na_CV%': ((self.tab_STD['Na'] / self.tab_MEAN['Na'])*100).round(2), \
            'Mg_min': self.tab_MIN['Mg'], 'Mg_max': self.tab_MAX['Mg'], 'Mg_mean': self.tab_MEAN['Mg'], 'Mg_std': self.tab_STD['Mg'], 'Mg_CV%': ((self.tab_STD['Mg'] / self.tab_MEAN['Mg'])*100).round(2), \
            'Zn_min': self.tab_MIN['Zn'], 'Zn_max': self.tab_MAX['Zn'], 'Zn_mean': self.tab_MEAN['Zn'], 'Zn_std': self.tab_STD['Zn'], 'Zn_CV%': ((self.tab_STD['Zn'] / self.tab_MEAN['Zn'])*100).round(2), \
            'Cu_min': self.tab_MIN['Cu'], 'Cu_max': self.tab_MAX['Cu'], 'Cu_mean': self.tab_MEAN['Cu'], 'Cu_std': self.tab_STD['Cu'], 'Cu_CV%': ((self.tab_STD['Cu'] / self.tab_MEAN['Cu'])*100).round(2), \
            'Mn_min': self.tab_MIN['Mn'], 'Mn_max': self.tab_MAX['Mn'], 'Mn_mean': self.tab_MEAN['Mn'], 'Mn_std': self.tab_STD['Mn'], 'Mn_CV%': ((self.tab_STD['Mn'] / self.tab_MEAN['Mn'])*100).round(2) \
        }
        df = pd.DataFrame(data=d)
        return df


if __name__ == "__main__":
    
    # path of input csv file
    table = "c:\\Python\\Python38-32\\mycodes\\pandas_example2\\data.csv" 
    # group by this column name
    colname = 'TÁBLA' 
    
    c = groupData(table,colname)
    
    # results on console
    print(c.resInDataframe())