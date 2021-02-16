import sys
from PyQt5.QtWidgets import QApplication
# from model.model import Model
# from controllers.main_ctrl import MainController
from view.mainview import View


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Connect everything together
        # self.model = Model()
        # self.ctrl = Controller(self.model)
        self.view = View()
        self.view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
