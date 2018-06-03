import sqlite3
import asyncio
import requests as re

def fetch_issues_by_type(curs,mode, page=1, pagecount=10):
	if int(page) < 1:
		page = 1
	return curs.execute("SELECT * FROM MALENIKI WHERE DIFFICULTY LIKE '"+str(mode)+"' ORDER BY ID ASC LIMIT "+str(pagecount) + " OFFSET "+str(int(pagecount)*int(page)))

def fetch_issues(curs,page=1, pagecount=10):
	if int(page) < 1:
		page = 1
	querystring  = "SELECT * FROM MALENIKI ORDER BY ID DESC LIMIT "+str(pagecount)+ " OFFSET "+str(int(pagecount)*int(page))
	return curs.execute(querystring )

#works flawlessy
def fetch_random(curs, n):
	if n > 100:
		n = 100
	return curs.execute("SELECT * FROM MALENIKI ORDER BY RANDOM() LIMIT "+str(n))


async def periodtask(curs,conn):
	while True:
		for element in ['easy','medium','hard']:
			await asyncio.sleep(600)
			queryurl="https://api.github.com/search/issues?q=label:"+str(element)+"&sort=created&order=desc&page=1&per_page=100"
			resp = re.get(queryurl)
			a = None
			try:
				a = resp.json()['items']
			except:
				pass
			if a is not None:
				for item in a:
					val = item['title'],item['body'],element,item['id'],item['html_url']
					try:
						curs.execute('INSERT INTO `maleniki`(`TITLE`,`DESCR`,`DIFFICULTY`,`ID`,`URL`) VALUES (?,?,?,?,?);',val)
					except sqlite3.IntegrityError as e:
						print('Already got value',item['title'],item['id'])
		conn.commit()
				
