from sanic import Sanic
from sanic.response import text, json,html,redirect
import sanic.request
from jinja2 import Environment, Template, FileSystemLoader, select_autoescape
import sqlite3

import os

#setting up app and stuff
app  = Sanic()
env = Environment(
	loader=FileSystemLoader('views',	),
	autoescape=select_autoescape(['html', 'xml']),
	#need python3.6 for this
	#enable_async=True
)
templates = env.list_templates()
conn = sqlite3.connect("data.db")
curs = conn.cursor()



@app.route("/")
def root (request):
	print(conn)
	template = env.get_template("index.tpl")
	rendered_templ = template.render(variable = "aylmao",seq = range(0,20))
	return html(rendered_templ)

@app.route("/page/<pageID>")
def page(req,pageID):
	#template = Template()
	return text("reqeust for "+str(pageID)+ " came in")

@app.route("/easy/")
def easy(req):
	return req.redirect("/easy/1")

@app.route("/easy/<pageID>"):
def filtereasy(req,):
	return text("TODO")


if __name__ == '__main__':
	app.static("/static", "./static")
	app.run("0.0.0.0",8080,debug=True)
