from sanic import Sanic
from sanic.response import text, json,html
import sanic.request
from jinja2 import Environment, Template, FileSystemLoader, select_autoescape


import aioodbc

import os

#setting up app and 
app  = Sanic()
env = Environment(
	loader=FileSystemLoader('views',	),
	autoescape=select_autoescape(['html', 'xml']),
	#need python3.6 for this
	#enable_async=True
)
templates = env.list_templates()

print(templates)


@app.listener('before_server_start')
async def setup_db_connection(app,loop):
	dsn = 'Driver=SQLite3;Database=data.db'
	_conn = await aioodbc.connect(dsn=dsn, loop=loop)
	_cursor = await _conn.cursor()
	app.
	print("aylmao")
	print(_cursor)

#@app.middleware('before_server_stop')


@app.route("/")
def root (request):
	print(_conn)
	template = env.get_template("index.tpl")
	rendered_templ = template.render(variable = "aylmao",seq = range(0,20))
	return html(rendered_templ)

@app.route("/page/<pageID>")
def page(req,pageID):
	#template = Template()
	return text("reqeust for "+str(pageID)+ " came in")



if __name__ == '__main__':
	app.static("/static", "./static")
	app.run("0.0.0.0",8080,debug=True)
