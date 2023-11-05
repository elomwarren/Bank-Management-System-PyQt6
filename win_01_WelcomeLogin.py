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
import os

# https://stackoverflow.com/a/31966932
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class welcome(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the window title
        windowTitle = "WEL Bank"
        self.setWindowTitle(windowTitle)

        # set WINDOW ICON (icons from icons8.com)
        self.setWindowIcon(QIcon(resource_path("./assets/bank.png")))

        # Set cream color for the background
        # self.setStyleSheet("background-color: #HEXcode")

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
        # self.welcomeLabel = QLabel("Welcome to WEL Bank")
        # self.welcomeLabel.setFont(QFont("Century", 28))
        self.logo = QPixmap(
            resource_path("./assets/WEL_Bank-logos_transparent_greentext_300x300.png")
        )
        self.logolabel = QLabel()
        self.logolabel.setPixmap(self.logo)
        self.logolabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
            "welbank",
            "cs",
            "kwameowusu",
        ]

        # EAST LEGON employees usernames
        self.hr_dep_usn = [
            "welbank",
            "hr",
            "kwadwohanson",
        ]
        # customer Service login Button
        self.cusServloginButton = QPushButton("Customer Service", clicked=lambda: self.login("cusServDashboard", self.cusServ_dep_usn))  # type: ignore
        # Human Resource login Button
        self.HRloginButton = QPushButton("Human Resources", clicked=lambda: self.login("hrDashboard", self.hr_dep_usn))  # type: ignore

        # About & Get Help widgets
        self.aboutButton = QPushButton("About", clicked=lambda: self.about())  # type: ignore
        self.getHelpButton = QPushButton("Get Help", clicked=lambda: self.help())  # type: ignore
        ######################################################### END OF WIDGETS CREATION #########################################################

        ############################ LAYOUT ############################
        layout = QVBoxLayout()

        # Add a spacer
        # layout.addStretch()

        ### ADD WIDGETS TO LAYOUT ###
        # layout.addWidget(self.welcomeLabel)
        layout.addWidget(self.logolabel)
        layout.addSpacing(10)
        layout.addWidget(self.usernameLabel)
        layout.addWidget(self.usernameField)
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.passwordField)
        layout.addWidget(self.loginasLabel)
        layout.addWidget(self.cusServloginButton)
        layout.addWidget(self.HRloginButton)
        layout.addSpacing(10)

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
        layout.setContentsMargins(200, 30, 200, 50)  # left, top, right, bottom

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
        self.dsn = "localhost:1521/WELBANK"

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
        QMessageBox.information(
            self,
            "Help",
            "This is the Help section" + "\n" + "Contact the IT Department",
        )

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

        # create the main window (an instance of of the welcome class)
        welcomewindow = welcome()

        # show the window
        welcomewindow.show()

        # DARK THEME (https://pypi.org/project/pyqtdarktheme/)
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())
