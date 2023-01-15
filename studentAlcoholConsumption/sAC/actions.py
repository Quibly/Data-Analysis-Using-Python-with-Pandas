from sAC.display import display

class actions:
    """
    This class is used to implement the choices of the user
    """
    def __init__(self):
        """"
        Arguments:
        self._command holds the variable for user input
        """
        self._command = ''
        self._display = display()
    
    def use_input(self, command):
        """
        Module to control program action based on user input
        """
        self._command = command
        match self._command:
            case '1':
                self._display.get_display(self._command)
            case '2':
                self._display.get_display(self._command)
            case '3':
                self._display.get_display(self._command)

