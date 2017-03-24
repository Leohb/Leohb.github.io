import requests
from constant import TP_CURRENT_API, TP_DAILY_API, KEY, LANGUAGE, UNIT_C, UNIT_F, TIMEOUT


class ThinkPage(object):
    def __init__(self, api, location, unit):
        self.api = api
        self.location = location
        self.unit = unit
        self.lang = LANGUAGE
        self.key = KEY
        self.timeout = TIMEOUT

    def get_request(self):
        '''get current weather data from open weather map API,
        return the response data'''
        data = {}
        params = {'location': self.location, 'unit': self.unit, 'language': self.lang, 'key': self.key}
        try:
            r = requests.get(self.api, params=params, timeout=self.timeout)
            if r.status_code == requests.codes.ok:
                data = r.json()['results'][0]
            else:
                print('-'*20 + 'ThinkPage API' + '-'*20)
                print('无法查到地区{0}!'.format(self.location))
        except (requests.Timeout, requests.ConnectionError):
            print('网络异常或者ThinkPage API连接超时!')

        return data


    def set_display_unit(self):
        units = {}
        if self.unit == UNIT_F:
            temperature_unit = 'F'
            wind_unit = 'miles/hour'

        if self.unit == UNIT_C:
            temperature_unit = 'C'
            wind_unit = 'km/h'

        units['temperature'] = temperature_unit
        units['wind'] = wind_unit

        return units


class CurrentWeather(ThinkPage):
    weather_history = {}


    def __init__(self, location, unit):
        super().__init__(TP_CURRENT_API, location, unit)


    def get_current_weather(self):
        '''This function send a request to get current weather information,
        then prints the data'''
        data = self.get_request()
        if data:
            self.print_current_weather(data)
            data['unit'] = self.unit
            self.weather_history[data['location']['name']] = data


    def get_history(self):
        '''This function prints the current weather query history'''
        length = len(self.weather_history)
        if length != 0:
            for index, key in enumerate(self.weather_history, start=1):
                print(index)
                self.print_current_weather(self.weather_history[key])
        else:
            print('ThinkPage: 没有查询记录!')


    def print_current_weather(self, data):
        '''organize current weather data, then print'''
        location = data['location']['name']
        weather = data['now']['text']
        temperature = data['now']['temperature']
        update_datetime = data['last_update']

        units = self.set_display_unit()
        print('-'*20 + 'ThinkPage API' + '-'*20)
        weather_info = '''
                    城市: {0}
                    时间: {1}

                    天气: {2}
                    温度: {3}\u00b0{4}'''

        print(weather_info.format(self.location, update_datetime,
                                  weather, str(temperature), units['temperature']))


class DailyWeather(ThinkPage):
    def __init__(self, location, unit, date):
        super().__init__(TP_DAILY_API, location, unit)
        self.date = date


    def get_daily_weather(self):
        '''This function sends a request to get daily forecast weather information,
        then prints the data'''
        data = self.get_request()
        if data:
            self.print_daily_weather(data)


    def print_daily_weather(self, data):
        '''organize daily forecast weather data, then print'''
        location = data['location']['name']
        daily = data['daily']
        for day in daily:
            if self.date == day['date']:
                weather_day = day['text_day']
                weather_night = day['text_night']
                temperature_high = day['high']
                temperature_low = day['low']
                wind_direction = day['wind_direction']
                wind_speed = day['wind_speed']
                wind_scale = day['wind_scale']

        units = self.set_display_unit()
        print('-'*20 + 'ThinkPage API' + '-'*20)
        weather_info = '''
                    城市: {0}
                    日期: {1}

                    白天: {2}
                    晚间: {3}
                最高温度: {4}\u00b0{6}
                最低温度: {5}\u00b0{6}
                    风向: {7}
                    风速: {8} {9}
                风力等级: {10}'''

        print(weather_info.format(self.location, self.date,
                                  weather_day, weather_night,
                                  str(temperature_high), str(temperature_low),
                                  units['temperature'], wind_direction, wind_speed,
                                  units['wind'], wind_scale))
