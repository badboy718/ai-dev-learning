# Git、GitHub的创建与使用

学习AI大模型开发的第一篇笔记。

学习内容：建GitHub仓库，用Git提交代码

- **Git** -- 本地软件，记录代码每次改动
- **GitHub** -- 远程网站，把代码存到网上

Git不会自动提交到GitHub

需要手动操作：`git add` → `git commit` → `git push`

## 创建 GitHub 仓库

### 1. 网页端

GitHub -> 头像 -> New repository -> 设置仓库名 -> Create repository

### 2. PowerShell 操作

```powershell
# 创建文件夹并初始化
mkdir C:\Users\13070\Documents\ai-dev-learning
cd C:\Users\13070\Documents\ai-dev-learning
git init

# 关联GitHub远程仓库
git remote add origin https://github.com/badboy718/ai-dev-learning.git

# 第一次提交并推送
git add .
git commit -m "init: 初始化学习仓库"
git branch -M main
git push -u origin main
```

## 日常使用

![1782902854492](C:\Users\13070\AppData\Roaming\Typora\typora-user-images\1782902854492.png)



```powershell
# 以后每次写完代码/笔记，就这三步
git add .                          # 添加改动
git commit -m "notes: 写了xxx"     # 提交到本地
git push                           # 推送到GitHub
```

## .gitignore

告诉Git哪些文件不用上传：

```
.idea/          # PyCharm配置
__pycache__/    # Python缓存
*.pyc
Thumbs.db       # Windows缩略图
```

## CSDN 配合

GitHub放代码和笔记文件，CSDN发技术博客文章，两者互相引流。

## 踩坑记录

一、首次 `git push` 报 SSL 证书错误，因为Git版本（2.33.1）较旧。解决方法：

```powershell
git config --global http.sslBackend schannel
```

重新 `git push` 。

二、多种add commit push方式

1. 下载github官方插件，网络原因，下载速度极慢，放弃

2. 小乌龟，commit-->push   SSL报错，**小乌龟调用 Git 时走了自己的网络通道，SSL 验证没被关闭。** 这是 TortoiseGit 的一个常见坑，命令行 Git 和 TortoiseGit 用的 SSL 库不完全一样。