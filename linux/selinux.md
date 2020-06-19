### Selinux
	SELinux则是由美国NSA（国安局）和一些公司（RedHat、Tresys）设计的一个针对Linux的安全加强系统。
	NSA最初设计的安全模型叫FLASK，全称为Flux Advanced Security Kernel（由Uta大学和美国国防部开发，后来由NSA将其开源），
	当时这套模型针对DTOS系统。后来，NSA觉得Linux更具发展和普及前景，所以就在Linux系统上重新实现了FLASK，称之为SELinux。
	
	SELinux出现之前，Linux上的安全模型叫DAC，全称是Discretionary Access Control（自主访问控制）
	DAC的核心思想很简单，就是：进程理论上所拥有的权限与执行它的用户的权限相同。
	在DAC之外，设计了一个新的安全模型，叫MAC（Mandatory Access Control），翻译为强制访问控制。
	MAC的处世哲学非常简单：即任何进程想在SELinux系统中干任何事情，都必须先在安全策略配置文件中赋予权限。凡是没有出现在安全策略配置文件中的权限，进程就没有该权限。

	关于DAC和MAC:

	Linux系统先做DAC检查。如果没有通过DAC权限检查，则操作直接失败。通过DAC检查之后，再做MAC权限检查。
	SELinux中也有用户的概念，但它和Linux中原有的user概念不是同一个概念。比如，Linux中的超级用户root在SELinux中可能就是一个没权限，没地位，打打酱油的"路人甲"。当然，这一切都由SELinux安全策略的制定者来决定。

### 三种模式
	selinux有3中模式：permissive、enforcing和disabled。
	* enforcing：强制模式，代表 SELinux 运作中，且已经正确的开始限制 domain/type 了；
	* permissive：宽容模式：代表 SELinux 运作中，不过仅会有警告讯息并不会实际限制 domain/type 的存取。这种模式可以运来作为 SELinux 的 debug 之用；
	* disabled：关闭，SELinux 并没有实际运作。
	查看selinux 当前模式
		getenforce              =》 Permissive
		更改当前的SELINUX值 ，后面可以跟 enforcing,permissive 或者 1, 0。
		setenforce enforcing | setenforce permissive
	修改|添加 selinux策略	
		1.1 提取所有的avc LOG. 如 adb shell "cat /proc/kmsg | grep avc" > avc_log.txt
		1.2 使用 audit2allow tool 直接生成policy. audit2allow -i avc_log.txt 即可自动输出生成的policy
		1.3 将对应的policy 添加到selinux policy 规则中，对应MTK Solution, 您可以将它们添加在KK: mediatek/custom/common/sepolicy, L: device/mediatek/common/sepolicy 下面，如
		allow zygote resource_cache_data_file:dir rw_dir_perms;
		allow zygote resource_cache_data_file:file create_file_perms;
		===> mediatek/custom/common/sepolicy/zygote.te (KK)
		===> device/mediatek/common/sepolicy/zygote.te (L)
		注意audit2allow 它自动机械的帮您将LOG 转换成policy, 而无法知道你操作的真实意图，有可能出现权限放大问题。

### 常用命令
	文件操作
		* ls命令 -Z | -context
		* chcon				更改文件的标签
		* restorecon		当这个文件在策略里有定义是，可以恢复原来的 文件标签。
		* setfiles			跟chcon一样可以更改一部分文件的标签，不需要对整个文件系统重新设定标签。
		* fixfiles			一般是对整个文件系统的， 后面一般跟 relabel,对整个系统 relabel后，一般我们都重新启动。
		* star				就是tar在SELinux下的互换命令，能把文件的标签也一起备份起来。
		* find				跟-context查特定的type文件
		* run_init			在sysadm_t里手动启动一些如Apache之类的程序，也可以让它正常进行，domain迁移。
	
	domain确认
		程序现在在那个domain里运行，使用 ps －Z
	
	ROLE的确认和变更
		命令id能用来确认自己的 security context
	
	模式切换
		getenforce		得到当前的SELINUX值
		setenforce		更改当前的SELINUX值 ，后面可以跟 enforcing,permissive 或者 1, 0。
		sestatus		显示当前的 SELinux的信息
	
	其他重要命令
		Audit2allow
			主要用来处理日志，把日志中的违反策略的动作的记录，转换成 access vector，对开发安全策略非常有用。
		checkmodule	
			编译模块
		semodule_package
			创建新的模块
		semodule
			可以显示，加载，删除 模块
		semanage
			这是一个功能强大的策略管理工具，有了它即使没有策略的源代码，也是可以管理安全策略的。
	
	
	
	
	
	
	
	
	
	
	
	