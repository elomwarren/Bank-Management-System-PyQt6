from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QToolBar,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QDockWidget,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QComboBox,
    QDateEdit,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize, QRegularExpression, QDate
from PyQt6.QtGui import QGuiApplication, QIcon, QAction, QRegularExpressionValidator

# import necessary modules from other windows

# other modules
import datetime
import re  # for regular expressions
import cx_Oracle
import qdarktheme
import sys


class accounts(QMainWindow):
    def __init__(self, *args, **kwargs):
        """
        Initializes the customers window.
        """
        super().__init__(*args, **kwargs)

        # set the window title
        windowTitle = "Accounts"
        self.setWindowTitle(windowTitle)

        # set WINDOW ICON (icons from icons8.com)
        self.setWindowIcon(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/account.png"
            )
        )

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
        """
        Initializes the user interface for the Customers window.
        """

        ##### MENU BAR #####

        # Create menu bar
        menuBar = self.menuBar()  # Get the QMenuBar from the QMainWindow

        # Create QMenus
        # Add the QMenu to the QMenuBar
        self.fileMenu = menuBar.addMenu("&File")  # type: ignore
        self.editMenu = menuBar.addMenu("&Edit")  # type: ignore
        self.viewMenu = menuBar.addMenu("&View")  # type: ignore
        self.helpMenu = menuBar.addMenu("&Help")  # type: ignore

        ### File Menu ###

        # 'Add' menu item
        addAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/add.png"
            ),
            "&New Record",
            self,
        )
        addAction.setStatusTip("Add a new record")
        addAction.setShortcut("Ctrl+N")
        addAction.triggered.connect(self.newRecord)
        self.fileMenu.addAction(addAction)  # type: ignore

        # 'Delete' menu item
        delAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/remove.png"
            ),
            "&Delete",
            self,
        )
        delAction.setStatusTip("Delete a record")
        delAction.setShortcut("Del")
        delAction.triggered.connect(self.delRecord)
        self.fileMenu.addAction(delAction)  # type: ignore

        # 'Save' menu item
        saveAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/save.png"
            ),
            "&Save Changes",
            self,
        )
        saveAction.setStatusTip("Save (Commit) changes to the database")
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.saveChanges)

        # add Sepaaratora after save
        self.fileMenu.addSeparator()  # type: ignore

        # 'Exit' menu item
        exitAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/exit.png"
            ),
            "&Exit",
            self,
        )
        exitAction.setStatusTip("Exit")
        exitAction.setShortcut("Alt+F4")
        exitAction.triggered.connect(self.close)  # no need to define a function
        self.fileMenu.addAction(exitAction)  # type: ignore

        ### Edit Menu ###

        # 'Undo' menu item
        undoAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/rollback.png"
            ),
            "&Undo",
            self,
        )
        undoAction.setStatusTip("Undo (Use with caution)")
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.undoChanges)
        self.editMenu.addAction(undoAction)  # type: ignore

        # add Separator
        self.editMenu.addSeparator()  # type: ignore

        # 'Cut' menu item
        cutAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/cut.png"
            ),
            "&Cut",
            self,
        )
        cutAction.setStatusTip("Cut")
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.cut)
        self.editMenu.addAction(cutAction)  # type: ignore

        # 'Copy' menu item
        copyAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/copy.png"
            ),
            "&Copy",
            self,
        )
        copyAction.setStatusTip("Copy")
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.copy)
        self.editMenu.addAction(copyAction)  # type: ignore

        # 'Paste' menu item
        pasteAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/paste.png"
            ),
            "&Paste",
            self,
        )
        pasteAction.setStatusTip("Paste")
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.paste)
        self.editMenu.addAction(pasteAction)  # type: ignore

        ### View menu ###

        # 'Search' menu item
        searchAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/search.png"
            ),
            "&Search",
            self,
        )
        searchAction.setStatusTip("Search")
        searchAction.setShortcut("Ctrl+F")
        searchAction.triggered.connect(self.searchdock)
        self.viewMenu.addAction(searchAction)  # type: ignore

        ### Help menu ###

        # 'About' menu item
        aboutAction = QAction(
            QIcon(
                "D:/01_IPMC/01_SEMESTER1/08_PROJECT_WORK/02_PROJECT/01_PROJECT_PAPER/GUI/VVBank_GUIProject_PyQt6/assets/info.png"
            ),
            "&About",
            self,
        )
        aboutAction.setStatusTip("Help")
        aboutAction.setShortcut("F1")
        aboutAction.triggered.connect(self.about)
        self.helpMenu.addAction(aboutAction)  # type: ignore

        ##### END OF MENU BAR #####

        ##### TOOLBAR #####

        # Create toolbar

        self.toolBar = QToolBar("Main ToolBar")
        self.addToolBar(self.toolBar)
        self.toolBar.setIconSize(QSize(25, 25))

        # toolbar items
        # From File menu
        self.toolBar.addAction(addAction)
        self.toolBar.addAction(delAction)
        self.toolBar.addAction(saveAction)
        self.toolBar.addSeparator()

        # From Edit menu
        self.toolBar.addAction(undoAction)
        # toolBar.addAction(redoAction)
        self.toolBar.addSeparator()

        # From View menu
        self.toolBar.addAction(searchAction)
        self.toolBar.addSeparator()

        # exit item
        self.toolBar.addAction(exitAction)
        self.addAction(exitAction)

        ##### ENF OF TOOLBAR ######

        # Create status bar
        statusBar = self.statusBar()
        # display the a message in 5 seconds
        statusBar.showMessage("Ready", 5000)  # type: ignore

        ########################### WIDGETS CREATION ###########################

        ### VBOX WIDGETS ###
        # Entity label
        self.tableLabel = QLabel("ACCOUNTS")

        # Entity Table
        self.table = QTableWidget(self)

        # BACK BUTTON
        self.backButton = QPushButton("Back", clicked=lambda: self.back())  # type: ignore

        ### END OF VBOX WIDGETS ###

        ### CREATION NEW CUSTOMER FORM WIDGETS ###

        # Account ID field
        self.accountIDField = QLineEdit(self)
        self.accountIDField.setPlaceholderText("Account ID")

        # Account Number field
        self.accountNumField = QLineEdit(self)
        self.accountNumField.setPlaceholderText("XXXXXXXXXXXXX")
        self.accountNumPattern = "[0-9]{13}"
        self.regExp1 = QRegularExpression(self.accountNumPattern)
        self.val1 = QRegularExpressionValidator(self.regExp1)
        self.accountNumField.setValidator(self.val1)

        # Account Balance field
        self.accountBalField = QLineEdit(self)
        self.accountBalField.setPlaceholderText("0.00")
        self.accountBalPattern = "[0-9]{1,10}.[0-9]{2}"
        self.regExp2 = QRegularExpression(self.accountBalPattern)
        self.val2 = QRegularExpressionValidator(self.regExp2)
        self.accountBalField.setValidator(self.val2)

        # Account Type field
        self.accountTypeField = QComboBox(self)
        self.accountTypeField.addItems(["", "Savings", "Current", "Fixed Deposit"])

        # Account Creation Date field
        self.dateCreatField = QDateEdit(self)
        self.dateCreatField.setDisplayFormat("yyyy-MM-dd")

        # Account closure Date field
        self.dateCloseField = QLineEdit(self)
        self.dateCloseField.setText("None")
        self.dateCloseField.setReadOnly(True)

        # Customer ID Field
        self.customerIDField = QLineEdit(self)
        self.customerIDField.setPlaceholderText("1XXXXXXX or 5XXXXXXX")
        self.customerIDPattern = "[1|5][0-9]{7}"
        self.regExp3 = QRegularExpression(self.customerIDPattern)
        self.val3 = QRegularExpressionValidator(self.regExp3)
        self.customerIDField.setValidator(self.val3)

        # ADD BUTTON
        self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore

        # CANCEL BUTTON
        self.cancelButton = QPushButton("Cancel", clicked=lambda: self.cancel())  # type: ignore

        ### END OF CREATION NEW CUSTOMER FORM WIDGETS ###

        ### SEARCH FORM WIDGETS ###

        # Search Field
        self.searchField = QLineEdit(self)
        self.searchField.setPlaceholderText("Enter a search term")

        # Filter Field
        self.filterField = QComboBox(self)
        self.filters = [
            "ACC_ID",
            "ACC_NUMBER",
            "ACC_BAL",
            "ACC_TYPE",
            "ACC_START",
            "ACC_END",
            "CUS_ID",
        ]
        # add filters to the drop down menu
        self.filterField.addItem("Required")
        self.filterField.addItems(self.filters)

        # Sort By Field
        self.orderbyField = QComboBox(self)
        self.orderbyField.addItem("Optional")
        self.orderbyField.addItems(self.filters)

        # Sort Order Field
        self.orderField = QComboBox(self)
        self.orderField.addItem("Asc")
        self.orderField.addItem("Desc")

        # SEARCH BUTTON
        self.intColumns = ["ACC_ID", "ACC_NUMBER", "ACC_BAL", "CUS_ID"]
        self.searchButton = QPushButton("Search", clicked=lambda: self.search(self.intColumns))  # type: ignore

        # CLEAR BUTTON
        self.clearButton = QPushButton("Clear", clicked=lambda: self.clearFilters())  # type: ignore

        ### END OF SEARCH FORM WIDGETS ###

        ####################### END OF WIDGETS CREATION ########################

        ############################ LAYOUT ############################

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.NewForm = QFormLayout()
        self.SearchForm = QFormLayout()

        ### ADD WIDGETS TO vbox LAYOUT ###

        # Entity label
        self.vbox.addWidget(self.tableLabel, alignment=Qt.AlignmentFlag.AlignLeft)

        # Entity Table
        self.vbox.addWidget(self.table)

        # PUT VALUES IN THE TABLE
        # Table display query
        self.selectQuery = "SELECT * FROM ACCOUNTS"

        # Call the function to display values in the table
        self.displayTable(self.selectQuery)

        # BACK BUTTON
        self.vbox.addWidget(self.backButton, alignment=Qt.AlignmentFlag.AlignRight)

        ### END OF ADD WIDGETS TO vbox LAYOUT ###

        # Nest vbox in hbox
        self.hbox.addLayout(self.vbox)

        ### ADD WIDGETS TO NewForm LAYOUT ###

        self.NewForm.addRow("Account ID", self.accountIDField)
        self.NewForm.addRow("Account Number", self.accountNumField)
        self.NewForm.addRow("Balance", self.accountBalField)
        self.NewForm.addRow("Account Type", self.accountTypeField)
        self.NewForm.addRow("Creation Date", self.dateCreatField)
        self.NewForm.addRow("Close Date", self.dateCloseField)
        self.NewForm.addRow("Customer ID", self.customerIDField)
        self.NewForm.addRow(self.addButton)
        self.NewForm.addRow(self.cancelButton)
        ### END OF ADD WIDGETS TO NewForm LAYOUT ###

        ### ADD WIDGETS TO SearchForm LAYOUT ###
        self.SearchForm.addRow(self.searchField)
        self.SearchForm.addRow("Filter by", self.filterField)
        self.SearchForm.addRow("Sort by", self.orderbyField)
        self.SearchForm.addRow("Order", self.orderField)
        self.SearchForm.addRow(self.searchButton)
        self.SearchForm.addRow(self.clearButton)

        ### END OF ADD WIDGETS TO SearchForm LAYOUT ###

        ### SEARCH DOCK ###

        # ADD DOCK WIDGET FOR SEARCH
        self.SearchDock = QDockWidget("Search", self)
        # add "self." to make it an instance of the class and accessible from other methods
        # SearchDock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.SearchDock)

        # END DOCK WIDGET FOR SEARCH

        # ADD WIDGETS TO SEARCH DOCK
        self.SearchDockWidget = QWidget(self)
        self.SearchDockWidget.setLayout(self.SearchForm)
        self.SearchDock.setWidget(self.SearchDockWidget)

        ### END OF SEARCH DOCK ###

        ###  NEW CUSTOMER DOCK ###

        # ADD DOCK WIDGET FOR NEW RECORD

        self.NewRecordDock = QDockWidget("New Record")
        # NewDock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.NewRecordDock)

        # END DOCK WIDGET FOR NEW CUSTOMER

        # ADD WIDGETS TO NEW CUSTOMER DOCK
        self.NewRecordDockWidget = QWidget(self)
        self.NewRecordDockWidget.setLayout(self.NewForm)
        self.NewRecordDock.setWidget(self.NewRecordDockWidget)

        ### END OF NEW CUSTOMER DOCK ###

        ### Center window content ###
        self.container = QWidget()
        self.container.setLayout(self.hbox)
        self.setCentralWidget(self.container)

        ########################## END OF LAYOUT ##########################

    ##################### BUTTON FUNCTIONS #####################

    # BACK BUTTON
    def back(self):
        """
        Function to go back to the Customer Service Dashboard window when the Back button is clicked.

        Args:
            None

        Returns:
            None
        """
        from win_02_1_CusServDashboard import cusServDashboard

        self.cusServDashboard = cusServDashboard()
        self.hide()
        self.cusServDashboard.show()

    ### ADD RECORD FORM FUNCTIONS ###

    # CANCEL BUTTON
    def cancel(self):
        """
        Function to clear all fields in the Add Record form when the Cancel button is clicked.

        Args:
            None

        Returns:
            None
        """
        # Ask user for confirmation
        msg = QMessageBox.question(
            self,
            "Confirmation",
            "Do you really want to clear all fields?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if msg == QMessageBox.StandardButton.Yes:
            # clear fields
            self.accountIDField.clear()
            self.accountNumField.clear()
            self.accountBalField.clear()
            self.accountTypeField.setCurrentIndex(0)
            self.dateCreatField.setDate(QDate.currentDate())
            self.dateCloseField.clear()
            self.customerIDField.clear()
        else:
            pass

    # ADD BUTTON
    def add(self):
        """
        This method is called when the user clicks the "Add" button in the GUI. It retrieves the data entered by the user
        in the various fields, validates the data, and inserts a new record into the "ACCOUNTS" table in the database.
        """

        self.insertQuery = """
                insert into customers values (:1, :2, :3, :4, :5, :6, :7)
                """

        ### GRAB TEXT IN THE FIELDS AND ADD LOGIC ###
        self.accountID = self.accountIDField.text()
        self.accountNum = self.accountNumField.text()
        self.accountBal = self.accountBalField.text()
        self.accountType = self.accountTypeField.currentText()
        self.dateCreat = self.dateCreatField.text()
        self.dateClose = self.dateCloseField.text()
        self.customerID = self.customerIDField.text()

        # create a list of the data entered by the user
        self.columnsData = [
            self.accountID,
            self.accountNum,
            self.accountBal,
            self.accountType,
            self.dateCreat,
            self.dateClose,
            self.customerID,
        ]

        ### FIELDS VALIDATI0N LOGIC ###

        # Account ID validation
        if self.accountID == "":
            QMessageBox.warning(self, "Warning", "Please enter an Account ID.")
            return self.accountID
        # convert accountID to integer
        try:
            self.accountID = int(self.accountID)
        except ValueError:
            QMessageBox.warning(
                self, "Warning", "Please enter a valid Account ID (integer)."
            )
            return self.accountID

        # Account Number validation
        if self.accountNum == "" or len(self.accountNum) != 13:
            QMessageBox.warning(
                self, "Warning", "Please enter a valid Account Number (13 digits)."
            )
            return self.accountNum
        # convert accuntNum to integer
        try:
            self.accountNum = int(self.accountNum)
        except ValueError:
            QMessageBox.warning(
                self, "Warning", "Please enter a valid Account Number (integer)."
            )
            return self.accountNum

        # Account Balance validation
        if self.accountBal == "":
            QMessageBox.warning(self, "Warning", "Please enter an Account Balance.")
            return self.accountBal
        # convert accuntBal to integer
        try:
            self.accountBal = float(self.accountBal)
        except ValueError:
            QMessageBox.warning(
                self, "Warning", "Please enter a valid Account Balance (integer)."
            )
            return self.accountBal

        # Account Type validation
        if self.accountType == "":
            QMessageBox.warning(self, "Warning", "Please select an Account Type.")
            return self.accountType

        # Date Created validation
        self.creatDate = QDate.fromString(self.dateCreat, "yyyy-MM-dd")
        self.currentDate = QDate.currentDate()
        if (self.creatDate.year(), self.currentDate.month(), self.currentDate.day()) < (
            self.currentDate.year(),
            self.currentDate.month(),
            self.currentDate.day(),
        ):
            QMessageBox.warning(self, "Warning", "Please select a valid creation Date.")
            return self.dateCreat

        # Date Closed validation
        # if self.dateClose != "None":
        #     self.closeDate = QDate.fromString(self.dateClose, "yyyy-MM-dd")
        #     if (self.closeDate.year(), self.currentDate.month(), self.currentDate.day()) < (
        #         self.currentDate.year(),
        #         self.currentDate.month(),
        #         self.currentDate.day(),
        #     ):
        #         QMessageBox.warning(self, "Warning", "Please select a valid closing Date.")
        #         return self.dateClose
        # else:
        #     self.dateClose = "None"

        # Customer ID validation
        if self.customerID == "" or len(str(self.customerID)) != 8:
            QMessageBox.warning(
                self,
                "Invalid Customer ID",
                "Please enter a valid customer ID (8 digits)",
            )
            return self.customerID
        # convert customerID to integer
        try:
            self.customerID = int(self.customerID)
        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid Customer ID",
                "Please enter a valid customer ID (8 digits)",
            )
            return self.customerID

        self.dataInsert(self.insertQuery, self.columnsData)
        # END OF ADD FUNCTION

    # SEARCH DOCK FUNCTIONS

    # SEARCH BUTTON
    def search(self, intColumns):
        """
        Function to handle the search button click event.
        Constructs a SQL query based on the search term, filter and sort options selected by the user.
        Calls the displayTable function to display the results of the query in a table.

        Parameters:
        intColumns (list): A list of column names that contain integer values in the database table.

        Returns:
        None
        """
        # initialise query parts

        # Term Field
        term = self.searchField.text()
        # Handle empty search field
        if term == "":
            QMessageBox.warning(self, "Search error", "Please enter a search term")
            return term

        # Filter Field
        filter = self.filterField.currentText()
        # Handle filter not choosen
        if filter == "Required":
            QMessageBox.warning(self, "Filter error", "Please choose a valid filter")
            return filter

        if filter in intColumns and term.isdigit():
            filterStatement = f" WHERE {filter} = {int(term)}"
        else:
            filterStatement = f" WHERE {filter} = '{term}'"

        # Sortby Field
        orderby = self.orderbyField.currentText()
        order = self.orderField.currentText()
        # Handle orderby not choosen
        orderbyStatement = ""
        if orderby == "Optional":
            orderbyStatement = ""
        else:
            if order == "Asc":
                orderbyStatement = f" ORDER BY {orderby} ASC"
            elif order == "Desc":
                orderbyStatement = f" ORDER BY {orderby} DESC"

        # concatenate query parts
        compoundQuery = (
            self.selectQuery + "\n" + filterStatement + "\n" + orderbyStatement
        )
        # print(compoundQuery)

        # call displayTable function to display result
        self.displayTable(compoundQuery)

    # CLEAR FILTERS BUTTON
    def clearFilters(self):
        """
        Clears the search field, filter field, orderby field, order field and table.
        Calls the displayTable function to display all values in the table.
        """
        self.searchField.clear()
        self.filterField.setCurrentIndex(0)
        self.orderbyField.setCurrentIndex(0)
        self.orderField.setCurrentIndex(0)
        self.table.setRowCount(0)
        self.displayTable(self.selectQuery)

    ##################### END OF BUTTON FUNCTIONS #####################

    # FUNCTION to Execute SQL QUERY without values returned

    def sqlExecute(self, query):
        """
        Function to execute a SQL query on the database.

        Args:
            query (str): The SQL query to execute.

        Returns:
            None

        Raises:
            QMessageBox.critical: If there is an error connecting to or executing the query on the database.

        """
        # initialize the connection variable
        connection = None
        try:
            connection = cx_Oracle.connect("elom/elom@localhost:1521/VVBANKING")

        except cx_Oracle.Error as err:
            QMessageBox.critical(
                self,
                "Database Connection Error",
                "\n" + str(err) + "\n" + "Please contact the database administrator",
            )

        else:
            try:
                cursor = connection.cursor()
                cursor.execute(query)

            except cx_Oracle.Error as err:
                QMessageBox.critical(
                    self,
                    "Couldn't Execute Query",
                    "\n" + str(err) + "\n" + "Please contact the administrator",
                )

            else:
                cursor.close()

        finally:
            if connection is not None:
                connection.close()

    # FUNCTION to Execute SQL QUERY and display values in a table
    # Display the results of a SQL query in a table
    def displayTable(self, query):
        """
        Given a SQL query, fetches the data from the database and displays it in a table.

        Args:
            query (str): The SQL query to execute.

        Returns:
            None.
        """
        # initialize the connection variable
        connection = None
        try:
            connection = cx_Oracle.connect("elom/elom@localhost:1521/VVBANKING")

        except cx_Oracle.Error as err:
            QMessageBox.critical(
                self,
                "Database Connection Error",
                "\n" + str(err) + "\n" + "Please contact the database administrator",
            )

        else:
            try:
                cursor = connection.cursor()
                cursor.execute(query)

            except cx_Oracle.Error as err:
                QMessageBox.critical(
                    self,
                    "Couldn't Fetch Data",
                    "\n" + str(err) + "\n" + "Please contact the administrator",
                )

            else:
                # Grab cursor result
                result = cursor.fetchall()

                # Display the results in the table
                self.table.setColumnCount(len(cursor.description))
                self.table.setRowCount(len(result))
                self.table.setHorizontalHeaderLabels(
                    [description[0] for description in cursor.description]
                )

                for row_idx, row in enumerate(result):
                    for col_idx, value in enumerate(row):
                        # Check if the value is a datetime
                        if isinstance(value, datetime.datetime):
                            item = QTableWidgetItem(value.strftime("%d-%b-%Y").upper())
                        else:
                            item = QTableWidgetItem(str(value))
                        self.table.setItem(row_idx, col_idx, item)

                cursor.close()

        finally:
            if connection is not None:
                connection.close()

    # Secondary functions for the ADD BUTTON

    #  Insert function
    # Function to insert data into the database
    def dataInsert(self, query, data):
        """
        Inserts data into the database using the provided query and data.

        Args:
        query (str): The SQL query to execute.
        data (tuple): The data to insert into the database.

        Returns:
        None
        """
        # set connection to None to initialise variable
        connection = None
        cursor = None
        try:
            connection = cx_Oracle.connect("elom/elom@localhost:1521/VVBANKING")
            try:
                cursor = connection.cursor()
                cursor.execute(
                    """
                    ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD'
                    """
                )
                cursor.execute(query, data)
            except cx_Oracle.Error as err:
                QMessageBox.critical(
                    self, "Database Error", str(err) + "\n" + "Insert Error"
                )
            else:
                connection.commit()
                # refresh table
                self.table.setRowCount(0)  # clear table keeping headers
                self.displayTable(self.selectQuery)
                # Notify user of successful insert
                QMessageBox.information(self, "Data Insert", "New Record Added")
            finally:
                if cursor is not None:
                    cursor.close()

        except cx_Oracle.Error as err:
            QMessageBox.critical(
                self,
                "Database Error",
                str(err)
                + "\n"
                + "Failed to connect to database"
                + "\n"
                + "Please contact the database administrator",
            )

        finally:
            if connection is not None:
                connection.close()

    ##################### MENU BAR FUNCTIONS #####################

    # Open New Record Dock
    def newRecord(self):
        """
        Displays the New Record Dock widget when the 'New Record' button is clicked.
        """
        self.NewRecordDock.show()

    # Delete selected record from database
    def delRecord(self):
        """
        Deletes the currently selected record from the database.

        If no record is selected, a warning message is displayed to the user.

        If a record is selected, a confirmation message is displayed to the user.

        If the user confirms the delete, the record is deleted from the database and the table is refreshed.

        If the user cancels the delete, no action is taken.

        Returns:
        - None
        """
        currentRow = self.table.currentRow()
        if currentRow == -1:
            return QMessageBox.warning(
                self, "No Record Selected", "Please select a record to delete"
            )

        # Ask user to confirm delete
        msg = QMessageBox.question(
            self,
            "Confirmation",
            "Do you really want to delete this record?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if msg == QMessageBox.StandardButton.Yes:
            # Get the ID of the selected record
            recordIDItem = self.table.item(currentRow, 0)
            if recordIDItem is None:
                return QMessageBox.warning(
                    self, "No Record Selected", "Please select a record to delete"
                )
            recordID = recordIDItem.text()

            # Get the ID header
            header = self.table.horizontalHeaderItem(0)
            if header is None:
                return QMessageBox.warning(
                    self, "No Record Selected", "Please select a record to delete"
                )
            header = header.text()

            # Delete the record from the database
            delQuery = f"DELETE FROM CUSTOMERS WHERE {header} = {int(recordID)}"
            # print(delQuery)
            self.sqlExecute(delQuery)
            # Refresh the table
            self.table.setRowCount(0)
            self.displayTable(self.selectQuery)
            # Notify user of successful delete
            QMessageBox.information(self, "Record Deleted", "Record has been deleted")

    # Save button: Commit changes to the database
    def saveChanges(self):
        """
        Commits changes made to the database and notifies the user of the successful commit.
        """
        # Ask user to confirm commit
        msgBoxBtn = QMessageBox.StandardButton
        msgBoxBtn = msgBoxBtn.Yes | msgBoxBtn.Cancel
        msgBox = QMessageBox.question(
            self,
            "Confirm Commit",
            "Do you really want to commit changes?",
            msgBoxBtn,
        )
        # Button choice action
        if msgBox == msgBoxBtn.Yes:
            self.sqlExecute("COMMIT")
            # Notify user of successful commit
            QMessageBox.information(
                self, "Changes Saved", "Changes of this session have been saved"
            )
        elif msgBox == msgBoxBtn.Cancel:
            pass

    # Rollback transactions
    def undoChanges(self):
        """
        Reverts changes made to the database and notifies the user of the successful rollback.
        """
        # Ask user to confirm rollback
        message = "Do you really want to revert changes?"
        msgBoxBtn = QMessageBox.StandardButton
        msgBoxBtn = msgBoxBtn.Yes | msgBoxBtn.Cancel
        msgBox = QMessageBox.question(self, "Confirm Rollback", message, msgBoxBtn)
        # Button choice action
        if msgBox == msgBoxBtn.Yes:
            self.sqlExecute("ROLLBACK")
            # Notify user of successful rollback
            QMessageBox.information(
                self, "Changes Reverted", "Changes have been reverted"
            )
        elif msgBox == msgBoxBtn.Cancel:
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
        """
        Displays the search dock widget when called.
        """
        self.SearchDock.show()

    # Open About window
    def about(self):
        """
        Displays an 'About' message box with information about the application.
        """
        QMessageBox.about(self, "About", "This is a simple bank management application")

    ##################### END OF MENU BAR FUNCTIONS #####################

    ##################### CENTER FUNCTION #####################
    def showEvent(self, event):
        """
        Overrides the default showEvent() function to center the main window on the screen when it is shown.
        """
        self.center()
        super().showEvent(event)

    def center(self):
        """
        Centers the main window on the screen.
        """
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
        accwindow = accounts()

        # show the window
        accwindow.show()

        # DARK THEME
        # https://pypi.org/project/pyqtdarktheme/
        # pip install pyqtdarktheme
        # Apply the complete dark theme to Qt App.
        qdarktheme.setup_theme("auto")

        # start the event loop
        sys.exit(app.exec())
