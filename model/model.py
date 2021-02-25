from PyQt5.QtCore import QObject, pyqtSignal
import sqlite3


class Model(QObject):
    """docstring for Model"""

    def __init__(self):
        super(Model, self).__init__()
        self.table = {0: {'name': "Angles", 'max-col': 24},
                      1: {'name': 'Beams', 'max-col': 20},
                      2: {'name': 'Channels', 'max-col': 21}
                      }

    def getRecord(self, index):
        conn = sqlite3.connect('steel_sections.sqlite')
        cursor = conn.execute("SELECT * from " + self.table.get(index).get('name'))
        record = []
        for row in cursor:
            record.append(list(row))
        header = list(map(lambda x: x[0], cursor.description))
        conn.close()
        return record, header

    def is_exist(self, index, designation):

        conn = sqlite3.connect('steel_sections.sqlite')
        cursor = conn.execute("SELECT designation from " + self.table.get(index).get('name'))

        for row in cursor:
            if designation.value == row[0]:
                conn.close()
                return True  # exist

        conn.close()
        return False  # not exist


    def append_record(self, index, record):

        insert_query = {
            0: "INSERT INTO Angles('Designation', 'Mass','Area', 'AXB', 't', 'R1', 'R2', 'Cz', 'Cy', 'Tan?', 'Iz', 'Iy', 'Iu(max)', 'Iv(min)', 'rz', 'ry', 'ru(max)', 'rv(min)', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source') VALUES( ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?)",
            1: "INSERT INTO Beams('Designation', 'Mass', 'Area', 'D', 'B', 'tw', 'T', 'FlangeSlope', 'R1', 'R2', 'Iz', 'Iy', 'rz','ry', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source') VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?)",
            2: "INSERT INTO Channels('Designation', 'Mass', 'Area', 'D', 'B', 'tw', 'T', 'FlangeSlope', 'R1', 'R2', 'Cy', 'Iz', 'Iy', 'rz', 'ry', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source') VALUES( ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?)"
        }
        record = record[0:self.table.get(index).get('max-col') - 1]  # -1, excluding id

        try:
            conn = sqlite3.connect('steel_sections.sqlite')
            cur = conn.cursor()

            cur.execute(insert_query.get(index), record)
            conn.commit()
            return True

        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    mod = Model()
    rec, head = mod.getRecord(0)
    print(head)
