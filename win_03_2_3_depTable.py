from PyQt6.QtWidgets import (
    QApplication,
)

# import necessary modules from other windows
from win_03_1_1_CusTable import entityWindow

# other modules
import qdarktheme
import sys

depAttrib = ["DEP_ID", "DEP_NAME"]
depAttribInt = ["DEP_ID"]


class departments(entityWindow):
    def __init__(self):
        super().__init__("Departments", depAttrib, depAttribInt)
        # Close dock widget
        self.NewRecordDock.close()

        ### CREATION NEW RECORD FORM WIDGETS ###
        # Department ID field
        # self.depIDField = QLineEdit()
        # Department Name field
        # self.depNameField = QLineEdit()

        # ADD BUTTON
        # self.addButton = QPushButton("Add", clicked=lambda: self.add())  # type: ignore
        ### ADD WIDGETS TO NewForm LAYOUT ###
        # self.NewForm.addRow("Department ID", self.depIDField)
        # self.NewForm.addRow("Department Name", self.depNameField)
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
        depwindow = departments()
        depwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
