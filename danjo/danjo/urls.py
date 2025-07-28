"""
URL configuration for danjo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path  # 导入路径匹配和路由包含模块

urlpatterns = [
    # Django自带的后台管理界面，访问/admin/会进入管理系统
    path('admin/', admin.site.urls),

    # 将所有以/index/开头的URL请求转发到index应用的URL配置中处理
    path('index/', include('index.urls')),

    # 使用正则表达式匹配所有以/webadmin/开头的URL请求，转发到webadmin应用的URL配置
    # 这里使用re_path可以编写更灵活的正则表达式模式
    re_path(r'^webadmin/', include('webadmin.urls')),
]
