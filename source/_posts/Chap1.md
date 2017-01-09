# Chap1 任务：制作本地天气查询小公举

## 1.同步AIminder/Py103下的 weather_info.txt文件到本地仓库

1.1 在本地仓库下使用命令下载远程主机的更新文件
  ```bash
  $ git remote add aiminder git@github.com:AIminder/Py103.git
                      |                   |
                  <远程主机名>         <远程主机的地址>
  $ git pull aiminder master
  ```

  附加信息：[我的git cli命令笔记](https://github.com/Leohb/Py103/Chap1/note/gitcli.md)

1.2 检查本地仓库文件夹下的 *weather_info.txt* 文件
  ```markdown
  $ more weather_info.txt

  北京,晴
  海淀,晴
  朝阳,晴
  ...
  ```
## 2.整理思路  

  2.1 目标为输入城市名，返回天气信息，不难想到要用到 **字典** 类型，那第一步需要读取 *weather_info.txt* 的内容。
  ```python
  with open("weather_info.txt","r") as file:
      weather_fo = file.readlines()
  # 首先使用open()读取 weather_info.txt 文件内容 赋值给file，并将每一行以字符串的格式注入到weather_fo列表
  # 使用with然后赋值给file是我的习惯，因为不用flle.close()啦 哈哈哈
  ```
  2.2 接下来就是将列表 *weather_fo* 转换为字典

  ```python
  city_dict = {}
  for item in weather_fo:
    item = item.split(",")
    city_dict[item[0]] = item[1]
    # 对应字典的key来赋值，循环跑一边就OK了。
  ```
  2.3 我还查到另一种更为简洁的方式
  ```python
  city_dict = dict(item.split(",") for item in weather_fo)
  # 遍历weather_fo每一行 -> item，对字符串根据“，”来分离，初始化city_dict
  ```
  但是有个疑问，按我的理解，*item.split(",")* 这也是列表，将字符串分列后的list

  ![](/img/list_check.png)

  但是，为啥上面可以直接将列表转换成字典呢？有点不太懂。。后面先去找找dict的资料，如果不行再去issue上请教教练了~

## 3.接下来就是交互界面啦

  3.1 考虑到需要重复多次输入指令，我使用了 *while + break*

```python
while True:
  ...
  elif cmd == "quit" or cmd == "exit":
      break
# 只有这种情况才能 break 跳出循环
```

  3.2 然后是history的问题了，我考虑过是不是再新建一个文件，历史记录都填进去，后来还是添加了一个his列表
  听说添加列表会增加程序的内存消耗，不知是不是，现在小程序还不在乎这点 哈哈哈
```python
# 我的做法是在成功打印出天气的这个条件里，将输出的内容append到his列表里面，再在history的条件下调用，这样感觉比较方便
if cmd in city_dict:
  print("现在是%s %s %s " % (time,cmd,city_dict[cmd]))
  his.append(str(time)+" "+ cmd + " " + str(city_dict[cmd]))
elif cmd == "history":
    print("您之前查询过：\n")
    for i in his:
        print(i)
```

  3.3 接下来就是help和匹配条件之外的输入了，不多说，就是print。

```python
elif cmd == "help":
    print('''
    以下为相关操作命令说明:
    - 输入<城市名>，获取该城市的天气信息；
    - 输入<history>，获取历史查询信息；
    - 输入<help>，获取帮助信息；
    - 输入<quit>或<exit>,退出该程序。
    ''')
else:
    print("我好像不明白，请输入正确的指令或者输入[help]进行查询。")
  # 学习了siri的语气 哈哈哈哈 我好像不明白 哦...
```

## 4.最后 附上整体的代码~

```python
import time
time = time.strftime("%Y-%m-%d %X",time.localtime())
with open("weather_info.txt","r") as file:
    weather_fo = file.readlines()
city_dict = dict(item.split(",") for item in weather_fo)
his = []
while True:
    cmd=input("请输入指令或您要查询的城市名:")
    if cmd in city_dict:
        print("现在是%s %s %s " % (time,cmd,city_dict[cmd]))
        his.append(str(time)+" "+ cmd + " " + str(city_dict[cmd]))
    elif cmd == "help":
        print('''
        以下为相关操作命令说明:
        - 输入<城市名>，获取该城市的天气信息；
        - 输入<history>，获取历史查询信息；
        - 输入<help>，获取帮助信息；
        - 输入<quit>或<exit>,退出该程序。
        ''')
    elif cmd == "history":
        print("您之前查询过：\n")
        for i in his:
            print(i)
    elif cmd == "quit" or cmd == "exit":
        break
    else:
        print("我好像不明白，请输入正确的指令或者输入[help]进行查询。")
```
