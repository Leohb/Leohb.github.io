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


## 从个人远程仓库下载内容到本地

git pull


## 将本地内容更新至个人远程仓库

+ **$**git add .
+ **$**git commit -m "description/notes"
+ **$**git push



