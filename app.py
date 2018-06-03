import os
import sqlite3
import ssl

import sanic.request
from jinja2 import Environment, FileSystemLoader, Template, select_autoescape
from sanic import Sanic
from sanic.response import html, json, redirect, text

from util import *

context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain("/etc/letsencrypt/live/gitraqr.online/fullchain.pem", keyfile="/etc/letsencrypt/live/gitraqr.online/privkey.pem")


app  = Sanic(__name__)
env = Environment(
	loader=FileSystemLoader('views',	),
	autoescape=select_autoescape(['html', 'xml']),
	#enable_async=True #lol this breaks lots of shit
)
templates = env.list_templates()
conn = sqlite3.connect("data.db")
curs = conn.cursor()

app.add_task(periodtask(curs,conn))


@app.route("/")
async def root (request):
	return redirect("/page/1")


@app.route("/page/<pageID>")
async def page(req,pageID):
	pageID = int(pageID)
	if pageID < 1:
		return redirect("/page/1")
	data = fetch_issues(curs,page=pageID)
	respdata = data.fetchall()
	template = env.get_template("index.tpl")
	rendered_templ = template.render(loopdata = respdata,page=pageID)
	return html(rendered_templ)

@app.route("/easy/")
async def easy(req):
	return redirect("/easy/1")

@app.route("/easy/<pageID>")
async def routeeasy(req,pageID):
	pageID = int(pageID)
	if pageID < 1:
		return redirect("/page/1")
	data = fetch_issues_by_type(curs,"easy",page=pageID)
	respdata = data.fetchall()
	template = env.get_template("easy.tpl")
	rendered_templ = template.render(loopdata = respdata,page=pageID)
	return html(rendered_templ)

@app.route("/medium/<pageID>")
async def medium(req,pageID):
	pageID = int(pageID)
	if pageID < 1:
		return redirect("/page/1")
	data = fetch_issues_by_type(curs,"medium",page=pageID)
	respdata = data.fetchall()
	template = env.get_template("medium.tpl")
	rendered_templ = template.render(loopdata = respdata,page=pageID)
	return html(rendered_templ)

@app.route("/medium")
async def routemedium(req):
	return redirect("/medium/1")

@app.route("/hard/<pageID>")
async def hard(req,pageID):
	pageID = int(pageID)
	if pageID < 1:
		return redirect("/page/1")
	data = fetch_issues_by_type(curs,"hard",page=pageID)
	respdata = data.fetchall()
	template = env.get_template("hard.tpl")
	rendered_templ = template.render(loopdata = respdata,page=pageID)
	return html(rendered_templ)

@app.route("/hard")
async def routehard(req):
	return redirect("/hard/1")


@app.route("/update")
async def updateval(req):
	return html("<body> nutting yet bois</body>")

@app.route("/random")
async def route_random(req):
	data = fetch_random(curs,10)
	respdata = data.fetchall()
	template = env.get_template("random.tpl")
	rendered_templ = template.render(loopdata = respdata)
	return html(rendered_templ)


if __name__ == '__main__':
	app.static("/static", "./static")
	app.run("0.0.0.0",443,debug=False,ssl=context)
