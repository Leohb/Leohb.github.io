# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
from RealtimeQuery import query_realtime, documentation, log, log_append
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
#app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/', methods=['POST','GET'])
def index():
	if request.method == 'POST':
		r = request.form['InputCity']
		if r:
			s = query_realtime(r)
			return render_template('index.html', result=s)
		else:
			return render_template('index.html')

	else:
		if request.args.get('help') == u'帮助':
	#		s = documentation("README.md").splitlines()
			s = ['This is documentation','help docu']
			return render_template('index.html', result = s)
		elif request.args.get('history') == u'历史':
			s = documentation("log.txt").splitlines()
			return render_template('index.html', result = s)
		else:
			return render_template('index.html')



if __name__ == '__main__':
	log()
#	app.run(debug = True, host='120.77.203.72', port=22)
	app.run(debug=True)
