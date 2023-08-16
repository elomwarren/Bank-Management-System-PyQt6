from PyQt6.QtWidgets import QApplication

# import the necessary modules from other windows
from win_03_2_1_empTable import employees
from win_03_2_2_jobsTable import jobs
from win_03_2_3_depTable import departments
from win_03_2_4_brchTable import branches
from win_03_2_5_locTable import locations
from win_03_2_6_regTable import regions
from win_02_1_CusServDashboard import dashboard

# other modules
import qdarktheme
import sys


class hrDashboard(dashboard):
    def __init__(self) -> None:
        super().__init__(dep="HR")

        # set window title
        self.setWindowTitle("WEL Bank - HR Dashboard")
        # modify the existing buttons and add their clicked signal
        self.button1.setText("Employees")
        self.button1.clicked.connect(lambda: self.open(employees))

        self.button2.setText("Jobs")
        self.button2.clicked.connect(lambda: self.open(jobs))

        self.button3.setText("Departments")
        self.button3.clicked.connect(lambda: self.open(departments))

        self.button4.setText("Branches")
        self.button4.clicked.connect(lambda: self.open(branches))

        self.button5.setText("Locations")
        self.button5.clicked.connect(lambda: self.open(locations))

        self.button6.setText("Regions")
        self.button6.clicked.connect(lambda: self.open(regions))


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
        hrdashwindow = hrDashboard()
        hrdashwindow.show()
        qdarktheme.setup_theme("auto")
        sys.exit(app.exec())
