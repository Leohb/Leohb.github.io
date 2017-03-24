#open the data file, convert into a dictionary,including keys(cities) and value(weather)
with open("weather_info.txt","r", encoding = "utf-8") as f:

	city_weather_dict = {} #create a dict

	#read the data from weather_info.txt 
	#and convert lines to a list(city and weather), then to a dictionary
	for line in f:
		s = line.split(',')  #split: turning a string with a certain separator into a list.
		city_weather_dict.setdefault(s[0], s[1])

cities = [] #define a list of cities user input from CLI

print("请输入您要查询的城市名： ")

while(True):
	
	k = input("城市：")

	# case1：quit .  Similar method:capitalize()  upper()  lower()  
	if k.capitalize() in {"Quit","Exit","E","Q"}:  #convert the first letter to Capitalize, 
		print("您查询过的城市有{}个:".format(len(cities)))
		# The method split is the opposite of join
		# join (joins a list of strings with another string as a separator)
		print("、".join(cities),"\n本次查询结束！")  
		break
	# case2: return the weather of cities
	if k in city_weather_dict:
		if k not in cities:  # remove duplicate elements
			cities.append(k)
		print("天气：" + city_weather_dict[k])  # remove leading characters(spaces)

	# case3: 获取帮助信息
	elif k.capitalize() in {"help", "h"}:
		with open("README.md","r", encoding = "utf-8") as f1:
			print(f1.read())


	# case4: cities don't exist
	#elif k not in city_weather_dict:
	else:
		print("对不起，你所输入的城市信息不存在，请尝试查询其他城市！")


	








