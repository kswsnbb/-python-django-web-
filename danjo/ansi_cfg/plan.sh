#! /bin/bash
#如果python虚拟环境报错，下面脚本建议在终端运行
ansible all -m setup --tree /tmp/myservers/
ansible-cmdb /tmp/myservers/ > ../templates/servers.html
