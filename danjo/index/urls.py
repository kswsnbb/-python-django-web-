from django.urls import re_path  # 导入正则表达式路径匹配模块
from index import views  # 导入index应用的视图函数

urlpatterns = [
    # 使用正则表达式匹配URL路径
    # r'^$' 表示匹配空路径（即根路径，例如http://example.com/）
    # views.index 是对应的视图函数，用于处理该URL请求
    # name='index' 为这个URL模式指定一个唯一的名称，方便在模板或代码中引用
    re_path(r'^$', views.index, name='index'),
]