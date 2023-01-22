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
        Case 1: comparing alcohol consumption to grades
        Case 2: comparing alcohol consumption to free time and going out
        Case 3: comparing alcohol consumption to family size
        """
        match option:
            case '1':
                df = pd.DataFrame(self._display1)
                df['Talc'] = df['Dalc']+df['Walc']
                df['Grades'] = df['G1']+df['G2']+df['G3']
                df = df[['Talc', 'Grades']]
                df = df.where(df['Grades'] > 10)
                df = df.sort_values(by=['Talc'])
                df = df.reset_index(drop=True)
                df = df.groupby('Talc').agg(Grades=('Grades', 'mean'))
                df.plot(xlabel='Total Alcohol Consumption', ylabel='Averge Grades', color='r', title='Grades by Alcohol Consuption', linewidth='5')
            case '2':
                df = pd.DataFrame(self._display2)
                df['Talc'] = df['Dalc']+df['Walc']
                df['Free'] = df['freetime']+df['goout']
                df = df[['Free', 'Talc']]
                fig, axes = plt.subplots(nrows=2, ncols=1)
                df = df.sort_values(by=['Free'])
                df = df.reset_index(drop=True)
                df['Free'].plot(ax=axes[0])
                df['Talc'].plot(ax=axes[1])
                df = df.groupby('Free').agg(Freetime=('Talc', 'mean'))
                df = df.reset_index(drop=True)
                df.plot()
            case '3':
                df = pd.DataFrame(self._display3)
                df['Talc'] = df['Dalc']+df['Walc']
                df = df[['famsize', 'Talc']]
                df = df.groupby('famsize').agg(Alcohol_avg=('Talc', 'mean'))
                df = df.reset_index(drop=True)
                df = df.rename(index={0: ">3", 1: "<=3"})
                df.plot(kind='bar', xlabel='Family Size')
        plt.show()
    
    def _init_display(self, option):
        """
        Module to get the plot data for the chosen display
        """
        dataset = self._students.get_data(option)
        return dataset