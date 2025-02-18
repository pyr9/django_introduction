# 1. django Admin模块是什么？
1. Django的后台管理工具
2. 读取定义的模型元数据,提供强大的管理使用页面
# 2. 为什么需要 Django Admin模块？
1. Django Shell新增文章太复杂了
2. 管理页面是基础设施中重要的部分
3. 认证用户、显示管理模型、校验输入等功能类似
# 3. Django Admin模块的使用
1. 创建管理员用户
```shell
PS D:\code\python\django_introduction> python manage.py createsuperuser
Username (leave blank to use 'z004nnre'): pyr
Email address: panyuro@163.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
2. 登录页面进行管理
`http://127.0.0.1:8000/admin`






