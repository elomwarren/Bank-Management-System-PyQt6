from PyQt6.QtWidgets import (
    QApplication,
)

# import necessary modules from other windows
from win_03_1_1_CusTable import entityWindow

# other modules
import qdarktheme
import sys

locAttrib = [
    "LOC_ID",
    "STREET_ADDRESS",
    "POSTCODE",
    "DIGI_ADDRESS",
    "BRCH_ID",
    "REG_ID",
]
intLocAttrib = ["LOC_ID", "BRCH_ID", "REG_ID"]


class locations(entityWindow):
    def __init__(self):
        super().__init__("Locations", locAttrib, intLocAttrib)
        # Close dock widget
        self.NewRecordDock.close()

        ### CREATION NEW RECORD FORM WIDGETS ###
        # Location ID field
        # self.locIDField = QLineEdit(self)

        # Street Address field
        # self.strAddrField = QLineEdit(self)

        # Postcode field
        # self.postcodeField = QLineEdit(self)

        # Digital Address field
        # self.digiAddrField = QLineEdit(self)

        # Branch ID Field
        # self.brchIDField = QLineEdit(self)

        # Region ID Field
        # self.regIDField = QLineEdit(self)

        # ADD BUTTON
        # self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore

        ### ADD WIDGETS TO NewForm LAYOUT ###
        # self.NewForm.addRow("Location ID", self.locIDField)
        # self.NewForm.addRow("Street Address", self.strAddrField)
        # self.NewForm.addRow("Postcode", self.postcodeField)
        # self.NewForm.addRow("Digital Address", self.digiAddrField)
        # self.NewForm.addRow("Branch ID", self.brchIDField)
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
        locwindow = locations()
        locwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
