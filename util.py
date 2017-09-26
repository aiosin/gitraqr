import sqlite3
import requests as re 
#DB access/management is still TODO
def fetchdata(curs , query):
	curs.execute("query")

#get top row from sqlite
#SELECT * FROM SAMPLE_TABLE ORDER BY ROWID ASC LIMIT 1
def fetch_issues_by_type(curs,mode, count=10):
	#curs.execute("SELECT * FROM maleniki WHERE IDIFFCTY LIKE '"+str(mode)+"' ORDER BY ITIME ASC LIMIT "+str(count))
	return curs.execute("SELECT * FROM MALENIKI WHERE DIFFICULTY LIKE '"+str(mode)+"' ORDER BY TIMECR ASC LIMIT "+str(count) )


def get_issues():
	r = re.get("http://api.github.com/search/issues",)
	api = "https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc"
	otherAPI="https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc&page=2&per_page=10"


def main():
	conn = sqlite3.connect("data.db")
	curs = conn.cursor()
	curs.execute("INSERT INTO MALENIKI VALUES (?,?,?,?)", ("aylmao", "AYLMAO DESCR", "easy", 123123))
	conn.commit()
	a = fetch_issues_by_type(curs, "easy")
	for i in a:
		print(i)
	
if __name__ == '__main__':
	main()