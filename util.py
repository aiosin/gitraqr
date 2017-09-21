import sqlite3
import requests as re 
import json
//DB access/management is still TODO
def fetchdata(curs , query):
	curs.execute("query")

def fetchissue(curs, id):
	query= "SELECT * FROM MALENIKI WHERE IID=\'"+str(int(id))+"\'"
	curs.execute(query)

def fetchtitle(curs, title):
	query= "SELECT * FROM MALENIKI WHERE ITITLE=\'"+str(title)+"\'"
	data = curs.execute(query)


def get_issues():
	r = re.get("http://api.github.com/search/issues",)
