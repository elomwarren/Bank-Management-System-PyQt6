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

empAttrib = [
    "EMP_ID",
    "EMP_FN",
    "EMP_LN",
    "GENDER",
    "NATIONALITY",
    "EMP_ADDR",
    "EMP_EMAIL",
    "EMP_PHONE",
    "EMP_SALARY",
    "HIRE_DATE",
    "JOB_ID",
    "DEP_ID",
    "BRCH_ID",
]
intEmpAttrib = [
    "EMP_ID",
    "EMP_SALARY",
    "EMP_PHONE",
    "EMP_SALARY",
    "JOB_ID",
    "DEP_ID",
    "BRCH_ID",
]


class employees(entityWindow):
    def __init__(self):
        super().__init__("Employees", empAttrib, intEmpAttrib)

    ###### ENTITY SPECIFIC FUNCTIONS ######
    def newRecordDock(self):
        ###################################### NEW RECORD DOCK ######################################

        ### CREATION NEW RECORD FORM WIDGETS ###

        # Employee ID field
        self.empIDField = QLineEdit(self)
        self.empIDField.setPlaceholderText("Employee ID")
        self.empIDField.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("[1|5]{1}[1-6]{1}[0][1-7]{1}[0-9]{3}")
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
        self.nationalityField.addItems(self.nationalities)

        # Employee Address Field
        self.empAddrField = QComboBox(self, editable=True)  # type: ignore
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
        self.empAddrField.addItems(self.addresses)

        # Email Field
        self.emailField = QLineEdit(self)
        self.emailField.setPlaceholderText("example@example.com")

        # Phone Number Field
        self.phoneNumberField = QLineEdit(self)
        self.phoneNumberField.setPlaceholderText("e.g. 24XXXXXXX (9 digits)")
        self.phoneNumberField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[2|5][0-9]{8}"))
        )

        # Salary Field
        self.salaryField = QLineEdit(self)
        self.salaryField.setPlaceholderText("0.00")
        self.salaryField.setValidator(
            QRegularExpressionValidator(QRegularExpression("[0-9]{1,10}.[0-9]{2}"))
        )

        # Hire Date Field
        self.hireDateField = QDateEdit(self)
        self.hireDateField.setDisplayFormat("yyyy-MM-dd")
        self.hireDateField.setDate(QDate.currentDate())

        # Job ID Field
        self.jobIDField = QComboBox(self)
        self.depList = [
            "",
            "101",
            "102",
            "103",
            "104",
            "105",
            "106",
            "107",
            "201",
            "202",
            "203",
            "204",
            "205",
            "206",
            "207",
            "301",
            "302",
            "303",
            "304",
            "305",
            "306",
            "307",
            "401",
            "402",
            "403",
            "501",
            "502",
            "503",
            "504",
            "505",
            "506",
            "601",
            "602",
            "603",
            "604",
            "605",
            "606",
        ]
        self.jobIDField.addItems(self.depList)

        # Department ID Field
        self.depIDField = QComboBox(self)
        self.depIDField.addItems(["", "10", "20", "30", "40", "50", "60"])

        # Branch ID Field
        self.brchIDField = QComboBox(self)
        self.brchIDField.addItems(["", "1", "5"])

        # ADD BUTTON
        self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore
        # CANCEL BUTTON
        self.cancelButton = QPushButton("Clear", clicked=lambda: self.cancel())  # type: ignore

        ### ADD WIDGETS TO NewForm LAYOUT ###

        self.NewForm.addRow("Employee ID", self.empIDField)
        self.NewForm.addRow("First Name", self.firstNameField)
        self.NewForm.addRow("Last Name", self.lastNameField)
        self.NewForm.addRow("Gender", self.genderField)
        self.NewForm.addRow("Nationality", self.nationalityField)
        self.NewForm.addRow("Address", self.empAddrField)
        self.NewForm.addRow("Email", self.emailField)
        self.NewForm.addRow("Phone Number", self.phoneNumberField)
        self.NewForm.addRow("Salary", self.salaryField)
        self.NewForm.addRow("Hire Date", self.hireDateField)
        self.NewForm.addRow("Job ID", self.jobIDField)
        self.NewForm.addRow("Department ID", self.depIDField)
        self.NewForm.addRow("Branch ID", self.brchIDField)
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
            self.empIDField.clear()
            self.firstNameField.clear()
            self.lastNameField.clear()
            self.genderField.setCurrentIndex(0)
            self.nationalityField.setCurrentIndex(0)
            self.empAddrField.setCurrentIndex(0)
            self.emailField.clear()
            self.phoneNumberField.clear()
            self.salaryField.clear()
            self.hireDateField.setDate(QDate.currentDate())
            self.jobIDField.clear()
            self.depIDField.setCurrentIndex(0)
            self.brchIDField.setCurrentIndex(0)
        else:
            pass

    # ADD BUTTON
    def add(self):
        """
        This method is called when the user clicks the "Add" button in the GUI. It retrieves the data entered by the user
        in the various fields, validates the data, and inserts a new record into the "ACCOUNTS" table in the database.
        """

        self.insertQuery = f"""
                insert into {self.entity} values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)
                """

        ### GRAB TEXT IN THE FIELDS AND ADD LOGIC ###
        self.empID = self.empIDField.text()
        self.firstName = self.firstNameField.text()
        self.lastName = self.lastNameField.text()
        self.gender = self.genderField.currentText()
        self.nationality = self.nationalityField.currentText()
        self.empAddr = self.empAddrField.currentText()
        self.email = self.emailField.text()
        self.phoneNumber = self.phoneNumberField.text()
        self.salary = self.salaryField.text()
        self.hireDate = self.hireDateField.text()
        self.jobID = self.jobIDField.currentText()
        self.depID = self.depIDField.currentText()
        self.brchID = self.brchIDField.currentText()

        # create a list of the data entered by the user
        self.columnsData = [
            self.empID,
            self.firstName,
            self.lastName,
            self.gender,
            self.nationality,
            self.empAddr,
            self.email,
            self.phoneNumber,
            self.salary,
            self.hireDate,
            self.jobID,
            self.depID,
            self.brchID,
        ]

        ### FIELDS VALIDATI0N LOGIC ###
        # Check emptiness field by field, exact field length and convert integer/float attributes to int/float
        # Employee ID
        if self.empID == "" or len(str(self.empID)) != 7:
            QMessageBox.warning(self, "Warning", "Please enter an Employee ID")  # noqa
            return self.empID
        else:
            self.empID = int(self.empID)
        # First name
        if self.firstName == "":
            QMessageBox.warning(self, "Warning", "Please enter a First Name")
            return self.firstName
        # Last name
        if self.lastName == "":
            QMessageBox.warning(self, "Warning", "Please enter a last name")
            return self.lastName
        # gender
        if self.gender == "":
            QMessageBox.warning(self, "Warning", "Please choose a valid gender")
            return self.gender
        # nationality
        if self.nationality == "":
            QMessageBox.warning(self, "Warning", "Please choose a valid nationality")
            return self.nationality
        # address
        if self.empAddr == "":
            QMessageBox.warning(self, "Warning", "Please choose a valid address")
            return self.empAddr
        # email
        if (
            self.email == ""
            or "@" not in self.email
            or "." not in self.email.split("@")[1]
        ):
            QMessageBox.warning(self, "Invalid Email", "Please enter a valid email")
            return self.email
        # phone number
        if self.phoneNumber == "" or len(str(self.phoneNumber)) != 9:
            QMessageBox.warning(
                self, "Invalid Phone Number", "Please enter a valid phone number"
            )
            return self.phoneNumber
        else:
            self.phoneNumber = int(self.phoneNumber)
        # salary
        if self.salary == "" or len(str(self.salary)) < 4:
            QMessageBox.warning(
                self, "Invalid salary value", "Please enter a valid salary value"
            )
            return self.salary
        else:
            self.salary = float(self.salary)
        # Hire date
        # job ID
        if self.jobID == "":
            QMessageBox.warning(self, "Invalid value", "Please choose a valid value")
            return self.jobID
        elif self.jobID != self.empIDField.text()[1:4]:
            QMessageBox.warning(
                self,
                "Invalid job ID value",
                "Job ID should match with the 3 digits after employee ID first digit"
                + "\n"
                + "Please choose a valid value",
            )
            return self.jobID
        else:
            self.jobID = int(self.jobID)
        # department ID
        if self.depID == "":
            QMessageBox.warning(
                self, "Invalid department ID value", "Please choose a valid value"
            )
            return self.depID
        elif self.depID != self.jobIDField.currentText()[:2]:
            QMessageBox.warning(
                self,
                "Invalid department ID value",
                "Department ID should match with ID first two digits"
                + "\n"
                + "Please choose a valid value",
            )
        else:
            self.depID = int(self.depID)
        # branch ID
        if self.brchID == "":
            QMessageBox.warning(
                self, "Invalid branch ID value", "Please choose a valid value"
            )
            return self.brchID
        elif self.brchID != self.empIDField.text()[0]:
            QMessageBox.warning(
                self,
                "Invalid branch ID value",
                "Branch ID should match with employee ID first digit"
                + "\n"
                + "Please choose a valid value",
            )
            return self.brchID
        else:
            self.brchID = int(self.brchID)
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
        empwindow = employees()
        empwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
