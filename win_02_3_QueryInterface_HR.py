from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QTextEdit,
    QTableWidget,
    QListWidget,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication, QIcon

import qdarktheme
import sys


class queryInterface(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        windowTitle = "Query Interface"
        self.setWindowTitle(windowTitle)

        # set WINDOW ICON
        self.setWindowIcon(QIcon("./assets/query.png"))

        # Set window size
        width = 800
        height = 600
        self.resize(width, height)

        # center the window, center function defined below
        self.center()

        # initialize the hrDashboard member to None in the welcome class
        self.hrDashboard = None

        # create the user interface
        self.initUI()

    # user interface function
    def initUI(self):
        ########################### ADD WIDGETS ###########################

        # Data Query Tool
        dataQueryToolLabel = QLabel("Data Query Tool")
        dataQueryToolLabel.setFont(QFont("Times", 24))
        dataQueryToolLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Enter Your Query
        enterYourQueryLabel = QLabel("Enter Your Query:")

        # Query Field - QTextEdit
        queryField = QTextEdit()
        queryField.setPlaceholderText("Enter your query here")
        # setFixedHeight(100)
        queryField.setFixedHeight(100)

        # Execute Query Button
        executeQueryButton = QPushButton("Execute Query", clicked=lambda: executeQuery())  # type: ignore

        # QUERY RESULTS: QTableWidget
        queryResultsLabel = QTableWidget()

        # Export to Excel Button
        exportToExcelButton = QPushButton("Export to Excel", clicked=lambda: exportToExcel())  # type: ignore

        # BACK BUTTON
        backButton = QPushButton("Back", clicked=lambda: back())  # type: ignore

        # Previous Queries
        previousQueriesLabel = QLabel("Previous Queries")
        # QLISTWIDGET
        list_queries = QListWidget()

        ####################### END OF ADD WIDGETS ########################

        ############################## LAYOUT ##############################

        hbox = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()

        ### ADD WIDGETS TO vbox1 ###

        # Data Query Tool
        vbox1.addWidget(dataQueryToolLabel)

        # set spacing between previous widget and next widget
        vbox1.addSpacing(20)

        # Enter Your Query
        vbox1.addWidget(enterYourQueryLabel)

        # Query Field - QTextEdit
        vbox1.addWidget(queryField)

        # ADD AUTOCOMPLETE FUNCTIONALITY TO QUERY FIELD
        # !!!!!! NEED TO ADD THIS !!!!!!

        # Execute Query Button
        vbox1.addWidget(executeQueryButton)

        # QUERY RESULTS: QTableWidget
        vbox1.addWidget(queryResultsLabel)

        # Export to Excel Button
        vbox1.addWidget(exportToExcelButton)

        # BACK BUTTON
        vbox1.addWidget(backButton)

        ### END ADD WIDGETS TO vbox1 ###

        # NEST vbox1 in hbox
        hbox.addLayout(vbox1, 2)

        ### ADD WIDGETS TO vbox2 ###

        # Label Previous Queries
        vbox2.addWidget(previousQueriesLabel)
        # QLISTWIDGET
        vbox2.addWidget(list_queries)

        ### END ADD WIDGETS TO vbox2 ###

        # NEST vbox2 in hbox
        hbox.addLayout(vbox2, 1)

        ### END ADD WIDGETS TO hbox ###

        ### Center window content ###
        container = QWidget()
        container.setLayout(hbox)
        self.setCentralWidget(container)

        ########################## END OF LAYOUT ##########################

        ##################### BUTTON FUNCTIONS #####################

        # Execute Query Button
        def executeQuery():
            print("Query executed")

        # Export to Excel Button
        def exportToExcel():
            print("Exported to Excel")

        # BACK BUTTON
        def back():
            # print('Back')
            from win_02_2_HRDashboard import hrDashboard

            self.hrDashboard = hrDashboard()
            self.hide()
            self.hrDashboard.show()

        ##################### END OF BUTTON FUNCTIONS #####################

    ############################## CENTER WINDOW FUNCTION ##############################
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

    ############################## END OF CENTER FUNCTION #############################


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
        querywindow = queryInterface()

        # show the window
        querywindow.show()

        # DARK THEME
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())
