from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QToolBar, QLineEdit, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QFormLayout, QDockWidget, 
                             QTableWidget, QTableWidgetItem, QMessageBox
                             )
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QGuiApplication, QIcon, QAction

import cx_Oracle
import qdarktheme
import sys

class loansPayment(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        windowTitle = 'Loans Payment'
        self.setWindowTitle(windowTitle)

        # set WINDOW ICON (icons from icons8.com)
        self.setWindowIcon(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/loan-payment.png'))

        # Set window size 
        width = 800
        height = 600
        self.resize(width, height)

        # center the window, center function defined below
        self.center()

        # initialize member of other windows
        self.cusServDashboard = None

        # create the UI
        self.initUI()


    def initUI(self):

        ##### MENU BAR #####

        # Create menu bar
        menuBar = self.menuBar() # Get the QMenuBar from the QMainWindow
        
        # Create QMenus
        fileMenu = menuBar.addMenu('&File') # Add the QMenu to the QMenuBar # type: ignore
        editMenu = menuBar.addMenu('&Edit') # type: ignore
        viewMenu = menuBar.addMenu('&View') # type: ignore
        helpMenu = menuBar.addMenu('&Help') # type: ignore

        ### File Menu ###

        # 'Add' menu item
        addAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/add.png'), '&Add', self)
        addAction.setStatusTip('Add a new customer')
        addAction.setShortcut('Ctrl+N')
        addAction.triggered.connect(self.newRecord)
        fileMenu.addAction(addAction) # type: ignore

        # 'Delete' menu item
        delAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/remove.png'), '&Delete', self)
        delAction.setStatusTip('Delete a customer')
        delAction.setShortcut('Del')
        delAction.triggered.connect(self.delRecord)
        fileMenu.addAction(delAction) # type: ignore

        # 'Save' menu item
        saveAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/save.png'), '&Save Changes', self)
        saveAction.setStatusTip('Save (Commit) changes to the database')
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveChanges)

        # add Sepaaratora after save
        fileMenu.addSeparator() # type: ignore

        # 'Exit' menu item
        exitAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/exit.png'), '&Exit', self)
        exitAction.setStatusTip('Exit')
        exitAction.setShortcut('Alt+F4')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction) # type: ignore

        ### Edit Menu ###

        # 'Undo' menu item
        undoAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/undo.png'), '&Undo', self)
        undoAction.setStatusTip('Undo')
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.undoChanges)
        editMenu.addAction(undoAction) # type: ignore

        # 'Redo' menu item
        redoAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/redo.png'), '&Redo', self)
        redoAction.setStatusTip('Redo')
        redoAction.setShortcut('Ctrl+Y')
        redoAction.triggered.connect(self.redoChanges)
        editMenu.addAction(redoAction) # type: ignore

        # add Separator
        editMenu.addSeparator() # type: ignore

        # 'Cut' menu item
        cutAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/cut.png'), '&Cut', self)
        cutAction.setStatusTip('Cut')
        cutAction.setShortcut('Ctrl+X')
        cutAction.triggered.connect(self.cut)
        editMenu.addAction(cutAction) # type: ignore

        # 'Copy' menu item
        copyAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/copy.png'), '&Copy', self)
        copyAction.setStatusTip('Copy')
        copyAction.setShortcut('Ctrl+C')
        copyAction.triggered.connect(self.copy)
        editMenu.addAction(copyAction) # type: ignore

        # 'Paste' menu item
        pasteAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/paste.png'), '&Paste', self)
        pasteAction.setStatusTip('Paste')
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.triggered.connect(self.paste)
        editMenu.addAction(pasteAction) # type: ignore

        ### View menu ###

        # 'Search' menu item
        searchAction  = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/search.png'), '&Search', self)
        searchAction.setStatusTip('Search')
        searchAction.setShortcut('Ctrl+F')
        searchAction.triggered.connect(self.searchdock)
        viewMenu.addAction(searchAction) # type: ignore

        ### Help menu ###

        # 'About' menu item
        aboutAction = QAction(QIcon('D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/info.png'), '&About', self)
        aboutAction.setStatusTip('Help')
        aboutAction.setShortcut('F1')
        aboutAction.triggered.connect(self.about)
        helpMenu.addAction(aboutAction) # type: ignore


        ##### END OF MENU BAR #####

        ##### TOOLBAR #####

        # Create toolbar

        toolBar = QToolBar('Main ToolBar')
        self.addToolBar(toolBar)
        toolBar.setIconSize(QSize(25, 25))

        # toolbar items
        # From File menu
        toolBar.addAction(addAction)
        toolBar.addAction(delAction)
        toolBar.addAction(saveAction)
        toolBar.addSeparator()

        # From Edit menu
        toolBar.addAction(undoAction)
        toolBar.addAction(redoAction)
        toolBar.addSeparator()

        # From View menu
        toolBar.addAction(searchAction)
        toolBar.addSeparator()

        # exit item
        toolBar.addAction(exitAction)

        ##### ENF OF TOOLBAR ######

        # Create status bar
        statusBar = self.statusBar()
        # display the a message in 5 seconds
        statusBar.showMessage('Ready', 5000) # type: ignore

        ########################### ADD WIDGETS ###########################

        ### VBOX WIDGETS ###
        # Entity label
        tableLabel = QLabel('LOANS PAYMENT')

        # Entity Table
        table = QTableWidget()

        # BACK BUTTON
        backButton = QPushButton('Back', clicked=lambda: back())  # type: ignore

        ### END OF VBOX WIDGETS ###

        ### CREATION NEW CUSTOMER FORM WIDGETS ###

        # Loan Payment ID field
        lnpayIDField = QLineEdit()

        # Loan Amount field
        lnpayAmountIDField = QLineEdit()

        # Loan Amount field
        lnpayRmnAmountIDField = QLineEdit()

        # Loan Date field
        lnpayDateField = QLineEdit()

        # Customer ID Field
        loanIDField = QLineEdit()


        # ADD BUTTON
        addButton = QPushButton('Add', clicked=lambda: add())  # type: ignore

        ### END OF CREATION NEW CUSTOMER FORM WIDGETS ###

        ### SEARCH FORM WIDGETS ###

        # Search Field
        SearchField = QLineEdit()
        SearchField.setPlaceholderText('Enter a search term')

        # SEARCH BUTTON
        SearchButton = QPushButton('Search', clicked= lambda: search())  # type: ignore

        # ADD FILTER BUTTON
        # !!! CONSIDER ADDING FILTER BUTTON !!!


        ### END OF SEARCH FORM WIDGETS ###



        ####################### END OF ADD WIDGETS ########################


        ############################ LAYOUT ############################
        
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        NewForm = QFormLayout()
        SearchForm = QFormLayout()

        ### ADD WIDGETS TO vbox LAYOUT ###

        # Entity label
        vbox.addWidget(tableLabel, alignment=Qt.AlignmentFlag.AlignLeft)

        # Entity Table
        vbox.addWidget(table)

        # PUT VALUES IN THE TABLE
        query = """
                SELECT * FROM LOANS_PAYMENT
                """
        try:
            connection = cx_Oracle.connect("elom/elom@localhost:1521/VVBANKING")
            cursor = connection.cursor()

            # Execute select all query
            cursor.execute(query)
            result = cursor.fetchall()

            # Display the results in the table
            table.setColumnCount(len(cursor.description))
            table.setRowCount(len(result))
            table.setHorizontalHeaderLabels([description[0] for description in cursor.description])

            for row_idx, row in enumerate(result):
                for col_idx, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    table.setItem(row_idx, col_idx, item)

            cursor.close()
            connection.close()

        except cx_Oracle.Error as err:
            failgetdatamsg =  QMessageBox.critical(self, 'Coundn\'t Fetch Data', '\n' + str(err) + '\n' + 'Please contact the database administrator')

        # BACK BUTTON
        vbox.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        ### END OF ADD WIDGETS TO vbox LAYOUT ###

        # Nest vbox in hbox
        hbox.addLayout(vbox)

        ### ADD WIDGETS TO NewForm LAYOUT ###

        NewForm.addRow('Loan Payment ID', lnpayIDField)
        NewForm.addRow('Amount', lnpayAmountIDField)
        NewForm.addRow('Balance', lnpayRmnAmountIDField)
        NewForm.addRow('Date', lnpayDateField)
        NewForm.addRow('Loan ID', loanIDField)
        NewForm.addRow(addButton)

        ### END OF ADD WIDGETS TO NewForm LAYOUT ###

        ### ADD WIDGETS TO SearchForm LAYOUT ###
        SearchForm.addRow(SearchField)
        SearchForm.addRow(SearchButton)

        ### END OF ADD WIDGETS TO SearchForm LAYOUT ###

        ### SEARCH DOCK ###

        # ADD DOCK WIDGET FOR SEARCH
        SearchDock = QDockWidget('Search')
        # SearchDock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, SearchDock)

        # END DOCK WIDGET FOR SEARCH

        # ADD WIDGETS TO SEARCH DOCK
        SearchDockWidget = QWidget()
        SearchDockWidget.setLayout(SearchForm)
        SearchDock.setWidget(SearchDockWidget)

        ### END OF SEARCH DOCK ###

        ###  NEW CUSTOMER DOCK ###

        # ADD DOCK WIDGET FOR NEW RECORD

        NewDock = QDockWidget('New Record')
        # NewDock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, NewDock)

        # END DOCK WIDGET FOR NEW CUSTOMER

        # ADD WIDGETS TO NEW CUSTOMER DOCK
        NewDockWidget = QWidget()
        NewDockWidget.setLayout(NewForm)
        NewDock.setWidget(NewDockWidget)


        ### END OF NEW CUSTOMER DOCK ###

        ### Center window content ###
        container = QWidget()
        container.setLayout(hbox)
        self.setCentralWidget(container)

        ########################## END OF LAYOUT ##########################


        ##################### BUTTON FUNCTIONS #####################

        # BACK BUTTON
        def back():
            # print('Back')
            from win_02_1_CusServDashboard import cusServDashboard
            self.cusServDashboard = cusServDashboard()
            self.hide()
            self.cusServDashboard.show()

        # ADD BUTTON
        def add():
            print('New record added')

        # SEARCH BUTTON
        def search():
            print('Search')


        ##################### END OF BUTTON FUNCTIONS #####################

    ##################### MENU BAR FUNCTIONS ??? #####################

    # Open New Record Dock 
    def newRecord(self):
        pass

    # Delete selected record from database
    def delRecord(self):
        pass

    # Save button: Commit changes to the database
    def saveChanges(self):
        pass

    # Rollback transactions
    def undoChanges(self):
        pass

    # Redo transactions
    def redoChanges(self):
        pass

    # Cut selected text
    def cut(self):
        pass

    # Copy selected text
    def copy(self):
        pass

    # Paste selected text
    def paste(self):
        pass

    # Open Search Dock
    def searchdock(self):
        pass

    # Open About window
    def about(self):
        pass



    ##################### END OF MENU BAR FUNCTIONS #####################

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
        lnpaywindow = loansPayment()

        # show window
        lnpaywindow.show()

        # DARK THEME
        # https://pypi.org/project/pyqtdarktheme/
        # pip install pyqtdarktheme
        # Apply the complete dark theme to Qt App.
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())