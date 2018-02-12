import requests as re
import sqlite3
import json
#script to scrape all past issues
def main():
	#db setup
	conn = sqlite3.connect("data.db")
	curs = conn.cursor()
	retrieveddata = []
	#gotta fetch issues labeled easy, medium, and hard
	labels = ["easy,","medium", "hard"]
	#for every label fetch the newest thousand issues, hope noone complains about older issues
	#although those can be added manually if desired
	for lbl in labels:
		for i in range(1,10):
			queryurl="https://api.github.com/search/issues?q=label:"+str(lbl)+"+&sort=created&order=desc&page="+str(i)+"&per_page=100"
			r = re.get(queryurl)
			a = r.json()
			#TODO parse the response and add  content to the database
			#query string saved for later: https://api.github.com/search/issues?q=label:easy+&sort=created&order=desc&page=200&per_page=5&state:open



if __name__ == '__main__':
	main()