from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QTableWidget,
    QListWidget,
    QMessageBox,
    QTableWidgetItem,
    QFileDialog,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication, QIcon

# other modules
import cx_Oracle
import sqlite3
import datetime
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


class queryInterface(QMainWindow):
    def __init__(self, dep: str):
        super().__init__()

        self.dep = dep
        # set the window title
        windowTitle = f"WEL Bank - {self.dep} Query Interface"
        self.setWindowTitle(windowTitle)

        # initialise sqlite3 DB
        self.connDB()

        # set WINDOW ICON
        self.setWindowIcon(QIcon(resource_path("./assets/query.png")))

        # Set window size
        width = 800
        height = 600
        self.resize(width, height)

        # center the window, center function defined below
        self.center()

        # initialize the cusServDashboard member to None in the welcome class
        self.cusServDashboard = None

        # create the user interface
        self.initUI()

    # user interface function
    def initUI(self):
        ########################### ADD WIDGETS ###########################

        # Data Query Tool
        self.dataQueryToolLabel = QLabel("Data Query Tool")
        self.dataQueryToolLabel.setFont(QFont("Arial", 24))
        self.dataQueryToolLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Enter Your Query
        self.enterYourQueryLabel = QLabel("Enter Your Query:")

        # Query Field - QTextEdit
        self.queryField = QTextEdit()
        self.queryField.setPlaceholderText("Enter your query here")
        self.queryField.setFixedHeight(100)  # set Fixed Height to 100

        # Execute Query Button
        self.executeQueryButton = QPushButton("Execute Query", clicked=lambda: self.executeQuery())  # type: ignore

        # QUERY RESULTS: QTableWidget
        self.queryResultsTable = QTableWidget()

        # Export to Excel Button
        self.exportToExcelButton = QPushButton("Export to Excel", clicked=lambda: self.exportToExcel())  # type: ignore

        # BACK BUTTON
        self.backButton = QPushButton("Back", clicked=lambda: self.back())  # type: ignore

        # Previous Queries
        self.previousQueriesLabel = QLabel("Previous Queries")
        # QLISTWIDGET
        self.listQueries = QListWidget(self)
        # Clear button
        self.clearButton = QPushButton("Clear", clicked=lambda: self.clear())  # type: ignore
        # Delete query button
        self.deleteButton = QPushButton("Delete Query", clicked=lambda: self.delete())  # type: ignore
        ####################### END OF ADD WIDGETS ########################

        ############################## LAYOUT ##############################

        hbox = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()

        ### ADD WIDGETS TO vbox1 ###

        # Data Query Tool
        vbox1.addWidget(self.dataQueryToolLabel)

        # set spacing between previous widget and next widget
        vbox1.addSpacing(20)

        # Enter Your Query
        vbox1.addWidget(self.enterYourQueryLabel)

        # Query Field - QTextEdit
        vbox1.addWidget(self.queryField)

        # ADD AUTOCOMPLETE FUNCTIONALITY TO QUERY FIELD
        # !!!!!! NEED TO ADD THIS !!!!!!

        # Execute Query Button
        vbox1.addWidget(self.executeQueryButton)

        # QUERY RESULTS: QTableWidget
        vbox1.addWidget(self.queryResultsTable)

        # Export to Excel Button
        vbox1.addWidget(self.exportToExcelButton)

        # BACK BUTTON
        vbox1.addWidget(self.backButton)

        ### END ADD WIDGETS TO vbox1 ###

        # NEST vbox1 in hbox
        hbox.addLayout(vbox1, 2)

        ### ADD WIDGETS TO vbox2 ###

        # Label Previous Queries
        vbox2.addWidget(self.previousQueriesLabel)
        # QLISTWIDGET
        vbox2.addWidget(self.listQueries)
        # Delete query button
        vbox2.addWidget(self.deleteButton)
        # Clear button
        vbox2.addWidget(self.clearButton)

        ### END ADD WIDGETS TO vbox2 ###

        # NEST vbox2 in hbox
        hbox.addLayout(vbox2, 1)

        ### END ADD WIDGETS TO hbox ###

        ### Center window content ###
        container = QWidget()
        container.setLayout(hbox)
        self.setCentralWidget(container)
        ########################## END OF LAYOUT ##########################

        # Grab data from database
        self.grabFromDB()

    ##################### BUTTON FUNCTIONS #####################
    # Execute Query Button
    def executeQuery(self):
        self.query = self.queryField.toPlainText()
        self.displayTable(self.query, self.dep)
        # Add query to list
        self.listQueries.addItem(self.query)
        # Clear query field
        self.queryField.clear()
        # save queries to db
        self.saveQueriesToDB()

    # Export to Excel Button
    def exportToExcel(self):
        # print("Exported to Excel")
        import pandas as pd

        options = QFileDialog().options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export to Excel",
            "",
            "Excel Files (*.xlsx);;All Files (*)",
            options=options,
        )

        if file_path:
            try:
                connection = cx_Oracle.connect("welbank/12345@localhost:1521/WELBANK")  # type: ignore
                cursor = connection.cursor()

                # Execute the query
                cursor.execute(self.query.strip())
                result = cursor.fetchall()

                # Convert result to a DataFrame
                df = pd.DataFrame(
                    result,
                    columns=[description[0] for description in cursor.description],
                )

                # Export DataFrame to Excel
                df.to_excel(file_path, index=False)

                cursor.close()
                connection.close()

                QMessageBox.information(self, "Export to Excel", "Export Successful")

            except Exception as e:
                QMessageBox.warning(
                    self, "Export to Excel", f"Error exporting to Excel - {str(e)}"
                )

    # BACK BUTTON
    def back(self):
        from win_02_1_CusServDashboard import cusServDashboard
        from win_02_2_HRDashboard import hrDashboard

        if self.dep == "CS":
            self.cusServDashboard = cusServDashboard()
            self.hide()
            self.cusServDashboard.show()
        elif self.dep == "HR":
            self.hrDashboard = hrDashboard()
            self.hide()
            self.hrDashboard.show()

    # Clear previous queries button
    def clear(self):
        # Create a database or connect to one
        conn = sqlite3.connect(resource_path("./data/queriesList.db"))
        cur = conn.cursor()
        # create table to store queries
        if self.dep == "CS":
            cur.execute("DELETE FROM QUERIES_LIST_CS")
        elif self.dep == "HR":
            cur.execute("DELETE FROM QUERIES_LIST_HR")
        # commit changes
        conn.commit()
        cur.close()
        conn.close()
        # clear the list
        self.listQueries.clear()

    # Delete query button
    def delete(self):
        # Grab the selected row
        self.selectedRow = self.listQueries.currentRow()
        # Delete selected row
        self.listQueries.takeItem(self.selectedRow)
        # Create a database or connect to one
        conn = sqlite3.connect(resource_path("./data/queriesList.db"))
        cur = conn.cursor()

        # create table to store queries
        if self.dep == "CS":
            cur.execute(
                f"delete from QUERIES_LIST_CS where rowid = {self.selectedRow + 1} "
            )
        elif self.dep == "HR":
            cur.execute(
                f"delete from QUERIES_LIST_HR where rowid = {self.selectedRow + 1} "
            )
        # commit changes
        conn.commit()
        cur.close()
        conn.close()

    # SECONDARY FUNCTIONS
    def saveQueriesToDB(self):
        conn = sqlite3.connect(resource_path("./data/queriesList.db"))
        cur = conn.cursor()
        if self.dep == "CS":
            cur.execute("DELETE FROM QUERIES_LIST_CS")
        elif self.dep == "HR":
            cur.execute("DELETE FROM QUERIES_LIST_HR")
        # initialize list to hold queries
        self.items = []
        # loop through listWidget to pull out each query/item
        for index in range(self.listQueries.count()):
            self.items.append(self.listQueries.item(index))

        for item in self.items:
            # add items to the database
            if self.dep == "CS":
                cur.execute(
                    f"INSERT INTO QUERIES_LIST_CS VALUES (:item)",
                    {
                        "item": item.text(),
                    },
                )
            elif self.dep == "HR":
                cur.execute(
                    f"INSERT INTO QUERIES_LIST_HR VALUES (:item)",
                    {
                        "item": item.text(),
                    },
                )

        # DB operations
        conn.commit()
        cur.close()
        conn.close()

    def grabFromDB(self):
        # Create a database or connect to one
        conn = sqlite3.connect(resource_path("./data/queriesList.db"))
        cur = conn.cursor()

        # create table to store queries
        if self.dep == "CS":
            query = """
                select * from QUERIES_LIST_CS
            """
        elif self.dep == "HR":
            query = """
                select * from QUERIES_LIST_HR
            """
        cur.execute(query)
        records = cur.fetchall()

        # commit changes
        conn.commit()
        cur.close()
        conn.close()

        # loop through records and add to listWidget
        for record in records:
            self.listQueries.addItem(str(record[0]))

    def connDB(self):
        """
        Arg: SQL query
        Returns: None
        connects to sqlite database,
        creates table to store queries if it doesn't exist
        """
        # Create a database or connect to one
        conn = sqlite3.connect(resource_path("./data/queriesList.db"))
        cur = conn.cursor()

        # create table to store queries
        if self.dep == "CS":
            cur.execute("create table if not exists QUERIES_LIST_CS (QUERIES text)")
        elif self.dep == "HR":
            cur.execute("create table if not exists QUERIES_LIST_HR (QUERIES text)")
        # commit changes
        conn.commit()
        cur.close()
        conn.close()

    ##################### END OF BUTTON FUNCTIONS #####################

    # SECONDARY FUNCTION
    # FUNCTION to Execute SQL QUERY and display values in a table
    def displayTable(self, query, dep):
        """
        Given a SQL query, fetches the data from the database and displays it in a table.

        Args:
            query (str): The SQL query to execute.

        Returns:
            None.
        """
        if dep == "CS":
            self.usn = "cs"
        elif dep == "HR":
            self.usn = "hr"

        # initialize the connection variable
        connection = None
        try:
            connection = cx_Oracle.connect(
                user=self.usn, password="12345", dsn="localhost:1521/WELBANK"
            )

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
                self.queryResultsTable.setColumnCount(len(cursor.description))
                self.queryResultsTable.setRowCount(len(result))
                self.queryResultsTable.setHorizontalHeaderLabels(
                    [description[0] for description in cursor.description]
                )
                for row_idx, row in enumerate(result):
                    for col_idx, value in enumerate(row):
                        # Check if the value is a datetime
                        if isinstance(value, datetime.datetime):
                            item = QTableWidgetItem(value.strftime("%d-%b-%Y").upper())
                        else:
                            item = QTableWidgetItem(str(value))
                        self.queryResultsTable.setItem(row_idx, col_idx, item)
                cursor.close()
        finally:
            if connection is not None:
                connection.close()

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


class CSqueryInterface(queryInterface):
    def __init__(self):
        super().__init__(dep="CS")


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
        querywindow = CSqueryInterface()
        querywindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
