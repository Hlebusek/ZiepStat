import sqlite3

class DBM(): # izveidojam datubāzes menedžera klasi, kas veiks visas darbības ar datubāzēms
	def __init__(self):
		self.con = sqlite3.connect("data/ZiepStat.db") #izveidojam savienojumu ar datubāzi
		self.cur = self.con.cursor()
		self.Create_Tables()
	def Create_Tables(self):
		# izveidojam tabulas ja tās vēl neeksistē
		self.cur.execute("""
		CREATE TABLE IF NOT EXISTS pods(
			id integer PRIMARY KEY AUTOINCREMENT,
			date datetime NOT NULL
		)
		""")
		self.cur.execute("""
		CREATE TABLE IF NOT EXISTS ziepes(
			id integer PRIMARY KEY AUTOINCREMENT,
			date datetime NOT NULL
		)
		""")
		self.con.commit() # apstiprinam darbības

	def WriteTable(self,date,tableName):
		if tableName not in ['ziepes','pods']: return {'error':'Wrong action name provided!'}
		self.cur.execute("""
			INSERT INTO {0} (date) VALUES ('{1}')
		""".format(tableName,date))
		self.con.commit()
		return {'OK':'Record submitted succesfully!'}

	def GetTimePeriod(self,start_date, end_date):
		self.cur.execute("""
			SELECT * FROM ziepes
			WHERE DATE(date) BETWEEN ? AND ?
		""", (start_date, end_date))
		ziep_rows = self.cur.fetchall()

		self.cur.execute("""
			SELECT * FROM pods
			WHERE DATE(date) BETWEEN ? AND ?
		""", (start_date, end_date))
		pods_rows = self.cur.fetchall()

		return (pods_rows, ziep_rows)