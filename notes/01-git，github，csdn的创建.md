# Git、GitHub、CSDN 的创建与使用

> 学习AI大模型开发的第一篇笔记，记录 Git 版本控制、GitHub 代码托管和 CSDN 技术博客的创建与配置过程。

---

## 一、Git 和 GitHub 是什么

很多人会混淆这两个东西，其实它们完全不同：

| | 是什么 | 打个比方 |
|---|---|---|
| **Git** | 安装在本地电脑上的**软件**，负责记录代码的每次改动 | 就像 Word 的"修订记录"功能 |
| **GitHub** | 一个**网站**（微软旗下），远程存放你的代码 | 就像网盘，把代码存到网上 |
| **CSDN** | 一个**中文技术博客网站**，发文章 | 就像知乎/公众号，写技术文章 |

**Git 不会自动提交到 GitHub**，需要手动执行三步操作：

```
git add . → git commit -m "说明" → git push
```

## 二、从零创建 GitHub 仓库

### 第一步：确认 Git 环境和 GitHub 账号

```powershell
# 1. 确认 Git 装了没有
git --version
# 我的结果：git version 2.33.1.windows.1

# 2. 查看已配置的用户名和邮箱
git config --global user.name
git config --global user.email
# 我的结果：badboy718 / 13070101975@139.com
```

### 第二步：在 GitHub 网站上创建仓库

1. 浏览器打开 https://github.com ，登录账号
2. 点右上角头像 -> **New repository**（新建仓库）
3. 填写信息：
   - **Repository name**：`ai-dev-learning`
   - **Description**：AI大模型开发学习记录
   - **Private**（私有仓库）
   - **不勾选** Add a README 等选项
4. 点击 **Create repository**

### 第三步：本地创建文件夹并关联 GitHub

```powershell
# 1. 创建本地文件夹
mkdir C:\Users\13070\Documents\ai-dev-learning
cd C:\Users\13070\Documents\ai-dev-learning

# 2. 初始化 Git 仓库
git init
# 显示：Initialized empty Git repository in ...

# 3. 关联远程 GitHub 仓库
git remote add origin https://github.com/badboy718/ai-dev-learning.git
```

### 第四步：创建 README.md 和 .gitignore

**README.md**（仓库首页展示的内容）：

```markdown
# AI大模型开发学习记录
> 基于黑马程序员课程的学习笔记与练习代码
## 当前进度
- [x] 阶段一：Python基础
- [x] 阶段二：Python高阶语法
- [ ] MySQL学习中...
- [ ] 阶段三：智能体平台开发
```

**.gitignore**（告诉 Git 哪些文件不需要上传）：

```
.idea/
__pycache__/
*.pyc
.DS_Store
Thumbs.db
*.tmp
```

### 第五步：第一次提交和推送

```powershell
git add .                              # 添加所有文件
git commit -m "init: 初始化学习仓库"     # 提交到本地
git branch -M main                     # 重命名分支为 main
git push -u origin main                # 推送到 GitHub
```

## 三、CSDN 博客创建

CSDN 是中文技术博客网站，用来发布学习文章。

### 创建步骤

1. 打开 https://www.csdn.net ，登录账号
2. 进入 **创作中心** -> 新建**专栏**（如"AI大模型开发学习之路"）
3. 点击 **发布文章**，选择 **Markdown 编辑器**
4. 用 Markdown 格式写文章，写完点击 **发布**

### CSDN 与 GitHub 的配合

- GitHub 存放代码和笔记文件（.md）
- CSDN 发布技术博客文章
- CSDN 文章中引用 GitHub 仓库链接，互相引流

## 四、仓库目录结构

```
ai-dev-learning/
├── README.md          # 学习路线和进度
├── .gitignore         # 忽略不需要上传的文件
└── notes/             # 学习笔记（Markdown 格式）
```

## 五、踩坑记录

### SSL 证书问题

首次 `git push` 时报错：

```
fatal: unable to access 'https://github.com/xxx': SSL certificate problem
```

**原因：** Git 版本较旧（2.33.1），与当前网络环境的 SSL 验证不兼容。

**解决方法：**

```powershell
git config --global http.sslBackend schannel
```

设置后重新 `git push` 即可成功。
