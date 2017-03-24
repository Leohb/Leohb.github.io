# Python 3 in 1 picture

仔细读了两遍，看不懂也记不住，没有任何感觉。我在想，这对于大牛来说都不是事儿，但是，也许有一张Python2的对比图，对于我这种小白，学起来更容易吧。

# Python 3 Tutorial（sololearn）
(打不开啊打不开)


# Python2 or Python3

> Should I use Python 2 or Python 3 for my development activity?

- 版本
	+ Python创建于1991年。
	+ Python2在2010年发布了最终版2.7
	+ Python3.0在2008年发布,（2012,V3.3;2014,v3.4;2015,v3.5）至今已发布至3.6(2016)。
- 最大的变化是更好地支持Unicode编码。
- python3消除了很多（Python2）易给初学者造成的困难（quirks、cruft、annoyances、warts）。
- 有些第三方模块和功能仅支持Python2，未更新支持Python3的版本，而且不能移植到Python3.
- core syntactic or semantic changes
- 当你一定需要python2模块时，尽量把它移植到Python3上。
- Python2与Python3之间可以相互转化。比如，python3代码经过3to2工具可以在Python2平台上使用，2to3同理。相比较而言，前者更容易。



# What's new in Python 3.0

>Document: What's new in Python 3.0

## Common Stumbling Blocks

	- 输出使用print()函数
	- 分隔符separator
	- 视图和迭代器代替列表（Views & Iterrators Instead of Lists）
		eg
		1. dict.keys()  dict.items()  dict.values() 返回视图    k = d.keys(); k.sort()  ——> k = sorted(d)
		2. map()   filter()  返回迭代器  map(func, *sequences)  ——>  list(map(func, itertools.zip_longest(*sequences)))
		3. xrange()  ——> range()
		4. zip() 返回迭代器
	- 比较Ordering comparison
	- 整数Integers
	- Text V. Data 代替Unicode Vs. 8-bit
	
## 语法变化Syntax

	- 新语法 
		1. 扩展的迭代器 （a, *rest, b） = range(5)表示：a=0，b=4, rest:[1,2,3]
		2. Set literal
		3. 新的八进制、二进制和字节字符。
	- 语法变化
		1. 保留字：as,with True,False,None
		2. except exc as var 代替 except exc，var
		3. class C (metacalss=M)：
		       ...
		代替
			class C:
				__metaclass__ = M
				...
		4. ... for var in (item1, item2,...)代替... for var in item1, item2
		5.省略号，不允许中间有空格。
	- 去掉的语法。 
		1. !=代替<> 
		2. 与import相关的语法仅保留 from .[module] import name

## Library 变化

有些模块更名，有些不再有了。

## 字符格式String Formatting

%被弃用，

## 其他各种各样的变化

1. 运算符和特殊字符
2. 内置命令 input()


## Python2代码移植到Python3

使用2to3代码转化器







