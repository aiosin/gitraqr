from sanic import Sanic
from sanic.response import text, json,html,redirect
import sanic.request
from jinja2 import Environment, Template, FileSystemLoader, select_autoescape
import sqlite3
import os
from util import fetch_issues, fetch_issues_by_type
# initializaton n stuff
app  = Sanic()
env = Environment(
	loader=FileSystemLoader('views',	),
	autoescape=select_autoescape(['html', 'xml']),
	#python 3.6 required for jinja 2 enable_async:
	#enable_async=True
)
templates = env.list_templates()
conn = sqlite3.connect("data.db")
curs = conn.cursor()

#file: app.py
#implements main logic for the service
#TODO: finish todos below (~30 min)

#TODO return to page/1
@app.route("/")
def root (request):
	return redirect("/page/1")


@app.route("/page/<pageID>")
def page(req,pageID):
	data = fetch_issues(curs)
	respdata = data.fetchall()
	template = env.get_template("index.tpl")
	rendered_templ = template.render(loopdata = respdata)
	return html(rendered_templ)

@app.route("/easy/")
def easy(req):
	return req.redirect("/easy/1")

@app.route("/easy/<pageID>")
def routeeasy(req):
	data = fetch_issues_by_type(curs,"easy")
	respdata = data.fetchall()
	template = env.get_template("index.tpl")
	rendered_templ = template.render(loopdata = respdata)
	return html(rendered_templ)

@app.route("/medium/<pageID>")
def medium(req):
	data = fetch_issues_by_type(curs,"medium")
	respdata = data.fetchall()
	template = env.get_template("index.tpl")
	rendered_templ = template.render(loopdata = respdata)
	return html(rendered_templ)

@app.route("/medium")
def routemedium(req):
	return req.redirect("/medium/1")

@app.route("/hard/<pageID>")
def hard(req):
	data = fetch_issues_by_type(curs,"hard")
	respdata = data.fetchall()
	template = env.get_template("index.tpl")
	rendered_templ = template.render(loopdata = respdata)
	return html(rendered_templ)

@app.route("/hard")
def routehard(req):
	return req.redirect("/hard/1")


if __name__ == '__main__':
	app.static("/static", "./static")
	app.run("0.0.0.0",8080,debug=True)
