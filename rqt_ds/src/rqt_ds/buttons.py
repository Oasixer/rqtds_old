import breeze_resources
import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import QFile
from PyQt5.QtCore import QTextStream
from dsmw import Ui_MainWindow
from fbs_runtime.application_context import ApplicationContext


class my_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.robot_enabled = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_buttons()
        self.set_element_styles()

    def setup_buttons(self):
        self.ui.enableButton.clicked.connect(self.enable_robot)
        self.ui.disableButton.clicked.connect(self.disable_robot)
        #self.ui.disableButton.setEnabled(False)
        self.set_element_styles()

    def disable_robot(self):
        self.robot_enabled = False
        print(self.robot_enabled)
        #self.enableButton.toggle()
        self.ui.enableButton.setEnabled(True)
        self.ui.enableButton.setStyleSheet("color: rgb(0,170,0); background-color: rgb(180, 180, 180)")
        self.ui.disableButton.setEnabled(False)
        self.ui.disableButton.setStyleSheet("color: rgb(85,0,0); background-color: rgb(70, 70, 70)")
        #self.ui.enableButton.toggle()
        #self.ui.disableButton.toggle()
        #self.refresh_toggle_buttons()

    def enable_robot(self):
        self.robot_enabled = True
        print(self.robot_enabled)
        self.ui.enableButton.setEnabled(False)
        self.ui.enableButton.setStyleSheet("color: rgb(0,85,0); background-color: rgb(70, 70, 70)")
        self.ui.disableButton.setEnabled(True)
        self.ui.disableButton.setStyleSheet("color: rgb(255,0,0);background-color: rgb(180, 180, 180)")
        #self.ui.enableButton.toggle()
        #self.refresh_toggle_buttons()

    '''def refresh_toggle_buttons(self):
        if self.robot_enabled:
            #self.ui.enableButton.setEnabled(False)
            #self.ui.disableButton.setEnabled(True)
        else:
            #self.ui.enableButton.setEnabled(True)
            #self.ui.disableButton.setEnabled(False)'''

    def set_element_styles(self):
        self.ui.disableButton.setChecked(True)
        self.disable_robot()
        self.ui.robotCommsBox.setStyleSheet("background-color: green")
        self.ui.robotModesWidget.setStyleSheet("background-color: rgb(30,30,30)")


class AppContext(ApplicationContext):  # 1. Subclass ApplicationContext
    def run(self):  # 2. Implement run()
        window = my_window()
        window.show()
        file = QFile(":/dark.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.app.setStyleSheet(stream.readAll())
        return self.app.exec_()  # 3. End run() with this line


if __name__ == '__main__':
    appctxt = AppContext()  # 4. Instantiate the subclass
    exit_code = appctxt.run()  # 5. Invoke run()
    sys.exit(exit_code)
