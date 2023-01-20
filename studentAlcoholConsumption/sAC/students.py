import pandas as pd
import matplotlib.pyplot as plt

class students:
    """
    This is a class to handle the formatting of data files and data manipulation
    """
    def __init__(self):
        """
        Arguments:
        self._math is a variable to hold math dataset
        self._port is a variable to hold portugese dataset
        """
        self._math = pd.read_csv('studentAlcoholConsumption\sAC\source\student-mat.csv')
        self._port = pd.read_csv('studentAlcoholConsumption\sAC\source\student-por.csv')
        self._both = ''
        self._grades = ''
        self._freetime = ''
        self._family = ''
        self._concat_frames()

    def get_data(self,option):
        """
        A module to get dataset for plotting
        """
        match str(option):
            case '1':
                dataset = self._get_grades_data()
                return dataset
            case '2':
                dataset = self._get_freetime_data()
                return dataset
            case '3':
                dataset = self._get_family_data()
                return dataset
        

    def _get_grades_data(self):
        """
        A module to get data for grades comparison
        """
        temp = self._both[['Dalc', 'Walc', 'schoolsup', 'G1', 'G2', 'G3']]
        return temp

    def _get_freetime_data(self):
        """
        A module to get data for free time and going out comparison
        """
        temp = self._both[['Dalc', 'Walc', 'freetime', 'goout', 'absences']]
        return temp

    def _get_family_data(self):
        """
        A module to get data for family comparison
        """
        temp = self._both[['Dalc', 'Walc', 'famsize', 'Pstatus', 'famsup', 'famrel']]
        return temp

    def _concat_frames(self):
        """
        A module to combine Pandas DataFrames
        """
        result = pd.concat([self._math, self._port], ignore_index=True)
        self._both = result
