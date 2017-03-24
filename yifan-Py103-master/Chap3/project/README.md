### 安装说明：
运行请安装以下module：

* requests：pip install requests

* dateutil：pip install python-dateutil

### 使用说明：
这是一个查询天气的程序：

* 查询实时天气，输入英文城市名称:shanghai

  将分别返回从OpenWeatherMap和ThinkPage获取的实时天气

  输入中文城市名称:上海，将只返回从ThinkPage获取的数据
* 查询未来3日天气预报，输入英文城市名称 日期:shanghai 2017-02-01

  空格分隔，日期格式为yyyy-mm-dd

  将分别返回从OpenWeatherMap和ThinkPage获取的天气预报
* 查看查询历史, 请输入history.
* 设置度量单位, 请输入unit或者u.

  输入C，设置为摄氏度Celsius，风速为meter/sec(默认值)

  输入F，设置为华氏度Fahrenheit，风速为miles/hour
* 查看帮助, 请输入help或者h.
* 退出, 请输入quit或者exit.
