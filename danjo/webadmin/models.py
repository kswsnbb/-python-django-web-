from django.db import models  # 导入Django数据库模型模块
# 主机组模型：用于组织和管理主机
class HostGroup(models.Model):
    groupname = models.CharField(max_length=50)  # 主机组名称字段
    def __str__(self):
        return self.groupname  # 字符串表示形式，用于管理界面和调试
# 主机模型：存储主机的基本信息，关联到特定主机组
class Host(models.Model):
    hostname = models.CharField(max_length=50)  # 主机名称字段
    ip_addr = models.CharField(max_length=15)  # IP地址字段（IPv4格式）
    group = models.ForeignKey(HostGroup, on_delete=models.CASCADE)  # 外键关联到HostGroup
    def __str__(self):
        return "%s: %s" % (self.group, self.hostname)  # 格式：组名: 主机名
# 模块模型：表示Ansible可执行的模块
class Module(models.Model):
    modulename = models.CharField(max_length=50)  # 模块名称字段

    def __str__(self):
        return self.modulename  # 字符串表示形式为模块名
# 参数模型：存储模块对应的参数，与模块为多对一关系
class Argument(models.Model):
    arg_text = models.CharField(max_length=100)  # 参数文本字段
    module = models.ForeignKey(Module, on_delete=models.CASCADE)  # 外键关联到Module
    def __str__(self):
        return "%s:%s" % (self.module, self.arg_text)  # 格式：模块名: 参数文本