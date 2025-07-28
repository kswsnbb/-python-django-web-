from django.shortcuts import render,redirect
from webadmin.models import HostGroup,Module,Argument,Host

# 导入主机组模型
# 服务器首页视图函数
def index(request):
    # 直接渲染servers.html模板，不传递额外上下文数据
    return render(request, 'servers.html')
# 添加主机视图函数 - 处理主机添加表单提交和展示
def add_hosts(request):
    # 处理POST请求（表单提交）
    if request.method == 'POST':
        # 从POST数据中获取表单字段并去除空白
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        # 如果主机组名称不为空
        if group:
            # 获取或创建主机组对象（返回元组，[0]表示实际对象）
            g = HostGroup.objects.get_or_create(groupname=group)[0]
            # 如果主机名和IP都不为空
            if host and ip:
                # 在该主机组下获取或创建主机对象（避免重复）
                g.host_set.get_or_create(hostname=host, ip_addr=ip)
    # 查询所有主机组数据（无论POST/GET请求都需要）
    groups = HostGroup.objects.all()
    # 渲染模板并传递主机组数据到模板
    return render(request, 'add_hosts.html', {'groups': groups})


def add_modules(request):
    # 处理添加模块的请求
    if request.method == 'POST':  # 检查请求方法是否为 POST
        module = request.POST.get('module')  # 从 POST 数据中获取模块名称
        param = request.POST.get('param')  # 从 POST 数据中获取参数文本

        if module:  # 如果模块名称不为空
            # 获取或创建一个模块对象，返回的第一个元素是模块实例
            m = Module.objects.get_or_create(modulename=module)[0]
            if param:  # 如果参数不为空
                # 获取或创建该模块的参数，参数文本为 param
                m.argument_set.get_or_create(arg_text=param)

    # 获取所有模块以供展示
    modules = Module.objects.all()
    # 渲染 add_modules.html 模板，并传递模块数据
    return render(request, 'add_modules.html', {'modules': modules})


def del_arg(request, arg_id):
    # 处理删除参数的请求
    arg = Argument.objects.get(id=arg_id)  # 根据参数 ID 获取参数对象
    arg.delete()  # 删除该参数对象
    # 重定向到 add_modules 视图
    return redirect('add_modules')


def tasks(request):
    # 处理任务请求
    if request.method == 'POST':  # 检查请求方法是否为 POST
        server = request.POST.get('server')  # 获取选择的服务器名称
        group = request.POST.get('group')  # 获取选择的主机组名称
        module = request.POST.get('module')  # 获取选择的模块名称
        param = request.POST.get('param')  # 获取选择的参数文本
        target = None  # 初始化目标变量

        # 确定目标（主机组或服务器）
        if group:  # 如果选择了主机组
            target = group  # 设置目标为主机组
        elif server:  # 如果选择了服务器
            target = server  # 设置目标为服务器

        # 如果目标存在且选择了模块和参数
        if target:
            if module and param:
                # 在这里可以执行相应的操作，例如调用 Ansible 等
                return render(request, 'tasks.html')  # 渲染任务模板

    # 获取所有主机、主机组和模块以供展示
    hosts = Host.objects.all()  # 获取所有主机
    groups = HostGroup.objects.all()  # 获取所有主机组
    modules = Module.objects.all()  # 获取所有模块

    # 将数据打包并传递给模板
    data = {'hosts': hosts, 'groups': groups, 'modules': modules}
    # 渲染 tasks.html 模板，传递相应的数据
    return render(request, 'tasks.html', data)
