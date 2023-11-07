from PyQt6.QtWidgets import QApplication

# import the necessary modules from other windows
from win_02_3_QueryInterface_CS import queryInterface

# other modules
import qdarktheme
import sys


class HRqueryInterface(queryInterface):
    def __init__(self):
        super().__init__(dep="HR")


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
        querywindow = HRqueryInterface()
        querywindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
