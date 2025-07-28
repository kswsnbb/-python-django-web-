from django.shortcuts import render  # 导入render函数用于渲染模板
def index(request):
    # 处理用户对网站根路径的请求
    # request: 包含用户请求信息的对象

    # 使用render函数将index.html模板文件渲染为HTML页面
    # request: 传递请求对象，用于在模板中访问请求相关信息
    # 'index.html': 指定要渲染的模板文件
    # 第三个参数可传递上下文数据，此处为空
    return render(request, 'index.html')