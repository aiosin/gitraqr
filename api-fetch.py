import requests as re
import sqlite3
import json
import time
#script to scrape all past issues
def main():
	#db setup
	conn = sqlite3.connect("data.db")
	curs = conn.cursor()
	labels = ["easy","medium", "hard"]

	for lbl in labels:
		for i in range(1,10):
			queryurl="https://api.github.com/search/issues?q=label:"+str(lbl)+"&sort=created&order=desc&page="+str(i)+"&per_page=100"
			r = re.get(queryurl)
			a = r.json()['items']
			for item in a:
				val = item['title'],item['body'],lbl,item['id'],item['html_url']
				try:
					curs.execute('INSERT INTO `maleniki`(`TITLE`,`DESCR`,`DIFFICULTY`,`ID`,`URL`) VALUES (?,?,?,?,?);',val)
				except sqlite3.IntegrityError as e:
					pass
			#TODO parse the response and add  content to the database
			#query string saved for later: https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc&page=200&per_page=5&state:open
			time.sleep(6.25)
	print(i)
	conn.commit()


if __name__ == '__main__':
	main()