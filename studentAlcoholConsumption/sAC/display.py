from sAC.students import students
import pandas as pd
import matplotlib.pyplot as plt

class display:
    """
    This class compiles the data needed for displaying to the user
    """
    def __init__(self):
        """
        Arguments:
        self._display1 holds the plot output for displaying option 1
        self._display2 holds the plot output for displaying option 2
        self._display3 holds the plot output for displaying option 3
        self._students connects control to 'students' class object methods
        """
        self._students = students()
        self._display1 = self._init_display('1')
        self._display2 = self._init_display('2')
        self._display3 = self._init_display('3')
    
    def get_display(self, option):
        """
        Module to return the plot data for the chosen display
        """
        match option:
            case '1':
                x = ''
                y = ''
                kind = ''
                title = ''
                xlabel = ''
                ylabel = ''
                df = pd.DataFrame(self._display1)
                df.sort_values("Walc", axis=0, ascending=True, na_position='first')
                df.where(df["G1"]>0)
                df.plot()
            case '2':
                df = pd.DataFrame(self._display2)
                df.plot()
            case '3':
                df = pd.DataFrame(self._display3)
                df['Talc'] = df['Dalc']+df['Walc']
                df.sort_values("Talc", axis=0, ascending=True, inplace=True, na_position='first')
                TalcList = list(set(df['Talc'].tolist()))
                dsl = pd.DataFrame(TalcList)
                df = df[['famrel','Talc']]
                countList = []
                famCountList = []
                famrelList = []
                for item in TalcList:
                    countList.append(len(df[df['Talc'] == item]))
                for i in range(5):
                    famCountList.append(len(df[df['famrel'] == (i+1)]))
                    famrelList.append(df.where(df['famrel'] == (i+1)).sum())
                print(TalcList)
                print(countList)
                print(famCountList)
                print(famrelList)
                
                dff = pd.DataFrame(famrelList)
                # dff.set_index(pd.Index([1,2,3,4,5]))
                # df = df[['famrel','Talc']]
                # df = df.where(df['famrel'] == 5)
                # df['percent'] = (df['famrel'] / df['famrel'].sum()) * 100

                #This plot returns a pie graph showing proportions of student famrel ratings.
                dff.plot(kind='pie' , y='famrel', labels =[1,2,3,4,5])
                dff.plot(kind='box')

                #This plot returns a pie graph showing proportions of student Talc ratings
                #per range of famrel ratings.
                dff.plot(kind='pie' , y='Talc', labels = [1,2,3,4,5])
        plt.show()
    
    def _init_display(self, option):
        """
        Module to get the plot data for the chosen display
        """
        dataset = self._students.get_data(option)
        return dataset