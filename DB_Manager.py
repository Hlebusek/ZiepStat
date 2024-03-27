import sqlite3

class DBM(): # izveidojam datubāzes menedžera klasi, kas veiks visas darbības ar datubāzēms
	def __init__(self):
		self.con = sqlite3.connect("Ziepes.db") #izveidojam savienojumu ar datubāzi
		self.cur = self.con.cursor()
		self.Create_Tables()
	def Create_Tables(self):
		# izveidojam tabulas ja tās vēl neeksistē
		self.cur.execute("""
		CREATE TABLE IF NOT EXISTS poda_nolaisana(
			id integer PRIMARY KEY AUTOINCREMENT,
			date text NOT NULL,
			time text NOT NULL
		)
		""")
		self.cur.execute("""
		CREATE TABLE IF NOT EXISTS ziepju_izmantosana(
			id integer PRIMARY KEY AUTOINCREMENT,
			date text NOT NULL,
			time text NOT NULL
		)
		""")
		self.con.commit() # apstiprinam darbības

	def WriteTable(self,date,time,tableName):
		if tableName not in ['ziepju_izmantosana','poda_nolaisana']: return {'error':'Wrong action name provided!'}
		self.cur.execute("""
			INSERT INTO {0} (date, time) VALUES ('{1}', '{2}')
		""".format(tableName, date, time)); self.con.commit()
		return {'OK':'Record submitted succesfully!'}

