import sys
from PyQt5.QtWidgets import QApplication
from model.model import Model
from controller.controller import Controller
from view.mainview import View
from os import path


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Connect everything together
        self.model = Model()
        self.ctrl = Controller(self.model)
        self.view = View(self.ctrl)
        self.view.show()


def main():
    print("Running...")

    resource_file = ['new_sections.xlsx', 'osdag_icon.png', 'steel_sections.sqlite']
    for file in resource_file:
        if not path.exists(file):
            print('Required file not exist...')
            return

    app = App(sys.argv)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
