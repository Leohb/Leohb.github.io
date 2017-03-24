#基于hexo搭建博客的最小行动指南

说明：
1. 本文对官网文档进行精简，仅包含基于hexo搭建官网文档的最少步骤（暂时忽略任何个性化配置的步骤），用最少时间完成博客的成功搭建（这对小白来说非常重要。因为一次次的配置个性化信息，一次次搭建失败，给如我一样的小白，带来极大的时间浪费和心力消耗）。
2. 一定要完全参照官方文档。（遇到问题再去查其他教程和说明。作为小白，有时候，你甚至不知道自己的问题是什么，所以要借助其他小伙伴的折腾路径，逐步界定自己的问题，然后再回官网查阅文档）
3. **未完待续.....**

## 安装node.js

下载软件，默认方式安装。CLI```node -version```查看到版本信息，确认安装正常。

## 安装git

下载软件，默认方式安装。CLI```git -version```查看到版本信息，确认安装正常。

## 安装hexo

CLI ```npm install -g hexo-cli```
时间视网络情况而定，如果不行，就多尝试几次。我尝试了至少五次才成功的。有时候慢，有时候快。

## hexo配置与部署

```hexo init <folder>```新建网站
```hexo generate```生成静态网页
```hexo s```启动服务器

## 本地检测

默认地址为：http://localhost:4000/
但是，win10系统中，不能响应。解决办法是更改端口：例如```hexo s -p 2000```

>参考方法：
> 1. hexo官网服务器设置.https://hexo.io/zh-cn/docs/server.html
> 2. WilliamStart.“hexo s -p 3600 换一个3600的端口号” https://github.com/hexojs/hexo/issues/1568

继续检测：地址栏输入 http://localhost:2000/，成功！

## git pages
按照官方文档提示，操作。

## 在不同电脑上进行hexo更新与同步

https://leroyli.github.io/2016/11/07/hexo-more-PC/
http://shanewfx.github.io/blog/2012/02/16/bulid-blog-by-octopress/
