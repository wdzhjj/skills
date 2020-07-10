### CentOS7 安装LNMP流程

#### CentOS7 安装
		选择安装,选择时区，创建root密码，重启。
		使用root登录，输入密码。
		ping 一个网址=>
		修改网卡
			vi /etc/sysconfig/network-scripts/ifcfg-enp (自动补全)
			ONBOOT=no
			修改为 ONBOOT=yes
			
			BOOTPROTO=dhcp
			修改为静态地址
				BOOTPROTO=static
				IPADDR=192.168.1.150
				NETMASK=255.255.255.0
				NM_CONTROLLED=no
			保存后 重启网络服务
				systemctl restart network.service
			使用 ip addr  或者 ifconfig 查看网络状态	
			
		远程链接登录此机器=》操作防火墙
			firewall-cmd --zone=public --add-port=2/tcp --permanent
			systemctl restart firewalld.service	
		
		=>虚拟机设置网络
		=>桥接网卡 重启
		
		如果网站无法访问 
		模式切换
		getenforce		得到当前的SELINUX值
		setenforce		更改当前的SELINUX值 ，后面可以跟 enforcing,permissive 或者 1, 0。
		sestatus		显示当前的 SELinux的信息
		如果网站无法访问 setenforce 设为0

                yum -y install net-tools
		yum install firewall
		yum install openssh-server


#### CentOS7使用firewalld打开关闭防火墙与端口
		1、firewalld的基本使用
		启动： systemctl start firewalld
		关闭： systemctl stop firewalld
		查看状态： systemctl status firewalld 
		开机禁用  ： systemctl disable firewalld
		开机启用  ： systemctl enable firewalld
		 
		 
		2.systemctl是CentOS7的服务管理工具中主要的工具，它融合之前service和chkconfig的功能于一体。

		启动一个服务：systemctl start firewalld.service
		关闭一个服务：systemctl stop firewalld.service
		重启一个服务：systemctl restart firewalld.service
		显示一个服务的状态：systemctl status firewalld.service
		在开机时启用一个服务：systemctl enable firewalld.service
		在开机时禁用一个服务：systemctl disable firewalld.service
		查看服务是否开机启动：systemctl is-enabled firewalld.service
		查看已启动的服务列表：systemctl list-unit-files|grep enabled
		查看启动失败的服务列表：systemctl --failed

		3.配置firewalld-cmd
		查看版本： firewall-cmd --version
		查看帮助： firewall-cmd --help
		显示状态： firewall-cmd --state
		查看所有打开的端口： firewall-cmd --zone=public --list-ports
		更新防火墙规则： firewall-cmd --reload
		查看区域信息:  firewall-cmd --get-active-zones
		查看指定接口所属区域： firewall-cmd --get-zone-of-interface=eth0
		拒绝所有包：firewall-cmd --panic-on
		取消拒绝状态： firewall-cmd --panic-off
		查看是否拒绝： firewall-cmd --query-panic
		 
		那怎么开启一个端口呢
		添加
		firewall-cmd --zone=public --add-port=80/tcp --permanent    （--permanent永久生效，没有此参数重启后失效）
		重新载入
		firewall-cmd --reload
		查看
		firewall-cmd --zone= public --query-port=80/tcp
		删除
		firewall-cmd --zone= public --remove-port=80/tcp --permanent
		
#### centos7 搭建ftp
		yum -y install vsftpd   安装
		alias stl = 'systemctl'
		stl start vsftpd.service  启动
		ps =ef | grep vsftpd     查看进程
		
		firewall-cmd --zone=public --add-port=21/tcp --permanent    # 添加 21 端口
		firewall-cmd --reload        # 重新载入
		firewall-cmd --zone=public --list-ports    # 查看所有已开放的端口



















		
