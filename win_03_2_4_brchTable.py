from PyQt6.QtWidgets import (
    QApplication,
)

# import necessary modules from other windows
from win_03_1_1_CusTable import entityWindow

# other modules
import qdarktheme
import sys

brchAttrib = ["BRCH_ID", "BRCH_NAME", "PHONE_NUMBER", "ASSETS", "REG_ID"]
intBrchAttrib = ["BRCH_ID", "PHONE_NUMBER", "ASSETS", "REG_ID"]


class branches(entityWindow):
    def __init__(self):
        super().__init__("Branches", brchAttrib, intBrchAttrib)
        # Close dock widget
        self.NewRecordDock.close()

        ### CREATION NEW RECORD FORM WIDGETS ###
        # Branches ID field
        # self.brchIDField = QLineEdit(self)

        # Branch Name field
        # self.brchNameField = QLineEdit(self)

        # Phone number field
        # self.phoneNumField = QLineEdit(self)

        # Branch Assets field
        # self.brchAssetsField = QLineEdit(self)

        # Region ID Field
        # self.regIDField = QLineEdit(self)

        # ADD BUTTON
        # self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore

        ### ADD WIDGETS TO NewForm LAYOUT ###
        # self.NewForm.addRow("Branch ID", self.brchIDField)
        # self.NewForm.addRow("Branch Name", self.brchNameField)
        # self.NewForm.addRow("Phone Number", self.phoneNumField)
        # self.NewForm.addRow("Assets", self.brchAssetsField)
        # self.NewForm.addRow("Region ID", self.regIDField)
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
        brchwindow = branches()
        brchwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
