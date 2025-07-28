from django.contrib import admin  # 导入Django管理后台模块
from webadmin.models import HostGroup, Host, Module, Argument  # 导入webadmin应用中的模型类

# 使用循环批量注册模型到Django管理后台
# 注册后可在管理界面通过/admin/路径管理这些模型的数据
for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)  # 将模型类注册到管理后台