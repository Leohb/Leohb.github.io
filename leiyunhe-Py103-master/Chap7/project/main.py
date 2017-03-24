# -*- coding=utf:-8 -*-
import time
from flask import Flask,request,make_response
import hashlib
import xml.etree.ElementTree as ET
import requests, json
from requestweather import fetchWeather

app = Flask(__name__)
app.debug=True

@app.route('/',methods=['GET','POST'])
def wechat():
	if request.method =='GET':
		data = request.args

		token = 'hellocraney'
		signature = data.get('signature','')
		timestamp = data.get('timestamp','')
		nonce = data.get('nonce','')
		echostr = data.get('echostr','')
		
		list = [timestamp,nonce,token]
		list.sort()
		s = ''.join(list)
		s = s.encode('utf-8')
		if (hashlib.sha1(s).hexdigest()==signature):
			return make_response(echostr)
	else:
		xml_recv = ET.fromstring(request.data)
		if isinstance(xml_recv
		ToUserName = xml_recv.find("ToUserName").text
		FromUserName = xml_recv.find("FromUserName").text
		Content = xml_recv.find(Content).text

		xml_rep = "<xml>\
					<ToUserName><![CDATA[%S]]></ToUserName>\
					<FromUserName><![CDATA[%S]]></FromUserName>\
					<GreatTime>%s<!CreateTime>\
					<MsgType><![CDATA[text]]></MsgType>\
					<Content><![CDATA[%S]]></Conten>\
					<FuncFlag>0</FuncFlag>\
					</xml>"

		if Content.strip() == 'help':
			response = make_response(xml_rep % (FromUserName,ToUserName,str(int(time.time())),help()))
			response.Content_type='application/xml'
			return response
		elif Content.strip() == 'history':
			response = make_response(xml_rep % (FromUserName,ToUserName,str(int(time.time())),history()))
			response.Content_type='application/xml'
			return response
		else:
			response = make_response(xml_rep % (FromUserName,ToUserName,str(int(time.time())),weather(Context)))
			response.Content_type='application/xml'
			return response

def weather(content):
	try:
		r = fetchWeather(content)
		result = json.loads(r)
		temperature = result["results"][0]['now']['temperature']
		weather = result["results"][0]['now']['text']
		get_weather = [city,  weather , temperature + " C"]

		text ="{} {} {}".format(content,weather,temperature)
		historyList.append(text)
	except Exception as e:
		helpText=help()
		text = '搜索不到，请重新输入'+helpText
	return text

def help():
	help = '输入城市名称查询天气信息；\n'\
			'输入[help]；\n'
	return help

def history():
	text = ''.join(historyList)
	return text

if __name__=="__main__":
	historyList=[]
	app.run(debug=True,host='0.0.0.0',port=80)
