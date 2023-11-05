from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication

# import the necessary modules from other windows
from win_02_3_QueryInterface_CS import queryInterface
from win_03_1_1_CusTable import customers
from win_03_1_2_AccTable import accounts
from win_03_1_3_CardsTable import cards
from win_03_1_4_TxnTable import transactions
from win_03_1_5_LoansTable import loans
from win_03_1_6_LnpayTable import loansPayment

# other modules
import qdarktheme
import sys
import os


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Construction of class dashboard, blueprint for Customer Service and HR dashboards
class dashboard(QMainWindow):
    def __init__(self,  dep: str):
        super().__init__()

        self.dep = dep
        # set the window title
        self.setWindowTitle("Dashboard")

        # set WINDOW ICON (icons from icons8.com)
        self.setWindowIcon(QIcon(resource_path("./assets/bank.png")))

        # Set window size
        width = 800
        height = 600
        self.resize(width, height)

        # center the window, center function defined below
        self.center()

        # initilize other windows member to None
        self.welcome = None
        self.queryInterface = None

        # CREATE THE USER INTERFACE
        self.initUI()

    def initUI(self):
        """
        Initializes the customers window.
        """
        ######################### CREATE WIDGETS #########################
        # Dashboard label
        self.dashboardLabel = QLabel("DASHBOARD")
        self.dashboardLabel.setFont(QFont("Century", 28))
        self.dashboardLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Entities Label
        self.label = QLabel("Entities")
        self.label.setFont(QFont("Century", 16))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ### Push buttons for entities ###
        self.button1 = QPushButton("Button 1")  # type: ignore
        self.button2 = QPushButton("Button 2")  # type: ignore
        self.button3 = QPushButton("Button 3")  # type: ignore
        self.button4 = QPushButton("Button 4")  # type: ignore
        self.button5 = QPushButton("Button 5")  # type: ignore
        self.button6 = QPushButton("Button 6")  # type: ignore

        # TOOL LABEL
        self.toolLabel = QLabel("Tools")
        self.toolLabel.setFont(QFont("Century", 16))
        self.toolLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Push button for Data Query Wizard
        self.dataQueryWizardButton = QPushButton("Data Query Wizard", clicked=lambda: self.dataQueryWizard())  # type: ignore
        self.dataQueryWizardButton.setIcon(QIcon(resource_path("./assets/query.png")))

        # Logout Push button
        self.logoutButton = QPushButton("Logout", clicked=lambda: self.logout())  # type: ignore

        # quit button
        self.quitButton = QPushButton("Quit", clicked=lambda: self.quit())  # type: ignore
        ####################### END OF ADD WIDGETS #######################

        ############################ LAYOUT ############################
        layout = QVBoxLayout()

        ### ADD WIDGETS TO LAYOUT ###

        # Dashboard label
        layout.addWidget(self.dashboardLabel)

        # set space after Dashboard label
        layout.addSpacing(15)

        # Entities Label
        layout.addWidget(self.label)

        # Push buttons for entities
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)

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
        layout.setContentsMargins(250, 150, 250, 75)  # left, top, right, bottom

        ### Center window content ###
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        ############################# END OF LAYOUT #############################

    ##################### BUTTON FUNCTIONS #####################
    # OPEN WINDOW function
    def open(self, entityWindow):
        """
        Takes the class of a window to be opened as an argument,
        creates an instance of that class
        and opens it.
        """
        window = entityWindow()
        self.hide()
        window.show()

    # Push button for Data Query Wizard
    def dataQueryWizard(self):
        from win_02_3_QueryInterface_CS import queryInterface, CSqueryInterface
        from win_02_3_QueryInterface_HR import HRqueryInterface

        if self.dep == "CS":
            self.CSqueryInterface = CSqueryInterface()
            self.hide()
            self.CSqueryInterface.show()
        if self.dep == "HR":
            self.HRqueryInterface = HRqueryInterface()
            self.hide()
            self.HRqueryInterface.show()

    # Logout Push button
    def logout(self):
        from win_01_WelcomeLogin import welcome

        self.welcome = welcome()
        self.hide()
        self.welcome.show()

    # Quit button
    def quit(self):
        self.close()

    ##################### END OF BUTTON FUNCTIONS #####################

    ############################### CENTER FUNCTION ###############################
    def showEvent(self, event):
        self.center()
        super().showEvent(event)

    def center(self):
        frame = self.frameGeometry()
        screen = QGuiApplication.primaryScreen()
        center = screen.availableGeometry().center()  # type: ignore
        frame.moveCenter(center)
        x = min(frame.topLeft().x(), screen.availableGeometry().right() - frame.width())  # type: ignore
        y = min(frame.topLeft().y(), screen.availableGeometry().bottom() - frame.height())  # type: ignore
        self.move(x, y)

    ############################# END OF CENTER FUNCTION #############################
    # END OF DASHBOARD CLASS


class cusServDashboard(dashboard):
    def __init__(self):
        super().__init__(dep="CS")

        # set the window title
        self.setWindowTitle("WEL Bank - Customer Service Dashboard")
        # Modify the existing buttons and connect their clicked signal
        self.button1.setText("Customers")
        self.button1.clicked.connect(lambda: self.open(customers))

        self.button2.setText("Accounts")
        self.button2.clicked.connect(lambda: self.open(accounts))

        self.button3.setText("Cards")
        self.button3.clicked.connect(lambda: self.open(cards))

        self.button4.setText("Transactions")
        self.button4.clicked.connect(lambda: self.open(transactions))

        self.button5.setText("Loans")
        self.button5.clicked.connect(lambda: self.open(loans))

        self.button6.setText("Loan Payments")
        self.button6.clicked.connect(lambda: self.open(loansPayment))


if __name__ == "__main__":
    try:
        # Include in try/except block if you're also targeting Mac/Linux
        from ctypes import windll  # only exists on Windows

        myappid = "mycompany.myproduct.subproduct.version"
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    finally:
        app = QApplication(sys.argv)
        cusdashwindow = cusServDashboard()
        cusdashwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
