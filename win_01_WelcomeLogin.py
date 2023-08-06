from PyQt6 import QtWidgets
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

        # Best practice to use a member of another class

        # initialize the cusServDashboard member to None in the welcome class
        self.cusServDashboard = None

        # initialize the hrDashboard member to None in the welcome class
        self.hrDashboard = None

        # create the user interface
        self.initUI()

    # user interface function
    def initUI(self):
        ######################### CREATE WIDGETS #########################

        self.welcomeLabel = QLabel("Welcome to VVBank")
        self.welcomeLabel.setFont(QFont("Century", 28))

        ######################### LOGO ##########################
        # logoPixmap = QPixmap('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/Volta Vision Bank 800².png')
        # logoPixmaplabel = QLabel()
        # logoPixmaplabel.setPixmap(logoPixmap)
        #########################################################

        # Username
        self.usernameLabel = QLabel("Username")
        self.usernameField = QLineEdit()
        self.usernameField.setPlaceholderText("Username")

        # Password
        self.passwordLabel = QLabel("Password")
        self.passwordField = QLineEdit()
        self.passwordField.setPlaceholderText("Enter your password")
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        ########################################################

        # Login as
        self.loginasLabel = QLabel("Login as")
        self.loginasLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # cusServloginButton
        self.cusServloginButton = QPushButton("Customer Service", clicked=lambda: self.cusServ())  # type: ignore

        # 2nd method
        # create the button
        # cusServloginButton = QPushButton('Customer Service')
        # Connect the clicked signal to the slot
        # cusServloginButton.clicked.connect(cusServ)

        # HRloginButton
        self.HRloginButton = QPushButton("Human Resources", clicked=lambda: self.hr())  # type: ignore

        # About & Get Help widgets
        self.aboutButton = QPushButton("About", clicked=lambda: self.about())  # type: ignore
        self.getHelpButton = QPushButton("Get Help", clicked=lambda: self.help())  # type: ignore

        ####################### END OF CREATE WIDGETS #######################

        ############################ LAYOUT ############################

        layout = QVBoxLayout()

        ############## STRETCHING DOWNWARD ##############
        # add a spacer
        # layout.addStretch()
        #################################################

        ### ADD WIDGETS TO LAYOUT ###

        layout.addWidget(self.welcomeLabel)
        # layout.addWidget(logoPixmaplabel)
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
        nestedlayout.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom
        )  # align to the bottom right

        # add nested layout to main layout
        layout.addStretch(1)  # push the widget to the bottom
        layout.addLayout(nestedlayout)

        ############## STRETCHING UPWARD ##############
        # add a spacer
        # layout.addStretch()
        ###############################################

        # cause error "QWidget::setLayout: Attempting to set QLayout "" on MainWindow "", which already has a layout"
        # self.setLayout(layout)

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

        # EAST LEGON employees
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

        # EAST LEGON employees
        self.hr_dep_usn = [
            "elom",
            "kwadwohanson",
            "joshuaayivor",
            "fatimakone",
        ]

    # cusServloginButton
    def cusServ(self):
        # Grab text in the fields
        self.username = self.usernameField.text()
        self.password = self.passwordField.text()
        self.dsn = "localhost:1521/VVBANKING"
        import cx_Oracle

        # initialise connection
        self.connection = None

        try:
            self.connection = cx_Oracle.connect(
                user=self.username, password=self.password, dsn=self.dsn
            )
            if self.connection:
                if self.username in self.cusServ_dep_usn:
                    self.cusServDashboard = cusServDashboard()
                    self.hide()
                    self.cusServDashboard.show()
                    # print('Login successful')
                    QMessageBox.information(self, "Login", "Login successful")
                    # successloginmsgBox.setWindowTitle('Login')
                    # successloginmsgBox.setWindowIcon(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/authentication.png'))
                    # successloginmsgBox.setText('Login successful')
                    # successloginmsgBox.exec()
                elif self.username in self.hr_dep_usn:
                    # print('''
                    #       You are not authorized to access this section.
                    #       Please login as a Human Resources employee
                    #       ''')
                    QMessageBox.warning(
                        self,
                        "Login Error",
                        "You are not authorized to access this section. Please login as a Human Resources employee!",
                    )
                    # wrongloginmsgBox.setWindowTitle('Login Error')
                    # wrongloginmsgBox.setWindowIcon(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/warning.png'))
                    # wrongloginmsgBox.setText('''
                    #                         You are not authorized to access this section.
                    #                         Please login as a Human Resources employee
                    #                         ''')
                    # failloginmsgBox.exec()
        except cx_Oracle.Error as err:
            # print('Fail to connect to database', err)
            QMessageBox.critical(
                self,
                "Database Connection Error",
                str(err)
                + "\n"
                + "Failed to connect to database"
                + "\n"
                + "Please contact the database administrator",
            )
        # else:
        #     cursor = connection.cursor()
        #     # Alter session date format
        #     cursor.execute(
        #         """
        #                 ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MON-YYYY'
        #                     """
        #     )

        finally:
            if self.connection is not None:
                self.connection.close()

    # HRloginButton
    def hr(self):
        # Grab text in the fields
        import cx_Oracle

        # initialise connection (previously done in cusServ function)

        try:
            self.connection = cx_Oracle.connect(
                user=self.username, password=self.password, dsn=self.dsn
            )
            if self.connection:
                if self.username in self.hr_dep_usn:
                    self.hrDashboard = hrDashboard()
                    self.hide()
                    self.hrDashboard.show()
                    QMessageBox.information(self, "Login", "Login successful")

                elif self.username in self.hr_dep_usn:
                    QMessageBox.warning(
                        self,
                        "Login Error",
                        "You are not authorized to access this section. Please login as a Customer Service employee!",
                    )
                    # print('Welcome to the HR Dashboard')
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
        # else:
        #     cursor = connection.cursor()
        #     # Alter session date format
        #     cursor.execute(
        #         """
        #                 ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MON-YYYY'
        #                     """
        #     )
        finally:
            if self.connection is not None:
                self.connection.close()

    # About button
    def about(self):
        aboutmsgBox = QMessageBox()
        aboutmsgBox.setWindowTitle("About")
        aboutmsgBox.setWindowIcon(QIcon("./assets/about.png"))
        aboutmsgBox.setText("This is the About section")
        aboutmsgBox.exec()
        # print('About')

    # Help button
    def help(self):
        helpmsgBox = QMessageBox()
        helpmsgBox.setWindowTitle("About")
        helpmsgBox.setText("This the Help section")
        helpmsgBox.setWindowIcon(QIcon("./assets/help.png"))
        helpmsgBox.exec()
        # print('Help')

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
        welcomewindow = welcome()

        # show the window
        welcomewindow.show()

        # DARK THEME
        # https://pypi.org/project/pyqtdarktheme/
        # pip install pyqtdarktheme
        # Apply the complete dark theme to Qt App.
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())
