import request as re
import sqlite3
import json
#script to scrape all past issues
def main():
	#db setup
	conn = sqlite3.connect("data.db")
	curs = conn.cursor()
	#gotta fetch issues labeled easy, medium, and hard
	labels = ["easy,","medium", "hard"]
	for lbl in labels:
		for i in range(1,10):
			queryurl="https://api.github.com/search/issues?q=label:"+str(lbl)+"+&sort=created&order=desc&page="+str(i)+"&per_page=100"


if __name__ == '__main__':
	main()