import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
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


# Construction of class dashboard, blueprint for Customer Service and HR dashboards
class dashboard(QMainWindow):
    def __init__(self, windowTitle: str, entities: dict) -> None:
        super().__init__()

        # set the window title
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
        # department specific entities
        self.entities = entities


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
        self.buttons = [
            QPushButton(entity, clicked=lambda: self.open(self.entities[entity]))  # type: ignore
            for entity in self.entities
        ]

        # TOOL LABEL
        self.toolLabel = QLabel("Tools")
        self.toolLabel.setFont(QFont("Century", 16))
        self.toolLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Push button for Data Query Wizard
        self.dataQueryWizardButton = QPushButton("Data Query Wizard", clicked=lambda: self.dataQueryWizard())  # type: ignore
        self.dataQueryWizardButton.setIcon(QIcon("./assets/query.png"))

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
        for button in self.buttons:
            layout.addWidget(button)

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
        ####################################

    ##################### BUTTON FUNCTIONS #####################

    def open(self, entityWindow):
        window = entityWindow()
        self.hide()
        window.show()

    # Push button for Data Query Wizard
    def dataQueryWizard(self):
        self.queryInterface = queryInterface()
        self.hide()
        self.queryInterface.show()

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

    ##################### center function #####################
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

    # END OF dashboard class


csEntities = {
    "Customers": customers,
    "Accounts": accounts,
    "Cards": cards,
    "Transactions": transactions,
    "Loans": loans,
    "Loan Payments": loansPayment
}


class cusServDashboard(dashboard):
    def __init__(self):
        super().__init__(
            windowTitle= "Customer Service Dashboard",
            entities= csEntities
        )


if __name__ == "__main__":
    try:
        # Include in try/except block if you're also targeting Mac/Linux
        from ctypes import windll  # only exists on Windows

        myappid = "mycompany.myproduct.subproduct.version"
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    # except ImportError:
    # pass
    finally:
        # create the QApplication object
        app = QApplication(sys.argv)

        # create the main window
        cusdashwindow = cusServDashboard()

        # show the window
        cusdashwindow.show()

        # DARK THEME
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())
