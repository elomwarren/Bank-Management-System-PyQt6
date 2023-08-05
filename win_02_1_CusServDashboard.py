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
        self.setWindowIcon(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/dashboard.png"
            )
        )

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
        dashboardLabel = QLabel("DASHBOARD")
        dashboardLabel.setFont(QFont("Century", 28))
        dashboardLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Entities Label
        entitiesLabel = QLabel("Entities")
        entitiesLabel.setFont(QFont("Century", 16))
        entitiesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ### Push buttons for entities ###

        cusButton = QPushButton("Customers", clicked=lambda: open_customers())  # type: ignore

        accButton = QPushButton("Accounts", clicked=lambda: open_accounts())  # type: ignore

        cardButton = QPushButton("Cards", clicked=lambda: open_cards())  # type: ignore

        txnButton = QPushButton("Transactions", clicked=lambda: open_transactions())  # type: ignore

        loanButton = QPushButton("Loans", clicked=lambda: open_loans())  # type: ignore

        loanPayButton = QPushButton("Loans Payment", clicked=lambda: open_loansPayment())  # type: ignore

        # ANOTHER PRACTICAL WAY TO CREATE BUTTONS using for loop
        # titles = ['Customers', 'Accounts', 'Cards', 'Transactions', 'Loans', 'Loans Payment']
        # buttons = [QPushButton(title) for title in titles]

        # ### CONNECT BUTTONS TO FUNCTIONS ###
        # buttons[0].clicked.connect(Customers)
        # buttons[1].clicked.connect(Accounts)
        # buttons[2].clicked.connect(Cards)
        # buttons[3].clicked.connect(Transactions)
        # buttons[4].clicked.connect(Loans)
        # buttons[5].clicked.connect(LoansPayment)

        # TOOL LABEL
        toolLabel = QLabel("Tools")
        toolLabel.setFont(QFont("Century", 16))
        toolLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Push button for Data Query Wizard
        dataQueryWizardButton = QPushButton("Data Query Wizard", clicked=lambda: dataQueryWizard())  # type: ignore
        dataQueryWizardButton.setIcon(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/query.png"
            )
        )

        # Logout Push button
        logoutButton = QPushButton("Logout", clicked=lambda: logout())  # type: ignore

        # quit button
        quitButton = QPushButton("Quit", clicked=lambda: quit())  # type: ignore

        ####################### END OF ADD WIDGETS #######################

        ############################ LAYOUT ############################

        layout = QVBoxLayout()

        ### ADD WIDGETS TO LAYOUT ###

        # Dashboard label
        layout.addWidget(dashboardLabel)

        # set space after Dashboard label
        layout.addSpacing(15)

        # Entities Label
        layout.addWidget(entitiesLabel)

        # Push buttons for entities
        layout.addWidget(cusButton)
        layout.addWidget(accButton)
        layout.addWidget(cardButton)
        layout.addWidget(txnButton)
        layout.addWidget(loanButton)
        layout.addWidget(loanPayButton)

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

        def open_customers():
            # print('Customers')
            self.customers = customers()
            self.hide()
            self.customers.show()

        def open_accounts():
            # print('Accounts')
            self.accounts = accounts()
            self.hide()
            self.accounts.show()

        def open_cards():
            # print('Cards')
            self.cards = cards()
            self.hide()
            self.cards.show()

        def open_transactions():
            # print('Transactions')
            self.transactions = transactions()
            self.hide()
            self.transactions.show()

        def open_loans():
            # print('Loans')
            self.loans = loans()
            self.hide()
            self.loans.show()

        def open_loansPayment():
            # print('Loans Payment')
            self.loansPayment = loansPayment()
            self.hide()
            self.loansPayment.show()

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
        # https://pypi.org/project/pyqtdarktheme/
        # pip install pyqtdarktheme
        # Apply the complete dark theme to Qt App.
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())
