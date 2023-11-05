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
import cx_Oracle
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


class entityWindow(QMainWindow):
    def __init__(self, entity: str, attributes: list, intAttributes: list):
        """
        Initializes entity window.
        """
        super().__init__()

        # set entity name
        self.entity = entity
        self.filters = attributes
        self.intColumns = intAttributes

        # set the window title
        self.setWindowTitle(f"WEL Bank - {self.entity}")

        # set WINDOW ICON (icons from icons8.com)
        self.setWindowIcon(QIcon(resource_path("./assets/bank.png")))

        # Set window size
        width = 800
        height = 600
        self.resize(width, height)

        # center the window, center function defined below
        self.center()

        # initialize member of other windows
        # self.cusServDashboard = None

        # create the UI
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface for the window.
        """

        ########################### MENU BAR ###########################
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
            QIcon(resource_path("./assets/add.png")), "&New Record", self
        )
        addAction.setStatusTip("Add a new record")
        addAction.setShortcut("Ctrl+N")
        addAction.triggered.connect(self.newRecord)
        self.fileMenu.addAction(addAction)  # type: ignore

        # 'Delete' menu item
        delAction = QAction(
            QIcon(resource_path("./assets/remove.png")),
            "&Delete",
            self,
        )
        delAction.setStatusTip("Delete a record")
        delAction.setShortcut("Del")
        delAction.triggered.connect(self.delRecord)
        self.fileMenu.addAction(delAction)  # type: ignore

        # 'Save' menu item
        saveAction = QAction(
            QIcon(resource_path("./assets/save.png")),
            "&Save Changes",
            self,
        )
        saveAction.setStatusTip("Save (Commit) changes to the database")
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.saveChanges)

        # add Separator after save
        self.fileMenu.addSeparator()  # type: ignore

        # 'Exit' menu item
        exitAction = QAction(
            QIcon(resource_path("./assets/exit.png")),
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
            QIcon(resource_path("./assets/rollback.png")),
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
            QIcon(resource_path("./assets/cut.png")),
            "&Cut",
            self,
        )
        cutAction.setStatusTip("Cut")
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.cut)
        self.editMenu.addAction(cutAction)  # type: ignore

        # 'Copy' menu item
        copyAction = QAction(
            QIcon(resource_path("./assets/copy.png")),
            "&Copy",
            self,
        )
        copyAction.setStatusTip("Copy")
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.copy)
        self.editMenu.addAction(copyAction)  # type: ignore

        # 'Paste' menu item
        pasteAction = QAction(
            QIcon(resource_path("./assets/paste.png")),
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
            QIcon(resource_path("./assets/search.png")),
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
            QIcon(resource_path("./assets/info.png")),
            "&About",
            self,
        )
        aboutAction.setStatusTip("Help")
        aboutAction.setShortcut("F1")
        aboutAction.triggered.connect(self.about)
        self.helpMenu.addAction(aboutAction)  # type: ignore

        ################# END OF MENU BAR #################

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
        ########## ENF OF TOOLBAR ##########

        # Create status bar
        statusBar = self.statusBar()
        # display the a message in 5 seconds
        statusBar.showMessage("Ready", 5000)  # type: ignore

        ########################### WIDGETS CREATION ###########################
        ### VBOX WIDGETS ###
        # Customers label
        self.tableLabel = QLabel(f"{self.entity}", self)

        # Customers Table
        self.table = QTableWidget(self)

        # BACK BUTTON
        self.backButton = QPushButton("Back", clicked=lambda: self.back())  # type: ignore
        ### END OF VBOX WIDGETS ###
        ####################### END OF WIDGETS CREATION ########################

        ############################ LAYOUT ############################
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.NewForm = QFormLayout()
        self.SearchForm = QFormLayout()

        ###################### ADD WIDGETS TO vbox LAYOUT ######################
        # Customers label
        self.vbox.addWidget(self.tableLabel, alignment=Qt.AlignmentFlag.AlignLeft)

        # Customers Table
        self.vbox.addWidget(self.table)

        # query to display entity data
        self.selectQuery = f"SELECT * FROM {self.entity}"

        # Call the function to display values in the table
        self.displayTable(self.selectQuery)

        # BACK BUTTON
        self.vbox.addWidget(self.backButton, alignment=Qt.AlignmentFlag.AlignRight)
        ###################### END OF ADD WIDGETS TO vbox LAYOUT ######################

        #################################
        # Nest vbox in hbox             #
        self.hbox.addLayout(self.vbox)  #
        #################################

        # NEW RECORD DOCK
        self.newRecordDock()

        ####################### SEARCH DOCK #######################
        ################## SEARCH FORM WIDGETS ##################
        # Search Field
        self.searchField = QLineEdit(self)
        self.searchField.setPlaceholderText("Enter a search term")
        # Filter Field
        self.filterField = QComboBox(self)
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
        self.searchButton = QPushButton("Search", clicked=lambda: self.search(self.intColumns))  # type: ignore

        # CLEAR BUTTON
        self.clearButton = QPushButton("Clear", clicked=lambda: self.clearFilters())  # type: ignore
        ############################ END OF CREATION SEARCH FORM WIDGETS ############################

        ############# ADD WIDGETS TO SearchForm LAYOUT #############
        self.SearchForm.addRow(self.searchField)
        self.SearchForm.addRow("Filter by", self.filterField)
        self.SearchForm.addRow("Sort by", self.orderbyField)
        self.SearchForm.addRow("Order", self.orderField)
        self.SearchForm.addRow(self.searchButton)
        self.SearchForm.addRow(self.clearButton)
        ########## END OF ADD WIDGETS TO SearchForm LAYOUT ##########

        ########################### SEARCH DOCK CREATION ###########################
        # ADD DOCK WIDGET FOR SEARCH
        self.SearchDock = QDockWidget("Search", self)
        # SearchDock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.SearchDock)
        # ADD WIDGETS TO SEARCH DOCK
        self.SearchDockWidget = QWidget(self)
        self.SearchDockWidget.setLayout(self.SearchForm)
        self.SearchDock.setWidget(self.SearchDockWidget)
        ####################### END OF SEARCH DOCK CREATION #######################

        ###########################  NEW RECORD DOCK CREATION ###########################
        # ADD DOCK WIDGET FOR NEW RECORD
        self.NewRecordDock = QDockWidget("New Record")
        # NewDock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.NewRecordDock)
        # ADD WIDGETS TO NEW CUSTOMER DOCK
        self.NewRecordDockWidget = QWidget(self)
        self.NewRecordDockWidget.setLayout(self.NewForm)
        self.NewRecordDock.setWidget(self.NewRecordDockWidget)
        ####################### END OF NEW RECORD DOCK CREATION #######################

        ######## CENTER WINDOW CONTENT ##########
        self.container = QWidget()
        self.container.setLayout(self.hbox)
        self.setCentralWidget(self.container)
        #########################################

        ########################## END OF LAYOUT ##########################

    ######################### UI FUNCTION: NEW RECORD DOCK #########################
    def newRecordDock(self):
        pass

    ####################################### BUTTON FUNCTIONS #######################################
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
        from win_02_2_HRDashboard import hrDashboard

        if self.entity in [
            "Customers",
            "Accounts",
            "Cards",
            "Transactions",
            "Loans",
            "Loans_Payment",
        ]:
            self.cusServDashboard = cusServDashboard()
            self.hide()
            self.cusServDashboard.show()
        else:
            self.hrDashboard = hrDashboard()
            self.hide()
            self.hrDashboard.show()

    ############################### SEARCH DOCK FUNCTIONS ###############################
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
            filterStatement = f" WHERE {filter} = {float(term)}"
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

    ####################################### END OF BUTTON FUNCTIONS #######################################

    ##################### SECONDARY FUNCTIONS #####################
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
            connection = cx_Oracle.connect("welbank/12345@localhost:1521/WELBANK")

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
                # Notify user of successful delete
                QMessageBox.information(
                    self, "Query Execution", "Query has been executed succesfully"
                )
                cursor.close()

        finally:
            if connection is not None:
                connection.close()

    # FUNCTION to Execute SQL QUERY and display values in a table
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
            connection = cx_Oracle.connect("welbank/12345@localhost:1521/WELBANK")

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
    # Insert function
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
            connection = cx_Oracle.connect("welbank/12345@localhost:1521/WELBANK")
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
                    self, "Database Error", str(err) + "\n" + "Insertion Error"
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

    # Function to calculate age of the customer
    def age(self, dateofbirth):
        """
        Calculates the age of a customer based on their date of birth.

        Args:
        - dateofbirth (str): A string representing the customer's date of birth in the format "yyyy-MM-dd".

        Returns:
        - age (int): The age of the customer in years.
        """
        # Convert string to date object
        birthDate = QDate.fromString(dateofbirth, "yyyy-MM-dd")
        # Get the current date
        currentDate = QDate.currentDate()
        # Calculate the age of the customer
        age = currentDate.year() - birthDate.year()
        # Check if the birth date has not yet occured within the current year
        if (currentDate.month(), currentDate.day()) < (
            birthDate.month(),
            birthDate.day(),
        ):
            age -= 1

        return age

    ##################### SECONDARY FUNCTIONS #####################

    ############################# MENU BAR FUNCTIONS #############################
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
        else:
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
                else:
                    recordID = recordIDItem.text()

                # Get the ID header
                header = self.table.horizontalHeaderItem(0)
                if header is None:
                    return QMessageBox.warning(
                        self, "No Record Selected", "Please select a record to delete"
                    )
                else:
                    header = header.text()
                    # Delete the record from the database
                    self.delQuery = (
                        f"DELETE FROM {self.entity} WHERE {header} = {recordID}"
                    )
                    # print(f"DELETE FROM {self.entity} WHERE {header} = {recordID}")
                    self.sqlExecute(self.delQuery)
                    # Refresh the table
                    self.table.setRowCount(0)
                    self.displayTable(self.selectQuery)

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

    ############################# CENTER FUNCTION #############################
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
    # END OF entityWindow CLASS


cusAttrib = [
    "CUS_ID",
    "NAT_ID",
    "CUS_FN",
    "CUS_LN",
    "GENDER",
    "CUS_DOB",
    "NATIONALITY",
    "CUS_EMAIL",
    "CUS_PHONE",
    "OCCUPATION",
    "CUS_ADDR",
    "BRCH_ID",
    "EMP_ID",
]
intCusAttrib = ["CUS_ID", "CUS_PHONE", "BRCH_ID", "EMP_ID"]


class customers(entityWindow):
    def __init__(self):
        super().__init__(
            entity="Customers", attributes=cusAttrib, intAttributes=intCusAttrib
        )

    ###### ENTITY SPECIFIC FUNCTIONS ######
    def newRecordDock(self):
        ###################################### NEW RECORD DOCK ######################################

        ################## CREATION NEW CUSTOMER FORM WIDGETS ##################
        # regExp = Regular Expression | validator = val
        # Customer ID field
        self.customerIDField = QLineEdit(self)
        self.customerIDField.setPlaceholderText("1 or 5 + (7 digits)")
        self.customerIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[1|5][0-9]{7}"))
        )
        # National ID field
        self.nationalIDField = QLineEdit(self)
        self.nationalIDField.setPlaceholderText(
            "XXX-XXXXXXXXX-X" + " (e.g. GHA-456789012-3)"
        )
        self.nationalIDField.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("[A-Z]{3}-[0-9]{9}-[0-9]{1}")
            )
        )
        # First Name field
        self.firstNameField = QLineEdit(self)
        self.firstNameField.setValidator(
            QRegularExpressionValidator(
                QRegularExpression(r"^[A-Z][a-z]*(([\- ][A-Z])[a-z]*)*$")
            )
        )
        # Last Name field
        self.lastNameField = QLineEdit(self)
        self.lastNameField.setValidator(
            QRegularExpressionValidator(
                QRegularExpression(r"^[A-Z][a-z]*(([\- ][A-Z])[a-z]*)*$")
            )
        )
        # Gender
        self.genderField = QComboBox(self)  # by default editable=False
        self.genderField.addItems(["", "Female", "Male"])
        # Date of Birth Field
        self.dateOfBirthField = QDateEdit(self)
        self.dateOfBirthField.setDisplayFormat("yyyy-MM-dd")
        # Nationality Field
        self.nationalityField = QComboBox(self)
        self.nationalities = [
            "",
            "American",
            "Beninese",
            "British",
            "Burkinabe",
            "Chinese",
            "French",
            "German",
            "Ghanaian",
            "Indian",
            "Ivorian",
            "Lebanese",
            "Liberian",
            "Malian",
            "Nigerian",
            "Nigerien",
            "Senegalese",
            "South African",
            "Togolese",
        ]
        # add nationalities to the drop down menu
        self.nationalityField.addItems(self.nationalities)
        # Email Field
        self.emailField = QLineEdit(self)
        self.emailField.setPlaceholderText("example@example.com")
        # Phone Number Field
        self.phoneNumberField = QLineEdit(self)
        self.phoneNumberField.setPlaceholderText("e.g. 24XXXXXXX (9 digits)")
        self.phoneNumberField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[2|5][0-9]{8}"))
        )
        # Occupaton Field
        self.occupationField = QLineEdit(self)
        self.occupationField.setPlaceholderText("Occupation")
        # Address Field
        self.addressField = QComboBox(self, editable=True)  # type: ignore
        self.addressField.setPlaceholderText("e.g. East Legon")
        self.addresses = [
            "",
            "Accra",
            "East Legon",
            "Madina",
            "Achimota",
            "Botwe",
            "Adenta",
            "Spintex",
            "Tema",
            "Aflao",
            "Lapaz",
            "Osu",
            "Dansoman",
            "Kaneshie",
            "Kasoa",
            "Kumasi",
            "Takoradi",
            "Tamale",
            "Ashaiman",
            "Ho",
            "Akatsi",
            "Asikuma",
            "Amedzofe",
            "Donkorkrom",
            "Hohoe",
            "Akossombo",
            "Kpeve",
        ]
        # add addresses to the drop down menu
        self.addressField.addItems(self.addresses)
        # Branch ID Field
        self.branchIDField = QComboBox(self)
        self.branchIDField.addItems(["", "1", "5"])
        # Employee ID Field
        self.employeeIDField = QComboBox(self)
        self.employeeIDField.addItems(
            ["", "1102001", "1102002", "1102003", "5102001", "5102002", "5102003"]
        )

        # ADD BUTTON
        self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore
        # CANCEL BUTTON
        self.cancelButton = QPushButton("Clear", clicked=lambda: self.cancel())  # type: ignore
        ############### END OF CREATION 'NEW RECORD' FORM WIDGETS ###############

        ############ ADD WIDGETS TO NewForm LAYOUT ############
        self.NewForm.addRow("Customer ID", self.customerIDField)
        self.NewForm.addRow("National ID", self.nationalIDField)
        self.NewForm.addRow("First Name", self.firstNameField)
        self.NewForm.addRow("Last Name", self.lastNameField)
        self.NewForm.addRow("Gender", self.genderField)
        self.NewForm.addRow("Date of Birth", self.dateOfBirthField)
        self.NewForm.addRow("Nationality", self.nationalityField)
        self.NewForm.addRow("Email", self.emailField)
        self.NewForm.addRow("Phone Number", self.phoneNumberField)
        self.NewForm.addRow("Occupation", self.occupationField)
        self.NewForm.addRow("Address", self.addressField)
        self.NewForm.addRow("Branch ID", self.branchIDField)
        self.NewForm.addRow("Personal Banker ID", self.employeeIDField)
        self.NewForm.addRow(self.addButton)
        self.NewForm.addRow(self.cancelButton)
        ########## END OF ADD WIDGETS TO NewForm LAYOUT ##########
        ###################### END OF NEW RECORD DOCK ######################

    ############################### 'ADD NEW RECORD' FORM FUNCTIONS ###############################
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
            self.customerIDField.clear()
            self.nationalIDField.clear()
            self.firstNameField.clear()
            self.lastNameField.clear()
            self.genderField.setCurrentIndex(0)
            self.dateOfBirthField.setDate(QDate.currentDate())
            self.nationalityField.setCurrentIndex(0)
            self.emailField.clear()
            self.phoneNumberField.clear()
            self.occupationField.clear()
            self.addressField.setCurrentIndex(0)
            self.branchIDField.setCurrentIndex(0)
            self.employeeIDField.setCurrentIndex(0)
        else:
            pass

    # ADD BUTTON
    # Primary function: Add function (insert logic)
    def add(self):
        """
        This method is called when the user clicks the "Add" button in the GUI. It retrieves the data entered by the user
        in the various fields, validates the data, and inserts a new record into the " " table in the database.
        """

        self.insertQuery = f"""
                insert into {self.entity} values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)
                """

        ### GRAB TEXT IN THE FIELDS AND ADD LOGIC ###
        self.customerID = self.customerIDField.text()
        self.nationalID = self.nationalIDField.text()
        self.firstName = self.firstNameField.text()
        self.lastName = self.lastNameField.text()
        self.gender = self.genderField.currentText()
        self.dateOfBirth = self.dateOfBirthField.text()
        self.nationality = self.nationalityField.currentText()
        self.email = self.emailField.text()
        self.phoneNumber = self.phoneNumberField.text()
        self.occupation = self.occupationField.text()
        self.address = self.addressField.currentText()
        self.branchID = self.branchIDField.currentText()
        self.employeeID = self.employeeIDField.currentText()

        self.columnsData = [
            self.customerID,
            self.nationalID,
            self.firstName,
            self.lastName,
            self.gender,
            self.dateOfBirth,
            self.nationality,
            self.email,
            self.phoneNumber,
            self.occupation,
            self.address,
            self.branchID,
            self.employeeID,
        ]
        ################# FIELDS VALIDATI0N LOGIC #################
        ### Customer ID field ###
        if self.customerID == "" or len(str(self.customerID)) != 8:
            QMessageBox.warning(
                self,
                "Invalid Customer ID",
                "Please enter a valid customer ID (8 digits)",
            )
            return self.customerID
        else:
            # convert customerID to integer
            self.customerID = int(self.customerID)

        ### National ID field ###
        if self.nationalID == "" or len(self.nationalID) != 15:
            QMessageBox.warning(
                self,
                "Invalid National ID",
                "Please enter a valid national ID (15 digits)",
            )
            return self.nationalID

        ### First Name field ###
        if self.firstName == "" or self.firstName[-1] == "-":
            QMessageBox.warning(
                self, "Invalid First Name", "Please enter a valid first name"
            )
            return self.firstName

        ### Last Name field ###
        if self.lastName == "" or self.lastName[-1] == "-":
            QMessageBox.warning(
                self, "Invalid Last Name", "Please enter a valid last name"
            )
            return self.lastName

        ### Gender field ###
        if self.gender == "":
            QMessageBox.warning(self, "Invalid Gender", "Please select a valid gender")
            return self.gender

        ### Date of Birth field ###
        # Check if the customer is already 18
        if self.age(self.dateOfBirth) < 18:
            QMessageBox.warning(
                self,
                "Invalid Date of Birth",
                "Customer must be at least 18 years old",
            )
            return self.dateOfBirth

        ### Nationality field ###
        if self.nationality == "":
            QMessageBox.warning(
                self, "Invalid Nationality", "Please enter a valid nationality"
            )
            return self.nationality

        ### Email field ###
        if (
            self.email == ""
            or "@" not in self.email
            or "." not in self.email.split("@")[1]
        ):
            QMessageBox.warning(self, "Invalid Email", "Please enter a valid email")
            return self.email

        ### Phone Number field ###
        if self.phoneNumber == "" or len(str(self.phoneNumber)) != 9:
            QMessageBox.warning(
                self, "Invalid Phone Number", "Please enter a valid phone number"
            )
            return self.phoneNumber
        else:
            self.phoneNumber = int(self.phoneNumber)

        ### Occupation field ###
        if self.occupation == "" or self.occupation.isnumeric():
            QMessageBox.warning(
                self, "Invalid Occupation", "Please enter a valid occupation"
            )
            return self.occupation

        ### Address field ###
        if self.address == "":
            QMessageBox.warning(
                self, "Invalid Address", "Please choose or enter a valid address"
            )
            return self.address

        ### Branch ID field ###
        if self.branchIDField.currentText() == "":
            QMessageBox.warning(
                self, "Invalid Branch ID", "Please choose a valid branch ID"
            )
            return self.branchIDField.currentText()
        elif self.customerIDField.text()[0] != self.branchIDField.currentText()[0]:
            QMessageBox.warning(
                self,
                "Invalid Branch ID",
                "Branch ID must match the first digit of the customer ID",
            )
            return self.branchIDField.currentText()
        else:
            self.branchID = int(self.branchIDField.currentText())

        ### Employee ID field ###
        if self.employeeIDField.currentText() == "":
            QMessageBox.warning(
                self, "Invalid Employee ID", "Please choose a valid employee ID"
            )
            return self.employeeIDField.currentText()
        elif self.customerIDField.text()[0] != self.employeeIDField.currentText()[0]:
            QMessageBox.warning(
                self,
                "Invalid Employee ID",
                "Employee ID must match the first digit of the customer ID",
            )
            return self.employeeIDField.currentText()
        else:
            self.employeeID = int(self.employeeIDField.currentText())

        # execute the insert query and ask to clear fields
        self.dataInsert(self.insertQuery, self.columnsData)
        self.cancel()
        # END OF ADD FUNCTION

    ############################### END OF ADD NEW RECORD FORM FUNCTIONS ###############################


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
        cuswindow = customers()
        cuswindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
