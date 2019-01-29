# pymark

> 主要解决更新API接口文档效率问题

[TOC]

## 一. 场景分析

前后端分离背景下， 后端API更新不及时，

- 开发完之后再去更新数据不同步
- 开发过程中口头对接API易遗忘，有道云、word文档不方便浏览

这块我本身代码托管在码云，所有文档索性也放在wiki里，发现看着还是很舒服的，麻烦在markdown的书写上、模版都是固定的

<center><img src="http://qiniu.s001.xin/ni09f.jpg"></center>

💡想法就是如果能**把模版view提取出来，填写动态数据，生成固定markdown格式**就好了



## 二. 开发

首先是定义变量，生成model

- 接口名称
- 请求方法GET/POST
- URL = 协议+域名【端口号】+ 版本 + 路径path
- 请求参数
- 成功回调
- 失败回调

<center><img src="http://qiniu.s001.xin/ogl0s.jpg" width=600></center>

原理就跟postman差不多，把url前面固定的部分协议域名版本号封装起来当作环境变量

<center><img src="http://qiniu.s001.xin/eb47n.jpg"></center>

## 三. 展示

<center><img src="http://qiniu.s001.xin/wqvwa.jpg"></center>

<center><img src="http://qiniu.s001.xin/wt495.jpg" width=600></center>

## 四. demo地址

给自己用的，做的比较粗糙，称不上项目，就勉强叫它demo吧

<a href="https://github.com/ZHAISHENKING/mark">github</a>



## 五. 使用

1. python3环境

```bash
# 依赖安装
pip install -r requirements.txt
```

2. 创建mongo数据库`mark`

3. 启动需自行创建`local_settings.py`和`production.py`文件

`local_settings.py`

```python
ENV = 'dev'
PORT = 27017
NAME = ""
PWD = ""
```

`production.py`

```python
ENV = 'prd'
PORT = 27017
NAME = ""
PWD = ""
```

4. 运行

```python
python manage.py runserver
```

打开` localhost:12341/mark`查看

5. 后台

`localhost:12341/api/`

```python
# 进入shell
python manage.py shell
# 创建管理
from admin import *
a=AdminUser(username="admin",password="admin",email="demo@qq.com")
a.save()
```


