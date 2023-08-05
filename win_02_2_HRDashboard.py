from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication


# import the necessary modules from other windows
from win_02_3_QueryInterface_HR import queryInterface
from win_03_2_1_empTable import employees
from win_03_2_2_jobsTable import jobs
from win_03_2_3_depTable import departments
from win_03_2_4_brchTable import branches
from win_03_2_5_locTable import locations
from win_03_2_6_regTable import regions

# other modules
import qdarktheme
import sys


class hrDashboard(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        windowTitle = 'HR Dashboard'
        self.setWindowTitle(windowTitle)

        # set WINDOW ICON (icons from icons8.com)
        self.setWindowIcon(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/dashboard.png'))

        # Set window size 
        width = 800
        height = 600
        self.resize(width, height)

        # center the window, center function defined below
        self.center()

        # initilize other windows member to None
        self.welcome = None
        self.queryInterface = None
        self.employees = None
        self.jobs = None
        self.departments = None
        self.branches = None
        self.locations = None
        self.regions = None

        # CREATE THE USER INTERFACE
        self.initUI()

    # user interface function
    def initUI(self):

        ######################### ADD WIDGETS #########################

        # Dashboard label
        dashboardLabel = QLabel('DASHBOARD')
        dashboardLabel.setFont(QFont("Century", 28))
        dashboardLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Entities Label
        entitiesLabel = QLabel('Entities')
        entitiesLabel.setFont(QFont("Century", 16))
        entitiesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ### Push buttons for entities ###

        # titles = ['Employees', 'Jobs', 'Departments', 'Branches', 'Locations', 'Regions']
        # buttons = [QPushButton(title) for title in titles]

        employeesButton = QPushButton('Employees', clicked=lambda: open_employees())  # type: ignore

        jobsButton = QPushButton('Jobs', clicked=lambda: open_jobs())  # type: ignore

        departmentsButton = QPushButton('Departments', clicked=lambda: open_departments())  # type: ignore

        branchesButton = QPushButton('Branches', clicked=lambda: open_branches())  # type: ignore

        locationsButton = QPushButton('Locations', clicked=lambda: open_locations())  # type: ignore

        regionsButton = QPushButton('Regions', clicked=lambda: open_regions())  # type: ignore

        
        # Tool label
        toolLabel = QLabel('Tools')
        toolLabel.setFont(QFont("Century", 16))
        toolLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # PUSH BUTTON FOR DATA QUERY WIZARD
        dataQueryWizardButton = QPushButton('Data Query Wizard', clicked=lambda: dataQueryWizard())  # type: ignore
        dataQueryWizardButton.setIcon(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/query.png'))

        # LOGOUT PUSH BUTTON
        logoutButton = QPushButton('Logout', clicked=lambda: logout())  # type: ignore
        
        # quit button
        quitButton = QPushButton('Quit', clicked = lambda: quit()) # type: ignore
        ####################### END OF ADD WIDGETS #######################


        ############################ LAYOUT ############################

        layout = QVBoxLayout() 

        ### ADD WIDGETS TO LAYOUT ###

        # DASHBOARD LABEL
        layout.addWidget(dashboardLabel)

        # set space after Dashboard label
        layout.addSpacing(15)

        # Entities Label
        layout.addWidget(entitiesLabel)

        # Push buttons for entities
        layout.addWidget(employeesButton)
        layout.addWidget(jobsButton)
        layout.addWidget(departmentsButton)
        layout.addWidget(branchesButton)
        layout.addWidget(locationsButton)
        layout.addWidget(regionsButton)

        # Tool label
        layout.addWidget(toolLabel)

        # Push button for Data Query Wizard
        layout.addWidget(dataQueryWizardButton)

        # set space after Data Query Wizard button
        layout.addSpacing(20)

        # Logout Push button
        layout.addWidget(logoutButton)
        
        # Quit Push button
        layout.addWidget(quitButton)

        ### SET CONTENT MARGINS ###
        layout.setContentsMargins(250, 150, 250, 75) # left, top, right, bottom

        # Set the layout        
        # self.setLayout(layout)
        ########################################

        ### Center window content ###
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        ####################################


        ##################### BUTTON FUNCTIONS #####################

        def open_employees():
            # print('Employees')
            self.employees = employees()
            self.hide()
            self.employees.show()

        def open_jobs():
            # print('Jobs')
            self.jobs = jobs()
            self.hide()
            self.jobs.show()

        def open_departments():
            # print('Departments')
            self.departments = departments()
            self.hide()
            self.departments.show()

        def open_branches():
            # print('Branches')
            self.branches =  branches()
            self.hide()
            self.branches.show()

        def open_locations():
            # print('Locations')
            self.locations = locations()
            self.hide()
            self.locations.show()

        def open_regions():
            # print('Regions')
            self.regions = regions()
            self.hide()
            self.regions.show()

        # Push button for Data Query Wizard
        def dataQueryWizard():
            # print('Data Query Wizard')
            self.queryInterface = queryInterface()
            self.hide()
            self.queryInterface.show()

        # Logout Push button
        def logout():
            # print('Logout')
            from win_01_WelcomeLogin import welcome
            self.welcome = welcome()
            self.hide()
            self.welcome.show()

        # Quit button
        def quit():
            self.close()

        ##################### END OF BUTTON FUNCTIONS #####################

    ##################### CENTER FUNCTION #####################
    def showEvent(self, event):
        self.center()
        super().showEvent(event)

    def center(self):
        frame = self.frameGeometry()
        screen = QGuiApplication.primaryScreen()
        center = screen.availableGeometry().center() # type: ignore
        frame.moveCenter(center)
        x = min(frame.topLeft().x(), screen.availableGeometry().right() - frame.width()) # type: ignore
        y = min(frame.topLeft().y(), screen.availableGeometry().bottom() - frame.height()) # type: ignore
        self.move(x, y)

    ############################# END OF CENTER FUNCTION #############################


if __name__ == '__main__':

    try:
        # Include in try/except block if you're also targeting Mac/Linux
        from ctypes import windll # only exists on Windows
        myappid = 'mycompany.myproduct.subproduct.version'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    # except ImportError:
        # pass
    finally:
        # create the QApplication object
        app = QApplication(sys.argv)

        # create the main window
        hrdashwindow = hrDashboard()

        # show the window
        hrdashwindow.show()

        # DARK THEME
        # https://pypi.org/project/pyqtdarktheme/
        # pip install pyqtdarktheme
        # Apply the complete dark theme to Qt App.
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())