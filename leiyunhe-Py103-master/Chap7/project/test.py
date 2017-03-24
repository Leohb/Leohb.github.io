# -*- coding:utf-8 -*-
import time
from flask import Flask,request,make_response
import hashlib
import xml.etree.ElementTree as ET
import requests, json
from requestweather import fetchWeather

app = Flask(__name__)
app.debug=True
historyList = []

@app.route('/',methods=['GET','POST'])
def wechat():
	if request.method =='GET':
		data = request.args

		token = 'hellocraney'
		signature = data.get('signature','')
		timestamp = data.get('timestamp','')
		nonce = data.get('nonce','')
		echostr = data.get('echostr','')
		
		l = [timestamp,nonce,token]
		l.sort()
		s = ''.join(l)
#		s = s.encode('utf-8')
		if (hashlib.sha1(s).hexdigest()==signature):
			return make_response(echostr)
	else:

		xml_recv = ET.fromstring(request.stream.read())
	
		ToUserName = xml_recv.find("ToUserName").text
		FromUserName = xml_recv.find("FromUserName").text
		Content = xml_recv.find("Content").text

		xml_rep = '''<xml>
				    <ToUserName><![CDATA[%s]]></ToUserName>
	    			<FromUserName><![CDATA[%s]]></FromUserName>
	    			<CreateTime>%s</CreateTime>
	        		<MsgType><![CDATA[text]]></MsgType>
	        		<Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag>
    				</xml>'''

		#if Content.strip() == 'help':
		if Content.strip() == u'帮助':
			response = make_response(xml_rep % (FromUserName, ToUserName, str(int(time.time())), help()))
		#	response.Content_type='application/xml'
			return response

		elif Content.strip() == u'历史':
			response = make_response(xml_rep % (FromUserName, ToUserName, str(int(time.time())), history()))	#		response.Content_type='application/xml' 
			return response
		else:

			response = make_response(xml_rep % (FromUserName, ToUserName, str(int(time.time())), weather(Content)))
		#	print(response)
			response.Content_type='application/xml'
		#	print(response.Content_type)
			return response
		#	print(response)


def weather(content):
	try:
		r = fetchWeather(content)
		result = json.loads(r)
		temperature = result["results"][0]['now']['temperature']
		weather = result["results"][0]['now']['text']
	#	get_weather = [city,  weather , temperature + " C"]

	#	text ="{} {} {}".format(content,weather,temperature)
		text = content + '*' + weather + '*' + temperature + u'摄氏度' + '\n'
		historyList.append(text)
	except Exception as e:
		helpText = help()
		text = '搜索不到，请重新输入' + helpText
	return text

def help():
	help = '''输入城市名称查询天气；\n输入[帮助]获取帮助文档；\n输入[历史]查询历史记录'''
	return help

def history():
	text = ''.join(historyList)
	return '查询历史\n' + text

if __name__=="__main__":


	app.run(debug=True,host='0.0.0.0',port=80)
