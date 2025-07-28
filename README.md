# My Project
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
