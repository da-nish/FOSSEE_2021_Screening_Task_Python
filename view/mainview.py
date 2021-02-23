from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from view.ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class View(QMainWindow):
    def __init__(self, controller):
        super(View, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._controller = controller
        self.setTable()
        self.setIDs()

        # DISPLAY SECTION
        self.ui.pushButton.clicked.connect(lambda:self._controller.change_display(self.ui.comboBox.currentIndex()))
        self.ui.pushButton.clicked.connect(self.setTable)


        # APPEND SECTION
        self.ui.comboBox_2.currentTextChanged.connect(lambda: self._controller.change_append(self.ui.comboBox_2.currentIndex()))
        self.ui.comboBox_2.currentTextChanged.connect(self.setIDs)

        self.ui.pushButton_2.clicked.connect(lambda: self._controller.append_data(self.ui.comboBox_2.currentIndex(), self.ui.comboBox_3.currentText()))
        self._controller.update_signal.connect(self.update)

        self.set_status_bar()


    # On success append: display appended section
    @pyqtSlot(int)
    def update(self, index):

        self.ui.comboBox.setCurrentIndex(index)  # set appended section in display dropdown
        self.setTable(True)  # updating table, update=True to know update call
        self.set_status_bar("New Record added in "+ self.ui.comboBox_2.currentText())  # updating status bar


    def setTable(self, update=False):

        col = len(self._controller.record[0])  # No. of columns
        row = len(self._controller.record)  # No. of rows


        self.ui.tableWidget.setRowCount(row)  # setting row
        self.ui.tableWidget.setColumnCount(col)  # setting columns
        self.ui.tableWidget.setHorizontalHeaderLabels(self._controller.header)  # setting table header

        # setting table values
        for i in range(0, row):
            for j in range(0, col):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(self._controller.record[i][j])))

        self.ui.tableWidget.selectRow(0)  # grey background

        # auto select new added row
        if update:
            self.ui.tableWidget.selectRow(row-1)  # grey background
            # self.ui.tableWidget.setFocus(0)  # dark blue background
        else:
            self.set_status_bar("Displaying "+self.ui.comboBox.currentText())  # updating status bar



        # Table will fit the screen horizontally
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



    # setting ids in dropdown of append section(current selected)
    # displaying excel id column in dropdown
    def setIDs(self):
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems(self._controller.excel_IDs)

    def set_status_bar(self, msg="Welcome"):
        self.ui.statusbar.showMessage(msg)