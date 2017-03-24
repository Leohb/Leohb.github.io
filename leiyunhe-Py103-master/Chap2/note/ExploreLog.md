# 2017-1-14预习探索

>忽然冒出一个念头：完成第一个MVP的过程非常有成就感，但是，如果Python班结束了，我在三个月后该如何继续往前。于是，我计划先独自思考，运用检索尝试一下未来一周的问题。

## Google“Python开发一个简易桌面版程序”

> http://www.ctolib.com/topics-519.html

主要分为三步：

+ 安装工具和组件库
+ 开发：拖拽控件等。
+ 打包发布

## Google“Python3 GUI tutorial”

网络时代果然让学习变得如此简单，google一下，就找到很多教程：

> https://www.tutorialspoint.com/python3/python_gui_programming.htm

+ Tkinter Widgets

Button Canvas Checkbutton Entry Frame Label Listbox Menubutton Menu Message Radiobutton Scale Scrollbar Text Toplevel Spinbox PanedEindow LabelFrame tkMessageBox

+ Standard attributes

Dimensions Colors Fonts Anchors Relief styles Bitmaps Cursors

+ Geometry Management

pack() grid() place()

> https://wiki.python.org/moin/TkInter

用python和tkinter编程的简单例子

> http://www.tkdocs.com/tutorial/index.html

教程中的代码非常详细，

# 2017-1-15卡包学习

> 昨天的尝试只是一次简单的探索，但是，当看到这周的核心是TKinter时，我的自信又增加了一点点。

## 第一个问题：如何制作标准桌面窗口
从官方文档找来一个例子，直接运行，就生成了标准桌面窗口。虽然丑，就先将就着用吧。

再此基础上，需要增加一个输入框、文本显示框，将点击、退出等分别修改为适合作业的内容。

遗留问题：修改窗口的大小。

## 第二个问题：为窗口添加控件

需要解决的主要是文本输入框，和文本显示框。

文本输入框，已经在解决第一个问题的时候，顺带解决掉了。接下来就是文本输出。

文本输出：

来来回回搜寻了几遍文档，想找到frame中的text，结果什么也没找到。想到课程提示中说，“不要陷到文档里出不来，要时刻记得自己需要解决的问题”。于是，我想起来自己提前预习中有找到一些教程，果断去看看教程中例子是怎么做的。
> https://www.tutorialspoint.com/python/python_gui_programming.htm

```
from tkinter import *

def onclick():
   pass

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
root.mainloop()
```
试运行，阅读这个例子，提炼我需要的关键内容，稍加修改，就可嫁接到我的程序中，如下：

```
text = Text(root)
text.insert(INSERT, "城市")
text.insert(END, "天气")
```
至此，拼凑出来窗口的简单原型。

## 难点：如何将窗口控件与Ch1的程序连接起来？

城市数据来源于“文本输入”，需要使用entry，响应事件为“查询”按钮event
天气数据来源于“ch1中的字典查询”，通过key:城市，到dict中查询到对应的weather，需要导入ch1已经做好的模块。
帮助文档来源于“readme.md"

具体细分为：导入ch1模块，修改几个位置的参数。

entry.get()
query(event) ,event为查询按钮的“点击”事件。
text.insert(INSERT, input)
text.insert(END, dict[input])

### 修改控件的变量和响应事件
这一部分应该是本周任务中最难的地方。
对于控件的应用不熟悉不理解，导致无法修改变量。因此，又反复看文档，做了七八个示例。
> http://www.python-course.eu/tkinter_text_widget.php
> http://www.python-course.eu/tkinter_entry_widgets.php

控件的变量是ch1中完成的功能，因此需要导入ch1的功能模块。

### 导入ch1中的模块
虽然不难，但是自己总是想当然，导致尝试多次，仍旧无果。
这时候，告诉自己停下来，理清思路：继续回去看卡包，提示说要看Modules
看完Modules文档，在命令行尝试了几个小例子，解决了这个问题。
在程序中导入了一个模块，发现可以实现了。终于有了小的突破口。

接下来，1.将所有需要的模块导入并应用起来。2.响应事件

### 需调整优化的程序
在实现本周程序的时候，发现上周的程序中的历史记录功能需要抽离出来。
+ 将历史记录重新写成一个函数，然后方便“历史”标签进行调用。




## 第三个问题：美化

位置：pack(side= "left")  取值分别为left、right、top、bottom

颜色：



## 第四个问题：桌面友好




