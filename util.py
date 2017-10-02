import sqlite3
import requests as re 


#get top row from sqlite
#SELECT * FROM SAMPLE_TABLE ORDER BY ROWID ASC LIMIT 1
def fetch_issues_by_type(curs,mode, count=10):
	#curs.execute("SELECT * FROM maleniki WHERE IDIFFCTY LIKE '"+str(mode)+"' ORDER BY ITIME ASC LIMIT "+str(count))
	return curs.execute("SELECT * FROM MALENIKI WHERE DIFFICULTY LIKE '"+str(mode)+"' ORDER BY TIMECR ASC LIMIT "+str(count) )
#fetch_issues
#args: sqlite curs object, (optional int: count)
#returns a cursor with the newerst n issues, n is 10 by default unless set otherwise
def fetch_issues(curs, count=10):
	return curs.execute("SELECT * FROM MALENIKI ORDER BY TIMECR ASC LIMIT "+str(count))

#get_issues
#returns the oldest/newest issues from github search api
#
def get_issues():
	r = re.get("http://api.github.com/search/issues",)
	api = "https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc"
	otherAPI="https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc&page=2&per_page=10"


def main():
	conn = sqlite3.connect("data.db")
	curs = conn.cursor()
	#curs.execute("INSERT INTO MALENIKI VALUES (?,?,?,?)", ("aylmao", "AYLMAO DESCR", "easy", 123123))
	conn.commit()
	a = fetch_issues_by_type(curs, "easy")
	for i in a:
		print(i)
	a = fetch_issues(curs,count = 5)
	for i in a:
		print(i)
	
if __name__ == '__main__':
	main()