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
			date date NOT NULL,
			time text NOT NULL
		)
		""")
		self.cur.execute("""
		CREATE TABLE IF NOT EXISTS ziepju_izmantosana(
			id integer PRIMARY KEY AUTOINCREMENT,
			date date NOT NULL,
			time text NOT NULL
		)
		""")
		self.con.commit() # apstiprinam darbības

	def WriteTable(self,year:int,month:int,day:int,time,tableName):
		if tableName not in ['ziepju_izmantosana','poda_nolaisana']: return {'error':'Wrong action name provided!'}
		self.cur.execute("""
			INSERT INTO {0} (year,month,day,time) VALUES ({1},{2},{3},'{4}')
		""".format(tableName, year, month, day, time)); self.con.commit()
		return {'OK':'Record submitted succesfully!'}

	def GetTimePeriod(self,start_date, end_date):
		self.cur.execute("""
			SELECT * FROM ziepju_izmantosana
			WHERE DATE BETWEEN {0} AND {1}
		""".format(start_date, end_date))
		
		ziep_rows = self.cur.fetchall()
		self.cur.execute("""
			SELECT * FROM poda_nolaisana
			WHERE DATE BETWEEN {0} AND {1}
		""".format(start_date, end_date))
		
		pods_rows = self.cur.fetchall()
		return (ziep_rows,pods_rows)