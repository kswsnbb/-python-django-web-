#!/root/PycharmProjects/pythonProject/venv/bin/python  # 指定 Python 解释器的路径
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey  # 导入 SQLAlchemy 中所需的类和方法
from sqlalchemy.orm import sessionmaker, declarative_base  # 导入会话生成器和声明基类
from sqlalchemy.ext.declarative import declarative_base  # 导入用于声明模型的基类
import json  # 导入 JSON 处理模块
# 创建数据库引擎，连接到 MySQL 数据库
engine = create_engine(
    'mysql+pymysql://root:%40WSLnb2004823@127.0.0.1/myansible?charset=utf8'
)
# 创建一个会话生成器，用于与数据库交互
Session = sessionmaker(bind=engine)
# 创建一个基类，用于模型声明
Base = declarative_base()
# 定义 HostGroup 模型类，映射到 'webadmin_hostgroup' 表
class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'  # 指定表名
    id = Column(Integer, primary_key=True)  # 主键字段
    groupname = Column(String(50))  # 主机组名称字段
# 定义 Host 模型类，映射到 'webadmin_host' 表
class Host(Base):
    __tablename__ = 'webadmin_host'  # 指定表名
    id = Column(Integer, primary_key=True)  # 主键字段
    hostname = Column(String(50))  # 主机名称字段
    ip_addr = Column(String(15))  # 主机 IP 地址字段
    group_id = Column(Integer, ForeignKey('webadmin_hostgroup.id'))  # 外键，关联到 HostGroup 的 id
if __name__ == '__main__':  # 确保该代码块在直接运行时执行
    session = Session()  # 创建数据库会话
    # 查询 HostGroup 和 Host 表，获取主机组名称和对应的 IP 地址
    qset = session.query(HostGroup.groupname, Host.ip_addr).join(Host)
    result = {}  # 初始化结果字典
    for g, ip in qset:  # 遍历查询结果
        if g not in result:  # 如果主机组名称不在结果字典中
            result[g] = {}  # 创建新的字典条目
            result[g]['hosts'] = []  # 初始化 'hosts' 列表
        result[g]['hosts'].append(ip)  # 将 IP 地址添加到对应主机组的 'hosts' 列表中
    print(json.dumps(result))  # 将结果字典转换为 JSON 格式并打印
