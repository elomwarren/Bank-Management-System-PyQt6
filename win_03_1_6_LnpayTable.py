from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QDateEdit,
)
from PyQt6.QtCore import QRegularExpression, QDate
from PyQt6.QtGui import QRegularExpressionValidator

# import necessary modules from other windows
from win_03_1_1_CusTable import entityWindow

# other modules
import qdarktheme
import sys

# forgotten to add due date in the database
lnpayAttrib = [
    "LNPAY_ID",
    "LNPAY_AMT",
    "LNPAY_RMN_AMT",
    "LNPAY_DATE",
    "LN_ID",
]
intLnpayAttrib = ["LNPAY_ID", "LNPAY_AMT", "LNPAY_RMN_AMT", "LN_ID"]


class loansPayment(entityWindow):
    def __init__(self):
        super().__init__("Loans_Payment", lnpayAttrib, intLnpayAttrib)

    def newRecordDock(self):
        ### CREATION OF 'NEW RECORD' FORM WIDGETS ###

        # Loan Payment ID field
        self.lnpayIDField = QLineEdit(self)
        self.lnpayIDField.setPlaceholderText("Loan Payment ID")
        self.lnpayIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}"))
        )

        # Loan Amount field
        self.lnpayAmountIDField = QLineEdit(self)
        self.lnpayAmountIDField.setPlaceholderText("0.00")
        self.lnpayAmountIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}.[0-9]{2}"))
        )

        # Loan Amount field
        self.lnpayRmnAmountIDField = QLineEdit(self)
        self.lnpayRmnAmountIDField.setPlaceholderText("0.00")
        self.lnpayRmnAmountIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}.[0-9]{2}"))
        )

        # Loan Date field
        self.lnpayDateField = QDateEdit(self)
        self.lnpayDateField.setDisplayFormat("yyyy-MM-dd")
        self.lnpayDateField.setDate(QDate.currentDate())

        # Loan ID Field
        self.loanIDField = QLineEdit(self)
        self.loanIDField.setPlaceholderText("Loan ID")
        self.loanIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}"))
        )

        # ADD BUTTON
        self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore
        # CANCEL BUTTON
        self.cancelButton = QPushButton("Clear", clicked=lambda: self.cancel())  # type: ignore

        ### ADD WIDGETS TO NewForm LAYOUT ###
        self.NewForm.addRow("Loan Payment ID", self.lnpayIDField)
        self.NewForm.addRow("Amount", self.lnpayAmountIDField)
        self.NewForm.addRow("Balance", self.lnpayRmnAmountIDField)
        self.NewForm.addRow("Date", self.lnpayDateField)
        self.NewForm.addRow("Loan ID", self.loanIDField)
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
            self.lnpayIDField.clear()
            self.lnpayAmountIDField.clear()
            self.lnpayRmnAmountIDField.clear()
            self.lnpayDateField.setDate(QDate.currentDate())
            self.loanIDField.clear()
        else:
            pass

    # ADD BUTTON
    def add(self):
        """
        This method is called when the user clicks the "Add" button in the GUI. It retrieves the data entered by the user
        in the various fields, validates the data, and inserts a new record into the "ACCOUNTS" table in the database.
        """

        self.insertQuery = f"""
                insert into {self.entity} values (:1, :2, :3, :4, :5)
                """

        ### GRAB TEXT IN THE FIELDS AND ADD LOGIC ###
        self.lnpayID = self.lnpayIDField.text()
        self.lnpayAmount = self.lnpayAmountIDField.text()
        self.lnpayRmnAmount = self.lnpayRmnAmountIDField.text()
        self.lnpayDate = self.lnpayDateField.text()
        self.loanID = self.loanIDField.text()

        # create a list of the data entered by the user
        self.columnsData = [
            self.lnpayID,
            self.lnpayAmount,
            self.lnpayRmnAmount,
            self.lnpayDate,
            self.loanID,
        ]

        ### FIELDS VALIDATI0N LOGIC ###
        # Check emptiness field by field, exact field length and convert integer attributes to int
        # lnpayID
        if self.lnpayID == "":
            QMessageBox.warning(self, "Warning", "Please enter a Loan Payment ID.")
            return self.lnpayID
        else:
            self.lnpayID = int(self.lnpayID)
        # lnpayAmount
        if self.lnpayAmount == "":
            QMessageBox.warning(self, "Warning", "Please enter a Loan Amount.")
            return self.lnpayAmount
        else:
            self.lnpayAmount = float(self.lnpayAmount)
        # lnpayRmnAmount
        if self.lnpayRmnAmount == "":
            QMessageBox.warning(self, "Warning", "Please enter a Loan Balance.")
            return self.lnpayRmnAmount
        else:
            self.lnpayRmnAmount = float(self.lnpayRmnAmount)
        # lnpayDate

        # loanID
        if self.loanID == "":
            QMessageBox.warning(self, "Warning", "Please enter a Loan ID.")
            return self.loanID
        else:
            self.loanID = int(self.loanID)
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
        lnpaywindow = loansPayment()
        lnpaywindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
