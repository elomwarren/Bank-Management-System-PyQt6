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

jobsAttrib = [
    "JOB_ID",
    "JOB_TITLE",
    "MIN_SALARY",
    "MAX_SALARY",
    "DEP_ID",
]
intJobsAttrib = ["JOB_ID", "MIN_SALARY", "MAX_SALARY", "DEP_ID"]


class jobs(entityWindow):
    def __init__(self):
        super().__init__("Jobs", jobsAttrib, intJobsAttrib)
        # Close dock widget
        self.NewRecordDock.close()

        ### CREATION NEW RECORD FORM WIDGETS ###
        # Job ID field
        # self.jobIDField = QLineEdit()

        # Job Title field
        # self.jobTitleField = QLineEdit()

        # Miinimum Salary field
        # self.minSalaryField = QLineEdit()

        # Maximum Salary field
        # self.maxSalaryField = QLineEdit()

        # # Department ID Field
        # self.depIDField = QLineEdit()

        # ADD BUTTON
        # self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore
        ## ADD WIDGETS TO NewForm LAYOUT ###

        # self.NewForm.addRow("Job ID", self.jobIDField)
        # self.NewForm.addRow("Job Title", self.jobTitleField)
        # self.NewForm.addRow("Minimum Salary", self.minSalaryField)
        # self.NewForm.addRow("Maximum Salary", self.maxSalaryField)
        # self.NewForm.addRow("Department ID", self.depIDField)
        # self.NewForm.addRow(self.addButton)
        ### END OF ADD WIDGETS TO NewForm LAYOUT ###



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
        jobswindow = jobs()
        jobswindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
