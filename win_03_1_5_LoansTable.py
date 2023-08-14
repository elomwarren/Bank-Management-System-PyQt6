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

loansAttrib = [
    "LN_ID",
    "LN_AMT",
    "LN_DATE",
    "CUS_ID",
]
intLoansAttrib = ["LN_ID", "LN_AMT", "CUS_ID"]


class loans(entityWindow):
    def __init__(self):
        super().__init__("Loans", loansAttrib, intLoansAttrib)

    def newRecordDock(self):
        ### CREATION NEW CUSTOMER FORM WIDGETS ###

        # Loan ID field
        self.lnIDField = QLineEdit(self)
        self.lnIDField.setPlaceholderText("Loan ID")
        self.lnIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}"))
        )
        # Loan Amount field
        self.lnAmountField = QLineEdit(self)
        self.lnAmountField.setPlaceholderText("0.00")
        self.lnAmountField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}.[0-9]{2}"))
        )
        # Loan Date field
        self.lnDateField = QDateEdit(self)
        self.lnDateField.setDisplayFormat("yyyy-MM-dd")
        self.lnDateField.setDate(QDate.currentDate())
        # Customer ID Field
        self.customerIDField = QLineEdit(self)
        self.customerIDField.setPlaceholderText("1 or 5 + (7 digits)")
        self.customerIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[1|5][0-9]{7}"))
        )

        # ADD BUTTON
        self.addButton = QPushButton("Add", clicked=lambda: add())  # type: ignore
        # CANCEL BUTTON
        self.cancelButton = QPushButton("Clear", clicked=lambda: self.cancel())  # type: ignore
        ### ADD WIDGETS TO NewForm LAYOUT ###
        self.NewForm.addRow("Loan ID", self.lnIDField)
        self.NewForm.addRow("Amount", self.lnAmountField)
        self.NewForm.addRow("Date", self.lnDateField)
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
            self.lnIDField.clear()
            self.lnAmountField.clear()
            self.lnDateField.setDate(QDate.currentDate())
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
                insert into {self.entity} values (:1, :2, :3, :4))
                """

        ### GRAB TEXT IN THE FIELDS AND ADD LOGIC ###
        self.lnID = self.lnIDField.text()
        self.lnAmount = self.lnAmountField.text()
        self.lnDate = self.lnDateField.text()
        self.customerID = self.customerIDField.text()

        # create a list of the data entered by the user
        self.columnsData = [
            self.lnID,
            self.lnAmount,
            self.lnDate,
            self.customerID,
        ]

        ### FIELDS VALIDATI0N LOGIC ###
        # Check emptiness field by field, exact field length and convert integer attributes to int
        # Loan ID
        if self.lnID == "":
            QMessageBox.warning(
                self,
                "Warning",
                "Please enter a Loan ID.",
                QMessageBox.StandardButton.Ok,
            )
            return self.lnID
        else:
            self.lnID = int(self.lnID)
        # Loan Amount
        if self.lnAmount == "":
            QMessageBox.warning(
                self,
                "Warning",
                "Please enter a Loan Amount.",
                QMessageBox.StandardButton.Ok,
            )
            return self.lnAmount
        else:
            self.lnAmount = float(self.lnAmount)
        # Loan Date

        # Customer ID
        if self.customerID == "":
            QMessageBox.warning(
                self,
                "Warning",
                "Please enter a Customer ID.",
                QMessageBox.StandardButton.Ok,
            )
            return self.customerID
        else:
            self.customerID = int(self.customerID)

        # END OF FIELDS VALIDATION LOGIC

        # execute the insert query and ask to clear fields
        self.dataInsert(self.insertQuery, self.columnsData)
        self.cancel()
        # END OF ADD FUNCTION


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
        loanwindow = loans()
        loanwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
