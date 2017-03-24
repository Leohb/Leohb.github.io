import requests, json

user_input = input("请输入城市或指令：")

url = "https://api.thinkpage.cn/v3/weather/now.json?key=kdtkmkoewxfhmqbx&location=" + user_input + "&language=zh-Hans&unit=c"

r = requests.get(url)

result = json.loads(r.text)

city = result["results"][0]['location']['name']
realtime = result["results"][0]['last_update']
temperature = result["results"][0]['now']['temperature']
weather = result["results"][0]['now']['text']

print(city + realtime + "天气情况为：" + weather + "," + "温度："+ temperature + "摄氏度" )

