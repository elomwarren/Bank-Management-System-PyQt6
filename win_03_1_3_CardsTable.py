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

cardsAttrib = [
    "CARD_ID",
    "CARD_NUMBER",
    "CARD_TYPE",
    "CARD_LIMIT",
    "CARD_START",
    "CARD_EXPIRY",
    "CARD_STATUS",
    "ACC_ID",
]
intCardsAttrib = ["CARD_ID", "CARD_NUMBER", "CARD_LIMIT", "ACC_ID"]


class cards(entityWindow):
    def __init__(self):
        super().__init__("Cards", cardsAttrib, intCardsAttrib)

    def newRecordDock(self):
        ### CREATION OF 'NEW RECORD' FORM WIDGETS ###

        # Card ID field
        self.cardIDField = QLineEdit(self)
        self.cardIDField.setPlaceholderText("Card ID")
        self.cardIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}"))
        )
        # Card Number field
        self.cardNumField = QLineEdit(self)
        self.cardNumField.setPlaceholderText("Card Number")
        self.cardNumField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{16}"))
        )
        # Card Type field
        self.cardTypeField = QComboBox(self)
        self.cardTypeField.addItems(["", "Debit", "Credit"])
        # Card Limit field
        self.cardLimitField = QComboBox(self)
        self.cardLimitField.addItems(["", "1500", "2000", "2500", "5000"])
        # Card Creation Date field
        self.dateCreatField = QDateEdit(self)
        self.dateCreatField.setDisplayFormat("yyyy-MM-dd")
        self.dateCreatField.setDate(QDate.currentDate())
        # Card expiry Date field
        self.dateExpiryField = QDateEdit(self)
        self.dateExpiryField.setDisplayFormat("yyyy-MM-dd")
        self.dateExpiryField.setReadOnly(True)
        # Card Status Field
        self.cardStatusField = QComboBox(self)
        self.cardStatusField.addItems(["", "Active", "Inactive", "Blocked", "Expired"])
        # Account ID Field
        self.accountIDField = QLineEdit(self)
        self.accountIDField.setPlaceholderText("Account ID")
        self.accountIDField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}"))
        )

        # ADD BUTTON
        self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore
        # CANCEL BUTTON
        self.cancelButton = QPushButton("Clear", clicked=lambda: self.cancel())  # type: ignore

        ### ADD WIDGETS TO NewForm LAYOUT ###
        self.NewForm.addRow("Card ID", self.cardIDField)
        self.NewForm.addRow("Card Number", self.cardNumField)
        self.NewForm.addRow("Card Type", self.cardTypeField)
        self.NewForm.addRow("Card Limit", self.cardLimitField)
        self.NewForm.addRow("Creation Date", self.dateCreatField)
        self.NewForm.addRow("Expiry", self.dateExpiryField)
        self.NewForm.addRow("Card Status", self.cardStatusField)
        self.NewForm.addRow("Account ID", self.accountIDField)
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
            self.cardIDField.clear()
            self.cardNumField.clear()
            self.cardTypeField.setCurrentIndex(0)
            self.cardLimitField.setCurrentIndex(0)
            self.dateCreatField.setDate(QDate.currentDate())
            self.dateExpiryField.setDate(QDate.currentDate())
            self.cardStatusField.setCurrentIndex(0)
            self.accountIDField.clear()
        else:
            pass

    # ADD BUTTON
    def add(self):
        """
        This method is called when the user clicks the "Add" button in the GUI. It retrieves the data entered by the user
        in the various fields, validates the data, and inserts a new record into the "ACCOUNTS" table in the database.
        """

        self.insertQuery = f"""
                insert into {self.entity} values (:1, :2, :3, :4, :5, :6, :7, :8)
                """

        ### GRAB TEXT IN THE FIELDS AND ADD LOGIC ###
        self.cardID = self.cardIDField.text()
        self.cardNum = self.cardNumField.text()
        self.cardType = self.cardTypeField.currentText()
        self.cardLimit = self.cardLimitField.currentText()
        self.dateCreat = self.dateCreatField.text()
        self.dateExpiry = self.dateExpiryField.text()
        self.cardStatus = self.cardStatusField.currentText()
        self.accountID = self.accountIDField.text()

        # create a list of the data entered by the user
        self.columnsData = [
            self.cardID,
            self.cardNum,
            self.cardType,
            self.cardLimit,
            self.dateCreat,
            self.dateExpiry,
            self.cardStatus,
            self.accountID,
        ]

        ### FIELDS VALIDATI0N LOGIC ###
        # Check emptiness field by field, exact field length and convert integer attributes to int
        # Card ID
        if self.cardID == "":
            QMessageBox.warning(self, "Warning", "Please enter a Card ID")
            return self.cardID
        else:
            self.cardID = int(self.cardID)

        # Card Number
        if self.cardNum == "" or len(self.cardNum) != 16:
            QMessageBox.warning(self, "Warning", "Please enter a valid Card Number")
            return self.cardNum
        else:
            self.cardNum = int(self.cardNum)

        # Card Type
        if self.cardType == "":
            QMessageBox.warning(self, "Warning", "Please enter a Card Type")
            return self.cardType

        # Card Limit
        if self.cardLimit == "":
            QMessageBox.warning(self, "Warning", "Please enter a Card Limit")
            return self.cardLimit
        else:
            self.cardLimit = float(self.cardLimit)
        # Creation Date

        # Card expiry date
        # set expiry date to 2 years after creation date
        self.dateExpiry = self.dateCreatField.date().addYears(2)

        # Card Status
        if self.cardStatus == "":
            QMessageBox.warning(self, "Warning", "Please enter a Card Status")
            return self.cardStatus

        # Account ID
        if self.accountID == "":
            QMessageBox.warning(self, "Warning", "Please enter an Account ID")
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
        cardswindow = cards()
        cardswindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
