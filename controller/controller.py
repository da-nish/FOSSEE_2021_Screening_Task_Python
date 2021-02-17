class Controller(object):
    """docstring for Controller"""

    def __init__(self, model):
        super(Controller, self).__init__()
        self._model = model


        self.header = []
        self.record = []
        self.current_section = 1
        self.change_display(0)




    def change_display(self, index):
        if self.current_section == index:
            return

        self.record, self.header = self._model.getRecord(index)
        self.current_section=index
        print(index, self.header)

    def ck(self, index):
        print("pressed", index)

# record, header = model.getAngels()
# print(header)
# print(record)
