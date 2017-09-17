import asyncio
import pyodbc


loop = asyncio.get_event_loop()
dsn ="Driver={sqlite};database=data.db"
conn = pyodbc.connect(dsn)
cur = conn.cursor()


async def db_fetch(cur):
	cur.execute("SELECT * FROM MALENIKI")
	cur.fetchall()
	return None
	
	
tasks =[]
for i in range(0,10):
	task = asyncio.ensure_future(db_fetch(cur))
	tasks += task

loop.run_until_complete(asyncio.ensure_future(tasks))

