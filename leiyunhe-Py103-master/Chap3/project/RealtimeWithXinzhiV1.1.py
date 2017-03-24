import requests, json

def query_realtime():
	'''query realtime weather'''
	r = requests.get(url)
	result = json.loads(r.text)
	city = result["results"][0]['location']['name']
	realtime = result["results"][0]['last_update']
	temperature = result["results"][0]['now']['temperature']
	weather = result["results"][0]['now']['text']

	return city + realtime + "天气情况为：" + weather + "," + "温度："+ temperature + "摄氏度"


with open("log.txt", "w", encoding = "utf-8") as f:
	f.write("您的查询记录如下：\n")


while True:

	user_input = input("请输入城市或指令：")

	if user_input in {"quit", "exit"}:
		break
	elif user_input == "history":
		with open("log.txt", "r", encoding = "utf-8") as f:
			print(f.read())
	elif user_input == "help":
		with open("README.md", "r", encoding = "utf-8") as f:
			print(f.read())
	else:
		url = "https://api.thinkpage.cn/v3/weather/now.json?key=kdtkmkoewxfhmqbx&location=" + user_input + "&language=zh-Hans&unit=c"
		get_weather = query_realtime()
		
		with open("log.txt", "a", encoding = "utf-8") as f:
			f.write(get_weather + "\n")
		print(get_weather)



