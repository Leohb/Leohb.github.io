# Heroku配置与安装 2017-02-23

按照官方安装教程，一步步操作，包括下载，安装，修改环境变量等。最终需要重启电脑使之生效。

+ Postgres
+ error：Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
+ 解决办法：按照错误提示信息，完成Microsoft VC++ 14.0的安装。

+ error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\cl.exe' failed with exit status 2
+ [解决办法](http://stackoverflow.com/questions/40700944/python-error-command-c-program-files-x86-microsoft-visual-studio-14-0-vc)

+ 寻找适合python3的版本，https://pypi.python.org/pypi/lxml/3.6.0
+ error: Failed building wheel for psycopg2

+ No module named "whitenoise"
+ 我今天（2017-2-24）重新找了文件位置，全部重做了一遍，1.把虚拟环境设置到了这个项目文件外面，2.今天把那个postgre的文档全部看了一下，把那个文档下面的命令都试了一遍，都能正确运行。3.刚才根据你的提示，pip install whitenoise安装了一下。

+ No module named  fcntl
+ fcntl是Linux下支持对文件进行关闭等操作的模块，在windows下需要修改api,或者换用其他的模块，如portalocker 等。 http://stackoverflow.com/questions/1422368/fcntl-substitute-on-windows
+ 安装portalocker模块。https://pypi.python.org/pypi/portalocker


# 掉进了莫名其妙的坑   error: command 'C:\\Program Files\\Microsoft Visual Studio 14.0\\VC\\BIN\\cl.exe' failed with exit status 2



# psycopy2安装

在全局和虚拟环境中均安装了psycopg2,结果heroku中的例子就可以运行了。
http://stackoverflow.com/questions/12079607/make-virtualenv-inherit-specific-packages-from-your-global-site-packages



# 部署一直不能成功。当回溯以前程序时，发现：运行chap4 chap5的程序时，都出错了。所以，回到chap4，重新开始吧。

```
Exception in thread Thread-1:
Traceback (most recent call last):
  File "c:\python3\Lib\threading.py", line 916, in _bootstrap_inner
    self.run()
  File "c:\python3\Lib\threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\Craneylei\virtual\venv\lib\site-packages\werkzeug\serving.py", line 670, in inner
    fd=fd)
  File "C:\Users\Craneylei\virtual\venv\lib\site-packages\werkzeug\serving.py", line 564, in make_server
    passthrough_errors, ssl_context, fd=fd)
  File "C:\Users\Craneylei\virtual\venv\lib\site-packages\werkzeug\serving.py", line 474, in __init__
    socket.SOCK_STREAM)
  File "c:\python3\Lib\socket.py", line 460, in fromfd
    nfd = dup(fd)
OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。

```

# 2017-2-28 被虐的...

我决定从chap4开始，重新做一下。一定要彻底解决这个问题。我就不相信，我做不出来！一定要加油！

## chap4本地程序都不能运行了

## html 乱码

# 问题是如何解决的

+ 阅读参考了很多同学的代码，修改了自己的chap4程序，主要是flask 的view function与html的交互方式。
+ 换了台电脑， 前面的程序问题和乱码都没了。所以，说到底还是我电脑环境配置的问题吧。
+ 问题得到解决的那一刻， 是昨晚22：59。多日的问题初步得到解决，那种发自内心的喜悦，真是无法言表啊。


