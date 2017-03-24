#  前提

运行在本地服务器上的程序，通过CLI启动程序，访问http://127.0.0.1:5000 ，可进行正常的交互。（我栽在这一步很长时间）

# 步骤

+ 注册heroku账号。
+ 在CLI登录heroku。```heroko login``` 根据提示输入用户名和密码。
+ 在github上新建仓库repository，命名为online-weather、初始化，然后克隆到本地指定文件夹folder。在CLI运行```git clone [online-weather仓库的地址]```。至此，本地仓库folder/online-weather 建立完成。
+ 将准备好的（本地正常运行的）程序拷贝到folder/online-weather。在CLI（虚拟环境）试运行并测试程序```python run.py```，其中run.py为主程序。
+ 在CLI运行```pip freeze```,获得已通过pip安装的模块（和版本号）

    + 可直接为app 创建requirements.txt文件。
    + 新建requirements.txt，将程序中涉及到的模块以版本号复制粘贴到此文件，并保存到主程序的同级目录。

+ 新建Procfile文件（注意：没有扩展名），```web: gunicorn run:app --log-file -```，保存到主程序的同级目录。
+ 新建runtime.txt, ```python-3.6.0``` ，保存到主程序的同级目录。
+ 在CLI（虚拟环境），```heroku create appname```其中appname将显示在部署生成的网址中。
+ 在CLI（虚拟环境），```heroku ps:scale web=1```
+ 在CLI（虚拟环境）完成部署，

    + ```git add .```
    + ```git commit -m "deploy app"```
    + ```git push heroku master```

+ 在CLI（虚拟环境），```heroku open``` 或者直接打开部署中提供的网址，http:[appname].herokuapp.com
+ 备注：

    + ```heroku logs```查看日志，用以排查问题。
    + 可以在heroku网站的dashboard中修改并设置app的一些参数。
    + 设置buildpacks,在CLI中，```heroku buildpacks:set heroku/python```
    + 通过heroku help可以查询到各种操作的方法。
