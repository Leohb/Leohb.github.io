>围观了 珠三角 @zgMichael @guoyuming @simpleowen 北京大区@wangjunyu @yxlbetty 长三角@shippomiru @yanzhiw @Davidfupenghao @betterMax @goldandelion @chuanwj @draachen

# 1.编码问题

## 1.1处理中文

+ 程序第一行注释信息

```
#!usr/bin/env python3
# -*- coding: uft-8 -*-
```

## 1.2读取文件时增加编码的参数

```
with open ("weather_info.txt", "r", encoding = "utf-8")
```


# 2.帮助文档

## 2.1定义一个变量，存储多行字符。

```
big_menu = """
\t* 输入look，开始查询天气情况；
\t* 输入help，获取帮助信息
\t* 输入history，获取历史查询信息
\t* 输入exit，退出程序

"""
```

## 2.2 
 
 
# 3.打印查询城市的记录

## 3.1 文件
 
 ```
 with open("city_history.txt", "a") as f:
	f.write(enterin)
	
.....

 with open("city_history.txt", "r") as f:
	print(f.read())

 ```
 
## 3.2 list


## 3.3 

# 4.将数据转换为字典

# 4.1 append 

weatherlist.append(tuple(("北京","晴"))

# 4.2 setdefault(dic[key],dic[value])

# 4.3


# 5.其他问题

## 5.1 大小写

## 5.2 中英文输入

## 5.3 提取系统当前时间


# 6.程序总结构

@huangdamao @wangjunyu @Davidfupenghao @Leohb @Yifan127

定义函数与调用函数

# 7.Git使用

官方文档：

>fork： https://help.github.com/articles/fork-a-repo/
>同步fork： https://help.github.com/articles/syncing-a-fork/

我的Git使用步骤：

## fork仓库到个人仓库

点击右上角的“fork”，完成Fork your own copy of source repository

## 克隆个人远程仓库到本地电脑

git clone git@github.com:leiyunhe/Py103.git

## 同步fork的源仓库更新的内容

git remote -v

git remote add upstream git@github.com:AIMinder/Py103.git

git remote -v

git fetch upstream

从上游仓库fetch更新

git checkout master

git merge upstream/master

git remote


## 从个人远程仓库下载内容到本地（在本地仓库的目录中）

git pull


## 将本地内容更新至个人远程仓库（在本地仓库的目录中）

+ **$**git add .
+ **$**git commit -m "description/notes"
+ **$**git push





 