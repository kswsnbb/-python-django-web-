import shutil  # 导入 shutil 模块，用于处理文件和目录的高阶操作
from collections import namedtuple  # 导入 namedtuple，用于创建命名元组
from ansible.parsing.dataloader import DataLoader  # 导入 DataLoader，用于加载 Ansible 数据
from ansible.vars.manager import VariableManager  # 导入 VariableManager，用于管理变量
from ansible.inventory.manager import InventoryManager  # 导入 InventoryManager，用于管理清单
from ansible.playbook.play import Play  # 导入 Play，用于创建 Ansible Play
from ansible.executor.task_queue_manager import TaskQueueManager  # 导入 TaskQueueManager，用于管理任务队列
import ansible.constants as C  # 导入 Ansible 常量，用于获取默认值


def adhoc(sources, hosts, module, args):
    # 定义一个名为 Options 的命名元组，用于存储 Ansible 选项
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                          'diff'])

    # 创建 Options 实例，设置 Ansible 运行时的选项
    options = Options(
        connection='smart',  # 连接类型
        module_path=['/to/mymodules'],  # 模块路径
        forks=10,  # 最大并发执行的任务数
        become=None,  # 提升权限选项
        become_method=None,  # 提升权限的方法
        become_user=None,  # 提升权限的用户
        check=None,  # 检查模式
        diff=False  # 是否显示差异
    )

    # 创建 DataLoader 实例，用于加载 Ansible 数据
    loader = DataLoader()
    # 定义密码字典，这里用作 Vault 密码
    passwords = dict(vault_pass='secret')

    # 创建 InventoryManager 实例，用于管理清单
    inventory = InventoryManager(loader=loader, sources=sources)

    # 创建 VariableManager 实例，用于管理变量
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # 定义要执行的 Play 的源字典
    play_source = dict(
        name='Ansible Play',  # Play 的名称
        hosts=hosts,  # 要执行的主机组
        gather_facts='no',  # 不收集事实信息
        tasks=[  # 任务列表
            dict(action=dict(module=module, args=args), register='shell_out'),  # 执行指定模块的任务
        ]
    )

    # 加载 Play，使用 variable_manager 和 loader
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    tqm = None  # 初始化任务队列管理器
    try:
        # 创建 TaskQueueManager 实例，用于管理任务的执行
        tqm = TaskQueueManager(
            inventory=inventory,  # 清单
            variable_manager=variable_manager,  # 变量管理器
            loader=loader,  # 数据加载器
            options=options,  # 运行时选项
            passwords=passwords,  # 密码字典
        )
        # 运行 Play
        result = tqm.run(play)
    finally:
        # 清理任务队列管理器和临时文件
        if tqm is not None:
            tqm.cleanup()  # 清理资源
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)  # 删除 Ansible 默认的临时目录
if __name__ == '__main__':
    # 主程序入口
    sources = ['myansible/hosts']  # 清单文件路径
    hosts = 'dbservers'  # 目标主机组
    module = 'shell'  # 要执行的 Ansible 模块
    args = 'id root'  # 传递给模块的参数
    adhoc(sources, hosts, module, args)  # 调用 adhoc 函数
