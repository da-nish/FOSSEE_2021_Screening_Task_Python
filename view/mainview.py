from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import pyqtSlot
from view.ui import Ui_MainWindow


class View(QMainWindow):
    def __init__(self, model, controller):
        super(View, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._model = model
        self._controller = controller
        self.setHeader()
        self.setIDs()

        # DISPLAY SECTION
        self.ui.pushButton.clicked.connect(lambda:self._controller.change_display(self.ui.comboBox.currentIndex()))
        self.ui.pushButton.clicked.connect(self.setHeader)

        # APPEND SECTION
        self.ui.comboBox_2.currentTextChanged.connect(lambda: self._controller.change_append(self.ui.comboBox_2.currentIndex()))
        self.ui.comboBox_2.currentTextChanged.connect(self.setIDs)

        self.ui.pushButton_2.clicked.connect(lambda: self._controller.append_data(self.ui.comboBox_2.currentIndex(), self.ui.comboBox_3.currentText()))
        try:
            self._model.append.connect(self.updated)
        except Exception as e:
            print(e)

    @pyqtSlot(int)
    def updated(self):
        print(' === ')

    def setHeader(self):
        # self.ui.table.setRowCount(len(self._controller.header))

        col = len(self._controller.record[0])
        row = len(self._controller.record)

        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnCount(col)
        self.ui.tableWidget.setHorizontalHeaderLabels(self._controller.header)

        for i in range(0, row):
            for j in range(0, col):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(self._controller.record[i][j])))

        # Table will fit the screen horizontally
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def setIDs(self):
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems(self._controller.excel_IDs)