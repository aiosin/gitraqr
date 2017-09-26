import request as re
import sqlite3
import json
#script to scrape all past issues
def main():
	conn = sqlite3.connect("data.db")
	curs = conn.cursor()
	page = 0
	#while there are issues, put them into the db (run every minute in prod)
	while True:
		queryurl="https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc&page=200&per_page="+str(page)
		resp = re.get(queryurl)
		respdata = resp.json()
		parsed = json.loads(str(respdata))
		


if __name__ == '__main__':
	main()