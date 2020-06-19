## 安装apache
	1、安装
		yum install httpd httpd-devel
	2、启动
		systemctl start httpd
	3、设置服务开机启动
		systemctl enable httpd
	4、查看服务状态
		systemctl status httpd
	5、防火墙设置开启80端口
		firewall-cmd --permanent --zone=public  --add-service=http
		firewall-cmd --permanent --zone=public  --add-service=https
		firewall-cmd --reload
	6、确认监听80
		netstat -tulp
	7、查服务器IP
		ip addr
	8、浏览器登录
		ens33..ip  =>Testing 123..
    
## 安装mysql
	1、安装
		yum install mariadb mariadb-server mariadb-libs mariadb-devel
		rpm -qa | grep maria
	2、开启mysql服务，并设置开机启动，检查mysql状态
		systemctl start mariadb
		systemctl enable mariadb
		systemctl status mariadb
		netstat -tulp
	3、数据库安全设置
		mysql_secure_installation
		y enter 设置密码 y n y y
		登录测试  mysql -uroot -p
	  
## 安装 PHP
	1、安装
		yum -y install php
		rpm -ql php
	2、与mysql关联
		yum install php-mysql
		rpm -ql php-mysql
	3、安装常用模块
		yum install -y php-gd php-ldap php-odbc php-pear php-xml php-xmlrpc php-mbstring php-snmp php-soap curl curl-devel php-bcmath
	4、测试
		phpinfo()
		systemctl restart httpd
		
		
		
