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
                df = pd.DataFrame(self._display1)
                df.plot()
            case '2':
                df = pd.DataFrame(self._display2)
                df.plot()
            case '3':
                df = pd.DataFrame(self._display3)
                df.plot()
        plt.show()
    
    def _init_display(self, option):
        """
        Module to get the plot data for the chosen display
        """
        dataset = self._students.get_data(option)
        return dataset