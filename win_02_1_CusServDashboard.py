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


class cusServDashboard(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        windowTitle = "Customer Service Dashboard"
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
        self.customers = None
        self.accounts = None
        self.cards = None
        self.transactions = None
        self.loans = None
        self.loansPayment = None

        # CREATE THE USER INTERFACE
        self.initUI()

    # user interface function
    def initUI(self):
        ######################### ADD WIDGETS #########################

        # Dashboard label
        self.dashboardLabel = QLabel("DASHBOARD")
        self.dashboardLabel.setFont(QFont("Century", 28))
        self.dashboardLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Entities Label
        self.entitiesLabel = QLabel("Entities")
        self.entitiesLabel.setFont(QFont("Century", 16))
        self.entitiesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ### Push buttons for entities ###

        self.cusButton = QPushButton("Customers", clicked=lambda: self.open_customers())  # type: ignore

        self.accButton = QPushButton("Accounts", clicked=lambda: self.open_accounts())  # type: ignore

        self.cardButton = QPushButton("Cards", clicked=lambda: self.open_cards())  # type: ignore

        self.txnButton = QPushButton("Transactions", clicked=lambda: self.open_transactions())  # type: ignore

        self.loanButton = QPushButton("Loans", clicked=lambda: self.open_loans())  # type: ignore

        self.loanPayButton = QPushButton("Loans Payment", clicked=lambda: self.open_loansPayment())  # type: ignore

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
        layout.addWidget(self.entitiesLabel)

        # Push buttons for entities
        layout.addWidget(self.cusButton)
        layout.addWidget(self.accButton)
        layout.addWidget(self.cardButton)
        layout.addWidget(self.txnButton)
        layout.addWidget(self.loanButton)
        layout.addWidget(self.loanPayButton)

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

        # Set the layout
        # self.setLayout(layout)
        ########################################

        ### Center window content ###
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        ####################################

    ##################### BUTTON FUNCTIONS #####################

    def open_customers(self):
        # print('Customers')
        self.customers = customers()
        self.hide()
        self.customers.show()

    def open_accounts(self):
        # print('Accounts')
        self.accounts = accounts()
        self.hide()
        self.accounts.show()

    def open_cards(self):
        # print('Cards')
        self.cards = cards()
        self.hide()
        self.cards.show()

    def open_transactions(self):
        # print('Transactions')
        self.transactions = transactions()
        self.hide()
        self.transactions.show()

    def open_loans(self):
        # print('Loans')
        self.loans = loans()
        self.hide()
        self.loans.show()

    def open_loansPayment(self):
        # print('Loans Payment')
        self.loansPayment = loansPayment()
        self.hide()
        self.loansPayment.show()

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
