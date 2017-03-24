>说明：安装环境为Win10，已安装有python2，现需安装python3，使两个版本的软件均可正常使用。

# 1.下载软件

官方网站下载软件[python3](https://www.python.org/)

# 2.安装软件

1. 双击运行。

2. 必须勾选“ADD Python 3.6 to PATH”，即为python3设置环境变量。

3. 选择安装方式“Install Now”（默认方式）或者“customize install”（个性化安装，可以更改安装目录）.

![](./pic/python3-setup-1.png)

# 3.如何让电脑按需要随时调用python3或python2.

电脑上同时安装有python2和python3。两者是不兼容的，因此python2编写的代码需调用python2运行，python3代码也只能用python3运行。需要解决的问题是：“在同一台电脑上如何实现python2与3的切换呢？”

1. 进入python2的安装目录，将python.exe文件名改成python2.exe，同理，python3安装文件中的python.exe重命名为python3.exe

2. 检测。打开powershell，输入python2，获得相应的安装版本信息。输入python3，获得相应的安装版本信息。说明安装成功。

![](./pic/python3-check.png)

3. 若出现问题，可重启电脑查看。

>参考文献：
知乎：[在同一台电脑上如何进行python2与3的切换](https://www.zhihu.com/question/22846291)


