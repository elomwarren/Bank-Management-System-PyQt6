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
        self.setWindowIcon(QIcon("./assets/bank.png"))

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
        self.dashboardLabel = QLabel('DASHBOARD')
        self.dashboardLabel.setFont(QFont("Century", 28))
        self.dashboardLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Entities Label
        self.entitiesLabel = QLabel('Entities')
        self.entitiesLabel.setFont(QFont("Century", 16))
        self.entitiesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ### Push buttons for entities ###

        # titles = ['Employees', 'Jobs', 'Departments', 'Branches', 'Locations', 'Regions']
        # buttons = [QPushButton(title) for title in titles]

        self.employeesButton = QPushButton('Employees', clicked=lambda: self.open_employees())  # type: ignore

        self.jobsButton = QPushButton('Jobs', clicked=lambda: self.open_jobs())  # type: ignore

        self.departmentsButton = QPushButton('Departments', clicked=lambda: self.open_departments())  # type: ignore

        self.branchesButton = QPushButton('Branches', clicked=lambda: self.open_branches())  # type: ignore

        self.locationsButton = QPushButton('Locations', clicked=lambda: self.open_locations())  # type: ignore

        self.regionsButton = QPushButton('Regions', clicked=lambda: self.open_regions())  # type: ignore

        
        # Tool label
        self.toolLabel = QLabel('Tools')
        self.toolLabel.setFont(QFont("Century", 16))
        self.toolLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # PUSH BUTTON FOR DATA QUERY WIZARD
        self.dataQueryWizardButton = QPushButton('Data Query Wizard', clicked=lambda: self.dataQueryWizard())  # type: ignore
        self.dataQueryWizardButton.setIcon(QIcon("./assets/query.png"))

        # LOGOUT PUSH BUTTON
        self.logoutButton = QPushButton('Logout', clicked=lambda: self.logout())  # type: ignore
        
        # quit button
        self.quitButton = QPushButton('Quit', clicked = lambda: self.quit()) # type: ignore
        ####################### END OF ADD WIDGETS #######################


        ############################ LAYOUT ############################

        layout = QVBoxLayout() 

        ### ADD WIDGETS TO LAYOUT ###

        # DASHBOARD LABEL
        layout.addWidget(self.dashboardLabel)

        # set space after Dashboard label
        layout.addSpacing(15)

        # Entities Label
        layout.addWidget(self.entitiesLabel)

        # Push buttons for entities
        layout.addWidget(self.employeesButton)
        layout.addWidget(self.jobsButton)
        layout.addWidget(self.departmentsButton)
        layout.addWidget(self.branchesButton)
        layout.addWidget(self.locationsButton)
        layout.addWidget(self.regionsButton)

        # Tool label
        layout.addWidget(self.toolLabel)

        # Push button for Data Query Wizard
        layout.addWidget(self.dataQueryWizardButton)

        # set space after Data Query Wizard button
        layout.addSpacing(20)

        # Logout Push button
        layout.addWidget(self.logoutButton)
        
        # Quit Push button
        layout.addWidget(self.quitButton)

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

    def open_employees(self):
        # print('Employees')
        self.employees = employees()
        self.hide()
        self.employees.show()

    def open_jobs(self):
        # print('Jobs')
        self.jobs = jobs()
        self.hide()
        self.jobs.show()

    def open_departments(self):
        # print('Departments')
        self.departments = departments()
        self.hide()
        self.departments.show()

    def open_branches(self):
        # print('Branches')
        self.branches =  branches()
        self.hide()
        self.branches.show()

    def open_locations(self):
        # print('Locations')
        self.locations = locations()
        self.hide()
        self.locations.show()

    def open_regions(self):
        # print('Regions')
        self.regions = regions()
        self.hide()
        self.regions.show()

    # Push button for Data Query Wizard
    def dataQueryWizard(self):
        # print('Data Query Wizard')
        self.queryInterface = queryInterface()
        self.hide()
        self.queryInterface.show()

    # Logout Push button
    def logout(self):
        # print('Logout')
        from win_01_WelcomeLogin import welcome
        self.welcome = welcome()
        self.hide()
        self.welcome.show()

    # Quit button
    def quit(self):
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
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())