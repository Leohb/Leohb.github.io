from datetime import date
from datetime import datetime
from datetime import timedelta
import argparse
import subprocess
import openweathermap as owm
import thinkpage as tp
from constant import METRIC, IMPERIAL, UNIT_C, UNIT_F


# add help to argparse
# user can also get help by executing 'py weather_report_api.py -h'
with open('README.MD', encoding="utf-8") as file:
    description = file.read()

parser = argparse.ArgumentParser(
    description = description,
    formatter_class = argparse.RawTextHelpFormatter)

args = parser.parse_args()


def print_help():
    '''This function prints help'''
    try:
        output = subprocess.check_output('py .\weather_report_api.py -h')
        output = output.decode('gbk')
        print('output:{0}'.format(output))
    except subprocess.CalledProcessError as e:
        output = e.output
        code = e.returncode
        print(code, output)


def input_unit():
    '''set unit of measure, F or C'''
    print('默认温度单位为摄氏度Celsius，风速为meter/sec.\
           \n\t* 输入F，设置为华氏度Fahrenheit，风速为miles/hour.\
           \n\t* 输入C，设置为摄氏度Celsius，风速为meter/sec.')
    unit = ''
    while True:
        unit = input('请输入温度单位>: ')
        unit = unit.strip().lower()
        if unit not in [UNIT_C, UNIT_F]:
            print('输入错误，请重新输入!')
        else:
            break

    return unit

def convert_unit_for_owm(unit):
    '''set unit of measure, F or C'''
    if unit == UNIT_F:
        unit = IMPERIAL
        print('度量单位已设置为F.')
    elif unit == UNIT_C:
        unit = METRIC
        print('度量单位已设置为C.')

    return unit


def date_validator(date):
    '''validate the input date value and format'''
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        print('输入错误，时间格式为yyyy-mm-dd，请重新输入.')
        return False
    else:
        if date.today() <= date <= date.today()+timedelta(days=2):
            return True
        else:
            print('日期超出范围，仅可查询3日内天气预报，请重新输入!')
            return False


# add main check, the script can only be executed directly
# which means it cannot be executed if imported into another module
if __name__ == '__main__':
    print('欢迎查询天气.\
           \n\t* 查询实时天气，请输入城市名称，例如： shanghai\
           \n\t* 查询3日内天气预报，请输入城市名称 日期（空格分割），例如：shanghai 2017-02-01\
           \n\t* 查看帮助, 请输入help或者h')

    unit_tp = UNIT_C
    unit_owm = METRIC

    while True:
        command = input('>: ')
        command = command.strip().lower().split()

        if len(command) == 1:
            choice = command[0]
            owm_current = owm.CurrentWeather(choice, unit_owm)
            tp_current = tp.CurrentWeather(choice, unit_tp)
            if choice == 'history':
                owm_current.get_history()
                tp_current.get_history()
            elif choice == 'quit' or choice == 'exit':
                print('再见！')
                exit(0)
            elif choice == 'help' or choice == 'h':
                print_help()
            elif choice == 'unit' or choice == 'u':
                unit_tp = input_unit()
                unit_owm = convert_unit_for_owm(unit_tp)
            else:
                owm_current.get_current_weather()
                tp_current.get_current_weather()
        elif len(command) == 2:
            location = command[0]
            date = command[1]
            if date_validator(date):
                owm_daily = owm.DailyWeather(location, unit_owm, date)
                owm_daily.get_daily_weather()

                tp_daily = tp.DailyWeather(location, unit_tp, date)
                tp_daily.get_daily_weather()
        else:
            print('指令无效，请从新输入！')
