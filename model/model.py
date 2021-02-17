
import sqlite3

class Model(object):
	"""docstring for Model"""
	def __init__(self):
		super(Model, self).__init__()
		self.table_name = {0: "Angles", 1: "Beams", 2: "Channels"}
	
	def getRecord(self, index):

		conn = sqlite3.connect('steel_sections.sqlite')
		cursor = conn.execute("SELECT * from "+self.table_name.get(index))
		record = []
		for row in cursor:
			record.append(list(row))
		header = list(map(lambda x: x[0], cursor.description))
		return record, header

	# def isExist(self, index, id):

	# 	conn = sqlite3.connect('steel_sections.sqlite')
	# 	cursor = conn.execute("SELECT count(id) from "+self.table_name.get(index)+" where id=?", (id,))
	# 	exist = cursor.fetchone()[0]
	# 	print(exist)
	# 	if exist == 0:
	# 		return False

	# 	# true,if exist
	# 	return True


if __name__=="__main__":
	mod = Model()
	rec,head = mod.getRecord(0)
	print(head)