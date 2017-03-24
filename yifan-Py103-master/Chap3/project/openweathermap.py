import requests
from datetime import datetime
from dateutil import tz
from constant import OWM_CURRENT_API, OWM_DAILY_API, APPID, LANG, METRIC, IMPERIAL, TIMEOUT


class OpenWeatherMap(object):
    def __init__(self, api, location, unit):
        self.api = api
        self.location = location
        self.unit = unit
        self.lang = LANG
        self.appid = APPID
        self.timeout = TIMEOUT

    def get_request(self):
        '''get current weather data from open weather map API,
        return the response data'''
        data = {}
        params = {'q': self.location, 'units': self.unit, 'lang': self.lang, 'appid': self.appid}
        try:
            r = requests.get(self.api, params=params, timeout=self.timeout)
            if r.status_code == requests.codes.ok:
                data = r.json()
            else:
                print('访问OpenWeatherMap API失败!')
        except (requests.Timeout, requests.ConnectionError):
            print('网络异常或者OpenWeatherMap API连接超时!')

        return data


    def set_display_unit(self):
        '''set unit of measure when print weather information'''
        units = {}
        if self.unit == IMPERIAL:
            temperature_unit = 'F'
            wind_unit = 'miles/hour'

        if self.unit == METRIC:
            temperature_unit = 'C'
            wind_unit = 'meter/sec'

        units['temperature'] = temperature_unit
        units['wind'] = wind_unit

        return units


    def deg_to_direction(self, deg):
        '''convert wind degree to compass direction'''
        direction = ['N', 'NNE', 'NE', 'ENE',
                     'E', 'ESE', 'SE', 'SSE',
                     'S', 'SSW', 'SW', 'WSW',
                     'W', 'WNW', 'NW', 'NNW']
        value = int((deg / 22.5) + 0.5)
        return direction[value % 16]


    def timestamp_to_format(self, timestamp):
        '''convert timestamp to string format datetime in user local time zone'''
        dt = datetime.fromtimestamp(timestamp, tz.tzlocal())
        fmt = '%Y-%m-%d %H:%M:%S %z'
        dt = dt.strftime(fmt)
        return dt


    def timestamp_to_dateString(self, timestamp):
        '''convert timestamp to string format date'''
        dt = datetime.fromtimestamp(timestamp)
        fmt = '%Y-%m-%d'
        date = dt.strftime(fmt)
        return date


class CurrentWeather(OpenWeatherMap):

    weather_history = {}

    def __init__(self, location, unit):
        super().__init__(OWM_CURRENT_API, location, unit)


    def get_current_weather(self):
        '''This function send a request to get current weather information,
        then prints the data'''
        data = self.get_request()
        if data:
            if data['name'].lower() == self.location:
                self.print_current_weather(data)
                data['unit'] = self.unit
                self.weather_history[data['name']] = data
            else:
                print('-'*17 + 'OpenWeatherMap API' + '-'*17)
                print('无法查到地区{0}!'.format(self.location))


    def get_history(self):
        '''This function prints the current weather query history'''
        length = len(self.weather_history)
        if length != 0:
            for index, key in enumerate(self.weather_history, start=1):
                print(index)
                self.print_current_weather(self.weather_history[key])
        else:
            print('OpenWeatherMap:没有查询记录!')


    def print_current_weather(self, data):
        '''organize current weather data, then print'''
        main = data['main']
        sys = data['sys']

        location = data['name']
        weather = data['weather'][0]['description']
        temperature = main['temp']
        temperature_unit = 'C'
        pressure = main['pressure']
        humidity = main['humidity']

        if 'deg' in data['wind']:
            wind_direction = self.deg_to_direction(data['wind']['deg'])
        else:
            wind_direction = ''

        wind_speed = data['wind']['speed']
        wind_unit = 'meter/sec'
        pressure = main['pressure']
        clouds = data['clouds']['all']
        timestamp = data['dt']
        sunrise = sys['sunrise']
        sunset = sys['sunset']

        if 'rain' in data:
            rain = data['rain']['3h']
        else:
            rain = 0

        if 'snow' in data:
            snow = data['snow']['3h']
        else:
            snow = 0

        units = self.set_display_unit()
        print('-'*17 + 'OpenWeatherMap API' + '-'*17)
        weather_info = '''
                    城市: {0}
                    时间: {1}

                    天气: {2}
                    温度: {3}\u00b0{4}

                    气压: {5} hPa
                    湿度: {6}%
                    云量: {7}%
                      风: {8} {9} {10}

                    日出: {11}
                    日落: {12}

                    降雨量: {13} mm
                    降雪量: {14} mm'''

        print(weather_info.format(self.location, self.timestamp_to_format(timestamp),
                                  weather, str(round(temperature)), units['temperature'],
                                  str(int(pressure)), str(humidity), str(clouds),
                                  wind_direction, str(round(wind_speed)), units['wind'],
                                  self.timestamp_to_format(sunrise),
                                  self.timestamp_to_format(sunset),
                                  str(rain), str(snow)))


class DailyWeather(OpenWeatherMap):
    def __init__(self, location, unit, date):
        super().__init__(OWM_DAILY_API, location, unit)
        self.date = date


    def get_daily_weather(self):
        '''This function sends a request to get daily forecast weather information,
        then prints the data'''
        data = self.get_request()
        if data:
            if data['city']['name'].lower() == self.location:
                self.print_daily_weather(data)
            else:
                print('-'*17 + 'OpenWeatherMap API' + '-'*17)
                print('无法查到地区{0}!'.format(self.location))


    def print_daily_weather(self, data):
        '''organize daily forecast weather data, then print'''
        location = data['city']['name']
        daily = data['list']
        for day in daily:
            dt = self.timestamp_to_dateString(day['dt'])
            if self.date == dt:
                weather = day['weather'][0]['description']
                temperature_min = day['temp']['min']
                temperature_max = day['temp']['max']
                pressure = day['pressure']
                humidity = day['humidity']
                wind_direction = self.deg_to_direction(day['deg'])
                wind_speed = day['speed']
                clouds = day['clouds']

        units = self.set_display_unit()
        print('-'*17 + 'OpenWeatherMap API' + '-'*17)
        weather_info = '''
                    城市: {0}
                    日期: {1}

                    天气: {2}
                最高温度: {3}\u00b0{5}
                最低温度：{4}\u00b0{5}

                    气压: {6} hPa
                    湿度: {7}%
                    云量: {8}%
                      风: {9} {10} {11}'''

        print(weather_info.format(self.location, self.date, weather,
                                  str(round(temperature_max)), str(round(temperature_min)),
                                  units['temperature'], str(int(pressure)),
                                  str(humidity), str(clouds),
                                  wind_direction, str(round(wind_speed)), units['wind']))
