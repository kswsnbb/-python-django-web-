# -python-django-web-
基于Python和Djanjo实现运维web化
---------------------------------
具体代码见master下danjo
准备环境：
centos 7版本
mysql liunx centos 7版本
pip 版本确保在35以上
mysql:
create database ansible;
如果数据库密码不一样请去ansi_cfg 下dhosts.py下修改engine引擎中root:后面密码
Ansible:
yum install -y epel-release
yum install ansible
ansible all -m setup --tree /tmp/myservers/
vim /etc/ansible/hosts:在这里修改主机名和密码实现免密登录
danjo：
python manage.py createsuperuser
接着输入用户名和密码
python 虚拟环境下
[root@lcoalhost danjo]# python manage.py makemigrations
[root@lcoalhost danjo]# python manage.py migrate
[root@lcoalhost danjo]# python manage.py shell
bootstrap 详细语法见官网：https"//v3.www.bootcss.com/
--------------------------
运行：
python manage.py runserver 0:80
原理：当客户端用户访问URL服务器时，URL服务器会调用视图函数，
视图函数views会通过用户请求返回template前端页面文件。同时也会通过crud调用数据库模型models。
----------------------------------------
项目介绍：

dhosts.py文件：这其实就是一个主机清单生成文件，通过调用SQLAchemy调用数据库，这里需要你创建数据库引擎来调用数据库，创建数据库引擎需要你的数据库类型，用户，密码和数据库的库名。然后创建会话生成器，用于数据库的交互，然后创建一个基类，声明模型。创建模型类：主机和主机组：通过__tablename__指定需要调用的表名，定义主机字段等需要调用的。最后在调用时将结果转为JSON格式
Plan.sh:自动化脚本文件，通过crontab实现自动化更新主机清单内容，我这里是每天更新一次

在danjo文件夹内的urls.py 文件
这里有danjo自带的admin管理界面
如果你创建了其他应用，需要在这里调用（path或re_path都可以）

Index文件夹内的views.py：
该项目主要是调用index应用主机页面展示的功能，在这个文件夹内需要url匹配路径，views视图函数返回用户访问的模型
Index.html:
通过继承继承基类文件的模版（extends）
这里主要是给四个模块项目提供主机页面入口

Webadmin的models.py文件（关键）：
需要导入Django数据库模型模块
这里定义了四个大类，分别是主机，主机组，模块，参数。
主机组：展示主机的名称（数据库里的）
主机：包含主机名称，ip和属组
模块：表示ansible可执行的模块
参数：与模块相对应
其实简单来说就是在数据库上写入了上述的清单，当用户添加调用时会通过这里对数据库进行相应的调用

Url.py 文件：
用户访问的url位置，这里调用了四个模块和主机页

Views.py:该文件的作用就是处理用户请求和调用页面文件
Index直接返回
Add_hosts:
处理POST请求
获取主机组，主机，ip
如果不为空创建对象并返回到模版文件内

Add_modules:
处理POST请求
获取模块，参数
如果不为空就返回相应的实例最后渲染到前端上
Del_arg:
主要是删除参数的请求
删除完参数对象重定向返回到该页面
Task：
如上面的类似

前端部分：
1.basic.html
这里是模块继承的位置，是所有页面部署的基础页面，这里有导航栏，轮播图，页面设计，留言板等
2.Index.html
继承basic.html主要加了四个页面的入口
3.Servers.html
主机详情的入口，其实就是下载ansible官网的web页面文件导入到这里
4.Tasks.html
{% csrf_token %}防止跨站请求访问的安全令牌
5.Add_hosts.html
与上面类似
6.Add_modules.html
与上面类似
