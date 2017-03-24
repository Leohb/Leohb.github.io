from flask import Flask,request, render_template,g
from RealtimeQuery import query_realtime, documentation, log, log_append
import sqlite3
import datetime
app = Flask(__name__)

DATABASE = './database.db'
UPDATE_DIC = ["晴","雪","雨","阴"]
PAGE = 'index_v1.html'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def query_from_db(city):
	'''通过城市名称，从数据库查询天气'''
	r = query_db('select * from qw where city_name = ?',
	                [city], one=True)
	if r is None:
	    print('No such city')
	else:
	    print(r)
	return r

def insert_into_db(city, weather, temperature):
	'''将查询的结果插入到数据库中'''
	c = get_db().cursor()
	qttime = datetime.date.today()
	city_name = city
	c.execute("INSERT INTO qw VALUES (?,?,?,?)",(qttime,city_name,weather,temperature))
	get_db().commit()

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.form['InputCity']
		print(r)
		if r:
			if request.form['query'] == '查询':
				t = query_realtime(r)
				return render_template(PAGE, result = t)
			elif request.args.get('update') == '更正':
				# c = get_db().cursor()
				# d = r.split(" ")
				# q = query_from_db(d[0])

				# if q and (d[1] in UPDATE_DIC):
				# 	c.execute("UPDATE qw SET weather= ? WHERE city_name = ?" , (str(d[1]),str(d[0])))
				# 	get_db().commit()
				# 	s = q

				# else:
				# 	s = ["请输入正确的天气情况：如晴，雪，雨，阴"]
				s = "请输入更正信息"
				return render_template(PGAE, result = s)	
			else:
				return render_template(PAGE)		

		else:
			return render_template(PAGE)

	else:
		if request.args.get('help') == '帮助':
			s = documentation("README.md").splitlines()
			return render_template(PAGE, result = s)
		elif request.args.get('history') == '历史':
			s = documentation("log.txt").splitlines()
			return render_template(PAGE, result = s)
		else:
			return render_template(PAGE)

if __name__ == '__main__':
	log()
	with app.app_context():
		app.run(debug=True)