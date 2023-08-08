from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication

# import the necessary modules from other windows
from win_02_1_CusServDashboard import cusServDashboard
from win_02_2_HRDashboard import hrDashboard

# other modules
import cx_Oracle
import qdarktheme
import sys


class welcome(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        windowTitle = "VVBank"
        self.setWindowTitle(windowTitle)

        # set WINDOW ICON (icons from icons8.com)
        self.setWindowIcon(QIcon("./assets/bank.png"))

        # Set window size
        width = 800
        height = 600
        self.resize(width, height)

        # center the window, center function defined below
        self.center()

        # Good practice to use a member of another class
        # initialize members of other classes to None
        self.cusServDashboard = None
        self.hrDashboard = None

        # create the user interface
        self.initUI()

    # user interface function
    def initUI(self):
        """
        Initializes the customers window.
        """
        ######################### CREATE WIDGETS #########################

        self.welcomeLabel = QLabel("Welcome to VVBank")
        self.welcomeLabel.setFont(QFont("Century", 28))

        # Consider adding a logo

        # Username
        self.usernameLabel = QLabel("Username")
        self.usernameField = QLineEdit()
        self.usernameField.setPlaceholderText("Username")

        # Password
        self.passwordLabel = QLabel("Password")
        self.passwordField = QLineEdit()
        self.passwordField.setPlaceholderText("Enter your password")
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        # Login as
        self.loginasLabel = QLabel("Login as")
        self.loginasLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Login buttons
        # EAST LEGON employees usernames
        self.cusServ_dep_usn = [
            "elom",
            "kwameowusu",
            "akosuaappiah",
            "kwesiannan",
            "amaboateng",
            "kofiasante",
            "adwoaaddo",
            "yawamoah",
            "abenaacheampong",
            "kwakuboakye",
            "akuadwomoh",
            "yawfrimpong",
            "adjoagyan",
            "kwabenakwame",
        ]

        # EAST LEGON employees usernames
        self.hr_dep_usn = [
            "elom",
            "kwadwohanson",
            "joshuaayivor",
            "fatimakone",
        ]
        # customer Service login Button
        self.cusServloginButton = QPushButton("Customer Service", clicked=lambda: self.login("cusServDashboard", self.cusServ_dep_usn))  # type: ignore
        # Human Resource login Button
        self.HRloginButton = QPushButton("Human Resources", clicked=lambda: self.login("hrDashboard", self.hr_dep_usn))  # type: ignore

        # About & Get Help widgets
        self.aboutButton = QPushButton("About", clicked=lambda: self.about())  # type: ignore
        self.getHelpButton = QPushButton("Get Help", clicked=lambda: self.help())  # type: ignore

        ####################### END OF WIDGETS CREATION #######################

        ############################ LAYOUT ############################

        layout = QVBoxLayout()

        ### ADD WIDGETS TO LAYOUT ###

        layout.addWidget(self.welcomeLabel)
        layout.addSpacing(20)
        layout.addWidget(self.usernameLabel)
        layout.addWidget(self.usernameField)
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.passwordField)
        layout.addWidget(self.loginasLabel)
        layout.addWidget(self.cusServloginButton)
        layout.addWidget(self.HRloginButton)

        # set layout
        nestedlayout = QVBoxLayout()
        nestedlayout.addWidget(self.aboutButton)
        nestedlayout.addWidget(self.getHelpButton)
        # align layout to the bottom right
        nestedlayout.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom
        )

        # add nested layout to main layout
        layout.addStretch(1)  # push the widget to the bottom
        layout.addLayout(nestedlayout)

        ### SET CONTENT MARGINS ###
        layout.setContentsMargins(200, 200, 200, 100)  # left, top, right, bottom

        ### Center window content ###
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        ####################################

        ############## Status Bar ##############
        # show message in the status bar
        self.statusBar().showMessage("Ready...")  # type: ignore
        ########################################

    ##################### BUTTON FUNCTIONS #####################

    # LOGIN BUTTON FUNCTION
    def login(self, dashboard: str, dep_usn: list):
        # Grab text in the fields
        self.username = self.usernameField.text()
        self.password = self.passwordField.text()
        self.dsn = "localhost:1521/VVBANKING"

        # set the appropriate dashboard and second department name
        if dashboard == "cusServDashboard":
            self.dashboard = cusServDashboard()
            self.otherdep = "Human Resources"
        elif dashboard == "hrDashboard":
            self.dashboard = hrDashboard()
            self.otherdep = "Customer Service"

        # initialise connection
        self.connection = None

        try:
            self.connection = cx_Oracle.connect(
                user=self.username, password=self.password, dsn=self.dsn
            )
        except cx_Oracle.Error as err:
            QMessageBox.critical(
                self,
                "Database Connection Error",
                str(err)
                + "\n"
                + "Failed to connect to database"
                + "\n"
                + "Please contact the database administrator",
            )
        else:
            if self.connection:
                if self.username in dep_usn:
                    self.hide()
                    self.dashboard.show()
                    QMessageBox.information(self, "Login", "Login successful")
                else:
                    QMessageBox.warning(
                        self,
                        "Login Error",
                        f"You are not authorized to access this section. Please login as a {self.otherdep} employee!",
                    )
        finally:
            if self.connection is not None:
                self.connection.close()

    # About button
    def about(self):
        QMessageBox.information(
            self, "About", "Version 1.0" + "\n" + "This is the About section"
        )

    # Help button
    def help(self):
        QMessageBox.information(self, "Help", "This is the Help section")

    ##################### END OF BUTTON FUNCTIONS #####################

    ##################### CENTER WINDOW FUNCTION #####################
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

    ############################# END OF CENTER WINDOW FUNCTION #############################


if __name__ == "__main__":
    try:
        # Include in try/except block if also targeting Mac/Linux
        from ctypes import windll  # only exists on Windows

        myappid = "mycompany.myproduct.subproduct.version"
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    finally:
        # create the QApplication object
        app = QApplication(sys.argv)

        # create the main window
        welcomewindow = welcome()

        # show the window
        welcomewindow.show()

        # DARK THEME (https://pypi.org/project/pyqtdarktheme/)
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())
