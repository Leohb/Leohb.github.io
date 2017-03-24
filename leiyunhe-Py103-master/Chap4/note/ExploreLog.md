# Flask

## 安装

### python3的环境与版本

python 3.3
Flask 0.10
Werkzeug 0.9

### pip-9.0.1

Python3 > scripts > pip 3.5 

我办公电脑同时安装了python2和python3，在运行pip时一直出错，不能解决，最终采取的办法是：将python2从环境变量路径中删掉，将python3.exe修改为python.exe



### virtualenv

```
pip3.5 install virtualenv
```

$ mkdir myproject
$ cd myproject
$ virtualenv venv

+ 问题：运行``` virtualenv venv ```不能成功。
+ 推测：配置环境的问题。python2与python3两个文件下都安装了pip和virtualenv，运行是不能决定是哪个virtualenv。
+ 对策：将python2\scripts\virtualenv 直接删掉。

$ venv\Scripts\activate

退出虚拟环境：deactivate

+ 问题：进入虚拟环境失败。```venv\scripts\activate 失败。
+ 分析：错误信息提示能够找到文件，但不能运行脚本，参阅https://technet.microsoft.com/zh-CN/library/hh847748.aspx
+ 对策：参考错误提示信息，修改执行策略。

$ ```get-ExecutionPolicy ```

> restricted #不运行未签名的脚本

$``` set-ExecutionPolicy -ExecutionPolicy RemoteSigned ```
$``` get-ExecutionPolicy ```

> RemoteSigned #不运行下载的未签名脚本，可运行本地未签名的脚本

$```pip3.5 install Flask```

$```pip list```

> Flask-0.12 Jinja2-2.9.5 MarkupSafe-0.23 Werkzeug-0.11.15 click-6.7 itsdangerous-0.24

## 更新pip

$```pip install --upgrade pip setuptools```

安装flask:

 $```pip install flask```

## flask例子

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

```
$ set FLASK_APP=hello.py
$ flask run

+ 问题：

Error: Could not locate Flask application. You did not provide the FLASK_APP environment variable.

+ 方法：
  google搜索 "Error: Could not locate Flask application. You did not provide the FLASK_APP environment variable."

> http://stackoverflow.com/questions/37826016/error-while-running-minimal-flask-application

+ 对策：修改运行方法（win10）：

1. $ setx FLASK_APP hello.py
2. 重启powershell
3. $ flask run

# html静态网页

很简单，很快就能做好一个简易的网页页面原型。接下来的问题就是交互了。

# 服务器与网页交互HTTP

## HTTP Methods: GET vs POST

### 实现网页端的简单交互

+ 问题：导入Chap3的queryRealtime实时查询天气代码时，出现错误为：ImportError: No module named 'requests'。

+ 分析：需要在虚拟环境中安装requests、json

+ 对策：在虚拟环境venv中，
  ``` pip3.5 install requests  ```
  ``` pip3.5 install json  ```出错：json模块不需要专门安装。

### 通过代码html和mvp示例代码，实现了基本的网页交互。

参考代码：https://www.tutorialspoint.com/flask/flask_http_methods.htm


### 返回结果呈现在新的网页中,如何在当前网页显示结果

+ 问题：返回结果显示在新网页中。如何将结果展示在本网页中呢？

+ 分析1：在html网页中增加新的label，用于展示即将返回的结果
+ 困难：无法解决（找不到可供模仿的案例，也不能读懂官方文档），暂时放下。
+ 对策：无法解决

+ 分析2：html中的框架也许有用。
+ 对策：寻找到内联框架<iframe></iframe>，可以实现在当前网页的其他位置显示form的返回内容。

  > 参考资料：http://www.jianshu.com/p/28385b328ec2
  > target：该属性规定在何处显示action属性中指定的URL所返回的结果。取值有:
  > _blank（在新窗口中打开）
  > _self（在相同的框架中打开，默认值）
  > _parent（在父框架中打开）
  > _top（在整个窗口中打开）
  > framename（在指定的框架中打开）

+ 步骤：
  - 1.增加form的属性，target = "framename"  
  - 2.<iframe name= "framename"></frame>

### 更多的交互：帮助、历史和的响应

+ 思路：仿照查询按钮，写出响应函数
+ 对策：通过对代码的阅读与微小修改，逐步精简函数，最终明白了帮助和历史按钮不同于查询按钮，前两者只需要点击按钮，返回对应内容即可。也就是，将form的action设置为help和history网页。通过get方法获得具体内容。

### 如何让日志分行显示(python程序在html中的换行问题)

+ 问题：程序运行后，日志已经逐条显示到日志文件log.txt中，一行一条记录。单击“历史”按钮，返回的查询日志不能按记录分行显示，看起来比较乱。
+ 思路：html网页响应时调用了history函数，因此需要在history函数中修改。history函数的返回值是所有记录组成的字符串，如何将这些字符串按顺序逐行显示呢？
+ 分析1：file.readlines()和循环输出均不起作用。因为返回值必须是一个值。
+ 分析2：循环print也不行。貌似需要return
+ 分析3：html网页的字符串显示不能识别\n进行换行，因此需要将字符串中的\n替换为<br>,即可实现换行。

+ 对策：使用string.replace("\n","<br>")以及string.replace(" ","<br>")

### 根据小伙伴上周作业启发，需要将key和用户ID抽离出来。

+ 问题：抽离key和用户名，模仿优秀的代码，让程序的功能更独立。此外，需考虑“不建议在生产环节下暴露 key！生产环境下请通过后端进行签名验证”

+ 分析1：先根据心知天气提供的示例代码修改调用方式。根据实例代码修改，修改过程中，因为基础不扎实，粗心大意，不细致思考，导致掉到json格式的坑里，折腾了很久。错误代码是"str indices must be integers"。
+ 结果：json.loads()是将json中string格式字符串‘{..}’转换成字典格式{..},进行转换处理后才可进行字典的取值操作。

+ 分析2：实现后端签名验证（貌似很复杂，待完善）


### 页面美化设计（css）

+ 问题1：如何将两个按钮排列在同一行
+ 对策：[示例1](https://shenwang.blog.ustc.edu.cn/html%E5%85%83%E7%B4%A0%E4%B9%8B%E6%80%8E%E4%B9%88%E5%B0%86%E4%B8%A4%E4%B8%AA%E5%85%83%E7%B4%A0%E6%8E%92%E5%88%97%E5%9C%A8%E8%A1%8C/)，具体如下：

```
如何将两个div设置在一行?
给这两个DIV设定一个宽度，然后定义float:left; display:inline;

例如HTML是这样：
< div class=”container”>
< div class=”box”> 121212< /div>
< div class=”box”> 455656< /div>
< /div>

在css里面要让两个class为box的DIV并排时只要这样定义即可
.box {width:50%; float:left; display:inline;}

```

+ 问题2：如何通过css实现界面设计
+ 分析：使用css完成页面排布，背景，字体，边框，颜色等的设计
+ 结果：看似简单，具体做的过程中，并不能顺利完成。


## Jinja2：模板引擎






