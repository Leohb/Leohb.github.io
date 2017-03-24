# coding:utf-8
import argparse
import subprocess


# add help to argparse
# user can get help by executing 'py weather_report.py -h'
parser = argparse.ArgumentParser(
    description = '''
    这是一个查询城市天气的程序。
    \t* 请输入城市或者地区的中文名称。
    \t\t例子1：上海
    \t\t例子2：浦东新区
    \t* 退出，输入quit或者exit。
    \t* 查询历史记录，输入history。
    \t* 帮助，输入h或者help。
    ''', formatter_class = argparse.RawTextHelpFormatter)
args=parser.parse_args()

filename = "weather_info.txt"
# create a dictionary to store all weather info
# another way to create dict: weather_dict = dict()
weather_dict = {}
# create a dictionary to store query history
weather_history = {}

def convert_txt_to_dict(filename, target_dict):
    '''This function reads data from a file encoding in utf-8,
     then save the data to a dictionary'''
    with open(filename, encoding = "utf-8") as file:
        for line in file.readlines():
            try:
                line = line.strip()
                data = line.split(',')
                # anther way to update dictory:
                # weather_dict.update({data[0]: data[1]})
                target_dict[data[0]] = data[1]
            except:
                pass
    return target_dict

def print_weather_report(city):
    '''This function prints the weather of the city that user input,
    and add the city:weather to a dictionary'''
    weather = weather_dict[city]
    if not weather:
        print("!!!没有查到{0}的天气!!!\n".format(city))
    else:
        print("-" * 20)
        print("{0}: {1}".format(city, weather))
        print("-" * 20)
        weather_history[city] = weather


def print_history(weather_history):
    '''This function prints the query history if it is not empty'''
    length = len(weather_history)
    if length != 0:
        print("您本次一共查询了{0}个城市的天气：".format(length))
        print("-" * 20)
        for key in weather_history:
            print("{0}: {1}".format(key, weather_history[key]))
        print("-" * 20)
    else:
        print("您还没有查询记录。")


def print_help():
    '''This function prints help'''
    try:
        output = subprocess.check_output("py .\weather_report.py -h")
        output = output.decode("gbk")
        print("output:{0}".format(output))
    except subprocess.CalledProcessError as e:
        output = e.output
        code = e.returncode
        print(code, output)

# add main check, the script can only be executed directly
# which means it cannot be executed if imported into another module
if __name__ == "__main__":
    weather_dict = convert_txt_to_dict(filename, weather_dict)
    print("欢迎查询天气预报\n\t* 请输入城市名称\n\t* 退出请输入quit或者exit\n\t* 帮助请输入help或者h")
    while True:
        choice = input("> ")
        choice = choice.strip()

        if choice in weather_dict:
            print_weather_report(choice)
        elif choice.lower() == "history":
            print_history(weather_history)
        elif choice.lower() == "quit" or choice.lower() == "exit":
            print("再见！")
            exit(0)
        elif choice.lower() == "help" or choice.lower() == "h":
            print_help()
        else:
            print("!!!没有查到这个城市[{0}]!!!\n".format(choice))
