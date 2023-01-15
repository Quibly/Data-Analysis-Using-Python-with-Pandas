import pandas as pd

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
        return self._math

    def _get_freetime_data(self):
        """
        A module to get data for free time and going out comparison
        """
        return self._math

    def _get_family_data(self):
        """
        A module to get data for family comparison
        """
        return self._math
