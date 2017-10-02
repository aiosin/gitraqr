import sqlite3
import requests as re 
import json

#file: util.py
#helper funcitons for app.py
#TODO: implement page browsing functionality
#

#get top row from sqlite
#SELECT * FROM SAMPLE_TABLE ORDER BY ROWID ASC LIMIT 1
def fetch_issues_by_type(curs,mode, page=1, pagecount=10):
	#curs.execute("SELECT * FROM maleniki WHERE IDIFFCTY LIKE '"+str(mode)+"' ORDER BY ITIME ASC LIMIT "+str(count))
	return curs.execute("SELECT * FROM MALENIKI WHERE DIFFICULTY LIKE '"+str(mode)+"' ORDER BY TIMECR ASC LIMIT "+str(pagecount) )
#fetch_issues
#args: sqlite curs object, (optional int: pagecount, int: page)
#returns a cursor with the newerst n issues, n is 10 by default unless set otherwise
def fetch_issues(curs,page=1, pagecount=10):
	return curs.execute("SELECT * FROM MALENIKI ORDER BY TIMECR ASC LIMIT "+str(pagecount))

#get_issues
#returns the oldest/newest issues from github search api
#
def get_issues():
	r = re.get("http://api.github.com/search/issues",)
	api = "https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc"
	otherAPI="https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc&page=2&per_page=10"

def fetch_n_random(curs,count=10):
	#TODO: implement random values from sqlite db
	pass

#main method for internal testing purposes only
def main():
	conn = sqlite3.connect("data.db")
	curs = conn.cursor()
	#curs.execute("INSERT INTO MALENIKI VALUES (?,?,?,?, ?)", ("aylmao", "AYLMAO DESCR", "easy", 123123, "http://example.com"))
	#conn.commit()
	with open("github-data.json", "r") as f:
		rawstring = f.read()
		jsonobject = json.loads(rawstring)
		print(jsonobject)
		print("\n\n\n\n\n")
		print(json.dumps(jsonobject.get("items"),sort_keys=True, indent=4))
		print(len(jsonobject.get("items")))

	
if __name__ == '__main__':
	main()