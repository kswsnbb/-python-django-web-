from django.urls import re_path, include
from webadmin import views

urlpatterns = [
    re_path(r'^$',views.index,name='webadmin_index'),
    re_path(r'^add_hosts/$',views.add_hosts,name='add_hosts'),
    re_path(r'^add_modules/$', views.add_modules, name='add_modules'),
    re_path(r'^(\d+)/del/$',views.del_arg,name='del_arg'),
    re_path(r'^tasks/$',views.tasks,name='tasks'),
]