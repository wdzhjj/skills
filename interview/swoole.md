#swoole
		swoole是运行在PHP下的一个extesion扩展，实际上与普通的扩展不同。	
		普通的扩展只是提供一个库函数。而swoole扩展在运行后会接管PHP的控制权，进入事件循环。当IO事件发生后，swoole会自动回调指定的PHP函数。
	
	
##包含模块
		swoole_server
			TCP/UDP Server框架，多线程,EventLoop,事件驱动，异步，Worker进程组，Task异步任务，毫秒定时器，SSL/TLS隧道加密
			* swoole_http_server 是 swoole_server的子类，内置了Http的支持
			* swoole_websocket_server 也是子类，内置了WebSocket的支持
		
		swoole_client 
			TCP/UDP客户端，支持同步并发调用，也支持异步事件驱动
	
		swoole_event
			EventLoop API,让用户可以直接操作底层的时间循环，将socket，stream，管道等linux文件加入到时间循环中
			
		swoole_async
			异步IO接口，提供了异步文件系统IO，异步DNS查询，异步MYSQL等API，包括2个重要子模块：
			*swoole_timer 异步秒表定时器，可以时间间隔时间或一次性的定时任务
			*file，文件体统操作的异步接口
		
		swoole_process
			进程管理模块，可以方便的创建子进程，进程间通信，进程管理
		
		swoole_buffer
			强大的内存区管理工具，像C一样进行指针计算，又无需关心内存的申请和释放，不用担心内存越界
			
		swoole_table
			基于共享内存和自旋锁实现的超高性能内存表。解决线程，进程间数据共享，枷锁同步等问题。
	
	
	
	
##Swoole 编程须知	
		
		*不要在代码中执行sleep 已经其他的睡眠函数，这样会导致整个进程堵塞
		*exit/die很危险，会导致worker进程退出
		*可以通过 register_shutdown_function 来捕获致命错误，在进程异常退出时做一些请求工作
		*PHP代码中如果有异常抛出，必须在回调函数中进行 try/catch捕获异常，否则会导致工作进程退出
		*swoole 不支持 set_exception_handler 必须使用 try/catch方式处理异常
		*Worker进程不得公用同一个Redis或MySQL 等网络服务客户端，REDIS/MYSQL创建连接的相关代码可以
		 放到onWorkerStart回调函数中。
	
	
##Swoole 优化内核参数
		ulimit
			ulimit -n 要调整为100000甚至更大。命令行下执行 ulimit -n 100000 即可修改
		
		内核设置
			net.unix.max_dgram_qlen = 100
				swoole使用unix socket dgram 来做进程间通信，如果请求量很大，需要调整此参数。系统默认为10
				可以设置为100 or more。 或者增加worker进程的数量，减少单个worker进程分配的请求量
			
			net.core.wmem_max
				修改此参数增加socket缓存区的内存大小
			
			net.ipv4.tcp_tw_reuse
				是否socket reuse，此函数的作用是Server重启时可以快速重新使用监听的端口。如果没有设置此参数，
				会导致server重启时发生端口未及时释放而启动失败
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	