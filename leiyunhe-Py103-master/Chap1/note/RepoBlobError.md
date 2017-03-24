# 奇怪的问题blob
发现fork到的仓库中多了一个文件，而且，地址中多另一个无缘无故的blob

## 1.现象一： fork后仓库是：leiyunhe/Py103

![](https://github.com/leiyunhe/Py103/blob/master/Chap1/note/pic/githubRepoScreen.png?raw=true)

## 2.现象二：仓库下文件的名称异常（又是blob）

请仔细观察下面两个地址（我从浏览器复制的）：第一行是正常的地址（同学们应该都是这个地址），第二行的地址是我仓库中的。你们看到差异了吧？又是blob。

https://github.com/leiyunhe/Py103/master/Chap1/note/pic/RepoBLob1.png
https://github.com/leiyunhe/Py103/blob/master/Chap1/note/pic/RepoBLob1.png


见图：
![](https://github.com/leiyunhe/Py103/blob/master/Chap1/note/pic/RepoBLob1.png?raw=true)
![](https://github.com/leiyunhe/Py103/blob/master/Chap1/note/pic/RepoBLob2.png?raw=true)


# 我的尝试和发现

## Git内部的对象tree和blob

>官方文档：https://developer.github.com/v3/git/blobs/

```GET /repos/:owner/:repo/git/blobs/:sha```

```"sha": "3a0f86fb8db8eea7ccbb9a95f325ddbedfb25e15",```

+ 我看到了这两行关键信息blob  sha 都是在gitbook更新失败时遇到的错误代码提示信息。
	- 因此，我猜测，gitbook中的错误就是和仓库中的blob有关系。

+ 根据官方文档对blob的描述，其中的content encoding参数，以及url sha等的属性。
	- 我进一步推测：我的错误可能出现在两个方面：一是fork仓库有误，二是中文编码问题。
	
+ 回想到，我的gitbook书籍每次在chap0都不会出错，到chap1才出错。
	- 我缩小范围，我的错误可能是在chap1，更新fork的仓库时，操作有误。
	- 我记得我当时的操作是 ```git clone git@github.com:AIMinder/Py103.git```
	- 当时好像有点地方不对劲。不过，当我看到chap1中已经出现了weather_info.txt时，我没有理会，赶紧去做作业了。


## 参考资料

>技术博客：http://shanewfx.github.io/blog/2012/04/21/learn-git-command/

Git内部有三种对象：commit对象、tree对象、blob对象。

+ blob对象会对应文件快照中变化的文件内容
+ tree对象记录了文件快照中各个目录和文件的结构关系

	- 其中，blob和tree组成了文件快照。

+ commit对象记录了这次要提交到本地仓库的文件快照





