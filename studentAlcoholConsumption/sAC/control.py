from sAC.actions import actions

class control:
    """
    This is the main class for the program.

    This class organizes the menu for the program.
    """
    def __init__(self):
        """
        Arguments:
        self._actions connects control to 'actions' class object methods
        self._exit is a variable for signifying the end of the program
        """
        self._actions = actions()
        self._exit = False
        self._command = ''
    
    def start_menu(self):
        """
        Method for controlling the flow of the software.
        The method starts the program and data conversion to objects
        and connects the user to options to view the table output of their choice.
        """
        while self._exit == False:
        # while self._students.exist and self._exit == False:
            self._display_menu()
            if self._command == 'Exit':
                self._exit = True
            else:
                self._actions.use_input(self._command)

    def _display_menu(self):
        """
        Method for prompting the user about what they want to display.
        When an input is received the program will either display
        a graph/chart or exit the program.
        """
        menu = ("""
        Please choose a graph to display:
            1: Comparison to Grades
            2: Comparison to Free time and Going out durations
            3: Comparison to family demographics

            Exit: Exit the program

            Type 1, 2, 3, or Exit
        """)
        command = input(menu)
        if command in ('1','2','3','Exit'):
            self._command = command
        else:
            self._display_menu()