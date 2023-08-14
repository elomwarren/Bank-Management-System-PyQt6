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

txnAttrib = [
    "TXN_ID",
    "TXN_TYPE",
    "TXN_DATE",
    "TXN_AMOUNT",
    "TXN_CHARGES",
    "ACC_ID",
    "EMP_ID",
]
intTxnAttrib = ["TXN_ID", "TXN_AMOUNT", "TXN_CHARGES", "ACC_ID", "EMP_ID"]


class transactions(entityWindow):
    def __init__(self):
        super().__init__("Transactions", txnAttrib, intTxnAttrib)

    def newRecordDock(self):
        ### CREATION OF 'NEW RECORD' FORM WIDGETS ###

        # Transaction ID field
        self.txnIDField = QLineEdit(self)
        self.txnIDField.setPlaceholderText("Transaction ID")
        self.txnIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}"))
        )
        # Transaction Type field
        self.txnTypeField = QComboBox(self)
        self.txnTypeField.addItems(["", "deposit", "withdrawal", "transfer"])
        # Transaction Date field
        self.txnDateField = QDateEdit(self)
        self.txnDateField.setDisplayFormat("yyyy-MM-dd")
        self.txnDateField.setDate(QDate.currentDate())
        # Transaction Amount field
        self.txnAmountField = QLineEdit(self)
        self.txnAmountField.setPlaceholderText("0.00")
        self.txnAmountField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}.[0-9]{2}"))
        )
        # Transaction Charges field
        self.txnChargesField = QLineEdit(self)
        self.txnChargesField.setPlaceholderText("0.00")
        self.txnChargesField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}.[0-9]{2}"))
        )
        # Account ID Field
        self.accountIDField = QLineEdit(self)
        self.accountIDField.setPlaceholderText("Account ID")
        self.accountIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}"))
        )
        # Employee ID Field
        self.employeeIDField = QComboBox(self)
        self.employeeIDField.addItems(
            ["", "1102001", "1102002", "1102003", "5102001", "5102002", "5102003"]
        )

        # ADD BUTTON
        self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore
        # CANCEL BUTTON
        self.cancelButton = QPushButton("Clear", clicked=lambda: self.cancel())  # type: ignore

        ### ADD WIDGETS TO NewForm LAYOUT ###
        self.NewForm.addRow("Transaction ID", self.txnIDField)
        self.NewForm.addRow("Transaction Type", self.txnTypeField)
        self.NewForm.addRow("Transaction Date", self.txnDateField)
        self.NewForm.addRow("Amount", self.txnAmountField)
        self.NewForm.addRow("Charges", self.txnChargesField)
        self.NewForm.addRow("Account ID", self.accountIDField)
        self.NewForm.addRow("Employee ID", self.employeeIDField)
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
            self.txnIDField.clear()
            self.txnTypeField.setCurrentIndex(0)
            self.txnDateField.setDate(QDate.currentDate())
            self.txnAmountField.clear()
            self.txnChargesField.clear()
            self.accountIDField.clear()
            self.employeeIDField.setCurrentIndex(0)
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
        self.txnID = self.txnIDField.text()
        self.txnType = self.txnTypeField.currentText()
        self.txnDate = self.txnDateField.text()
        self.txnAmount = self.txnAmountField.text()
        self.txnCharges = self.txnChargesField.text()
        self.accountID = self.accountIDField.text()
        self.employeeID = self.employeeIDField.currentText()

        # create a list of the data entered by the user
        self.columnsData = [
            self.txnID,
            self.txnType,
            self.txnDate,
            self.txnAmount,
            self.txnCharges,
            self.accountID,
            self.employeeID,
        ]

        ### FIELDS VALIDATI0N LOGIC ###
        # Check emptiness field by field, exact field length and convert integer attributes to int
        # Transaction ID
        if self.txnID == "":
            QMessageBox.warning(self, "Warning", "Please enter a Transaction ID.")
            return self.txnID
        else:
            self.txnID = int(self.txnID)
            

        # Transaction Type
        if self.txnType == "":
            QMessageBox.warning(self, "Warning", "Please enter a Transaction Type.")
            return self.txnType

        # Transaction Date

        # Transaction Amount
        if self.txnAmount == "":
            QMessageBox.warning(self, "Warning", "Please enter an Amount.")
            return self.txnAmount
        else:
            self.txnAmount = float(self.txnAmount)

        # Transaction Charges
        if self.txnCharges == "":
            QMessageBox.warning(self, "Warning", "Please enter a Charge.")
            return self.txnCharges
        else:
            self.txnCharges = float(self.txnCharges)

        # Account ID
        if self.accountID == "":
            QMessageBox.warning(self, "Warning", "Please enter an Account ID.")
            return self.accountID
        else:
            self.accountID = int(self.accountID)

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
        txnwindow = transactions()
        txnwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
