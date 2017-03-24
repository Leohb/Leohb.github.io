# python103个人学习策略

1. 将Py103的课程任务目录下载到本地。
(git clone git@github.com:leiyunhe/*****)
2. 直接在任务目录文件夹中存放程序和文档。
3. 每日将完成的内容推送到github上。


# python2与python3的区别
从Learn Python The Hard Way中前七个练习来看，主要区别在于语法表达方式。

### 输出函数print
python2：<pre><code>print **********</code></pre>
python3: <pre><code>print (**********)</code></pre>
Comment:对所有的print后面内容一对小括号。
Example:LearnPythonTheHardWay,ex1-ex7

### 命令行输入raw_input()与input()
python2:raw_input()
python3:input()   
Commet:the new input() function reads a line from sys.stdin and returns it with the trailing newline stripped.
Example:LearnPythonTheHardWay,ex14

python2:input()
python3:eval(input())

>参考文档：What's new in Python3 -> Builtins -> PEP 3111

### agrv应用没有变化
Example：ex14

### open(filename)没有变化
Example：ex15


>参考资料：
>1. [Learn Python The Hard Way](https://learnpythonthehardway.org/book/preface.html)
>2. [廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)


# 基本命令

- CLI：echo "This is a test file.">test.txt   #新建文件test.txt,并输入内容This is a test file.
- CLI：cat test.txt    #在CLI输出文件test.txt的内容


# 附加探索：用pip安装模块Pakage（Learn Python The Hard Way-ex46）
看到有人建议安装virtualenv，因此尝试了用pip直接安装其他模块。好处是：不用下载，直接用命令行 <pre><code>pip install nose/distribute/virtualenv</code></pre>

### 第一步：下载并安装pip.
- 下载pip，并解压缩到python27目录。
- 在powershell(CLI)中进入pip目录。
- 运行setup.py。
- 检测pip。

### 第二步：应用pip安装distribute、nose和virtualenv
- CLI进入python27目录。
- 运行 <pre><code>pip install SomePakage</code></pre>.


#Python2 VS Python3
format controling tool：%




