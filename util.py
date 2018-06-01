import sqlite3
import requests as re 
import json


def fetch_issues_by_type(curs,mode, page=1, pagecount=10):
	return curs.execute("SELECT * FROM MALENIKI WHERE DIFFICULTY LIKE '"+str(mode)+"' ORDER BY ID ASC LIMIT "+str(pagecount) )

def fetch_issues(curs,page=1, pagecount=10):
	return curs.execute("SELECT * FROM MALENIKI ORDER BY ID ASC LIMIT "+str(pagecount))

def get_issues():
	r = re.get("http://api.github.com/search/issues",)
	api = "https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc"
	otherAPI="https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc&page=2&per_page=10"

