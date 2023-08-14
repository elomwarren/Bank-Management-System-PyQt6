from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QComboBox,
    QDateEdit,
)
from PyQt6.QtCore import QRegularExpression, QDate
from PyQt6.QtGui import QRegularExpressionValidator

# import necessary modules from other windows
from win_03_1_1_CusTable import entityWindow

# other modules
import qdarktheme
import sys

accAttrib = [
    "ACC_ID",
    "ACC_NUMBER",
    "ACC_BAL",
    "ACC_TYPE",
    "ACC_START",
    "ACC_END",
    "CUS_ID",
]
intAccAttrib = ["ACC_ID", "ACC_NUMBER", "ACC_BAL", "CUS_ID"]


class accounts(entityWindow):
    def __init__(self):
        """
        Initializes the entity window.
        """
        super().__init__("Accounts", accAttrib, intAccAttrib)

    def newRecordDock(self):
        ### CREATION OF 'NEW RECORD' FORM WIDGETS ###

        # Account ID field
        self.accountIDField = QLineEdit(self)
        self.accountIDField.setPlaceholderText("Account ID")
        self.accountIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}"))
        )
        # Account Number field
        self.accountNumField = QLineEdit(self)
        self.accountNumField.setPlaceholderText("13 digits")
        self.accountNumField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{13}"))
        )
        # Account Balance field
        self.accountBalField = QLineEdit(self)
        self.accountBalField.setPlaceholderText("0.00")
        self.accountBalField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}.[0-9]{2}"))
        )
        # Account Type field
        self.accountTypeField = QComboBox(self)
        self.accountTypeField.addItems(["", "Savings", "Current", "Fixed Deposit"])
        # Account Creation Date field
        self.dateCreatField = QDateEdit(self)
        self.dateCreatField.setDisplayFormat("yyyy-MM-dd")
        self.dateCreatField.setDate(QDate.currentDate())
        # Account closure Date field
        self.dateCloseField = QDateEdit(self)
        self.dateCloseField.setDisplayFormat("yyyy-MM-dd")
        self.dateCloseField.setReadOnly(True)
        # Customer ID Field
        self.customerIDField = QLineEdit(self)
        self.customerIDField.setPlaceholderText("1 or 5 + (7 digits)")
        self.customerIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[1|5][0-9]{7}"))
        )

        # ADD BUTTON
        self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore
        # CANCEL BUTTON
        self.cancelButton = QPushButton("Clear", clicked=lambda: self.cancel())  # type: ignore

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

    ##################### BUTTON FUNCTIONS #####################

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
            self.dateCloseField.setDate(QDate(2000, 1, 1))
            self.customerIDField.clear()
        else:
            pass

    # ADD BUTTON
    def add(self):
        """
        This method is called when the user clicks the "Add" button in the GUI. It retrieves the data entered by the user
        in the various fields, validates the data, and inserts a new record into the "ACCOUNTS" table in the database.
        """

        self.insertQuery = f"""
                insert into {self.entity} values (:1, :2, :3, :4, :5, :6, :7)
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

        ############# FIELDS VALIDATI0N LOGIC #############
        # Account ID validation
        if self.accountID == "":
            QMessageBox.warning(self, "Warning", "Please enter an Account ID.")
            return self.accountID
        else:
            self.accountID = int(self.accountID)

        # Account Number validation
        if self.accountNum == "" or len(self.accountNum) != 13:
            QMessageBox.warning(
                self, "Warning", "Please enter a valid Account Number (13 digits)."
            )
            return self.accountNum
        else:
            self.accountNum = int(self.accountNum)

        # Account Balance validation
        if self.accountBal == "":
            QMessageBox.warning(self, "Warning", "Please enter an Account Balance.")
            return self.accountBal
        else:
            self.accountBal = float(self.accountBal)

        # Account Type validation
        if self.accountType == "":
            QMessageBox.warning(self, "Warning", "Please select an Account Type.")
            return self.accountType

        # Date Created validation

        # Date Closed validation

        # Customer ID validation
        if self.customerID == "" or len(str(self.customerID)) != 8:
            QMessageBox.warning(
                self,
                "Invalid Customer ID",
                "Please enter a valid customer ID (8 digits)",
            )
            return self.customerID
        else:
            self.customerID = int(self.customerID)
        # END OF FIELDS VALIDATION LOGIC

        # execute the insert query and ask to clear fields
        self.dataInsert(self.insertQuery, self.columnsData)
        self.cancel()
        ############# END OF ADD FUNCTION #############


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
        accwindow = accounts()
        accwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
