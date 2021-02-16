from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from view.ui import Ui_MainWindow


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
