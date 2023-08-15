from PyQt6.QtWidgets import (
    QApplication,
)

# import necessary modules from other windows
from win_03_1_1_CusTable import entityWindow

# other modules
import qdarktheme
import sys

regAttrib = ["REG_ID", "REG_NAME"]
intRegAttrib = ["REG_ID"]


class regions(entityWindow):
    def __init__(self):
        super().__init__("Regions", regAttrib, intRegAttrib)
        # Close dock widget
        self.NewRecordDock.close()

        ### CREATION NEW RECORD FORM WIDGETS ###
        # Region ID field
        # self.regIDField = QLineEdit(self)

        # Region Name field
        # self.regNameField = QLineEdit(self)

        # ADD BUTTON
        # self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore

        ### ADD WIDGETS TO NewForm LAYOUT ###
        # self.NewForm.addRow("Region ID", self.regIDField)
        # self.NewForm.addRow("Region Name", self.regNameField)
        # self.NewForm.addRow(self.addButton)

    # BACK BUTTON
    def back(self):
        from win_02_2_HRDashboard import hrDashboard

        self.cusServDashboard = hrDashboard()
        self.hide()
        self.cusServDashboard.show()


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
        regwindow = regions()
        regwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
