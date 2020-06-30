#### PHP7 增加
		1、类型的声明
			可以使用字符串(string), 整数 (int), 浮点数 (float), 以及布尔值 (bool)，来声明函数的参数类型与函数返回值。
				declare(strict_types=1);
				function add(int $a, int $b): int {
					return $a+$b;
				}
				echo add(1, 2);
				echo add(1.5, 2.6);
			php5是无法执行上面代码的，php7执行的时候会先输出一个3和一个报错( Argument 1 passed to add() must be of the type integer, float given);
			标量类型声明 有两种模式: 强制 (默认) 和 严格模式。
			declare(strict_types=1),必须放在文件的第一行执行代码，当前文件有效！	
		2、	.set_exception_handler() 不再保证收到的一定是 Exception 对象
				在 PHP 7 中，很多致命错误以及可恢复的致命错误，都被转换为异常来处理了。 这些异常继承自 Error 类，此类实现了 Throwable 接口 （所有异常都实现了这个基础接口）。
				PHP7进一步方便开发者处理, 让开发者对程序的掌控能力更强. 因为在默认情况下, Error会直接导致程序中断, 而PHP7则提供捕获并且处理的能力, 让程序继续执行下去,
		3、 新增操作符“<=>”
				语法：$c = $a <=> $b
				如果$a > $b, $c 的值为1
				如果$a == $b, $c 的值为0
				如果$a < $b, $c 的值为-1
		4、 新增操作符“??”		
				如果变量存在且值不为NULL， 它就会返回自身的值，否则返回它的第二个操作数。
				//原写法
				$username = isset($_GET['user]) ? $_GET['user] : 'nobody';
				//现在
				$username = $_GET['user'] ?? 'nobody';
		5、 define() 定义常量数组
				define('ARR',['a','b']);
				echo ARR[1];// a		
		6、 AST: Abstract Syntax Tree, 抽象语法树
				AST在PHP编译过程作为一个中间件的角色, 替换原来直接从解释器吐出opcode的方式, 让解释器(parser)和编译器(compliler)解耦, 可以减少一些Hack代码, 同时, 让实现更容易理解和可维护.

				PHP5 : PHP代码 -> Parser语法解析 -> OPCODE -> 执行
				PHP7 : PHP代码 -> Parser语法解析 -> AST -> OPCODE -> 执行 
		7、 匿名函数
				$anonymous_func = function(){return 'function';};
				echo $anonymous_func(); // 输出function
		8、 Unicode字符格式支持(echo “\u{9999}”)
		9、 Unserialize 提供过滤特性
				防止非法数据进行代码注入,提供了更安全的反序列化数据。
		10、命名空间引用优化
				// PHP7以前语法的写法 
				use FooLibrary\Bar\Baz\ClassA; 
				use FooLibrary\Bar\Baz\ClassB; 
				// PHP7新语法写法 
				use FooLibrary\Bar\Baz\{ ClassA, ClassB};

				

#### PHP7 废弃
		1、废弃扩展
			Ereg 正则表达式
			mssql
			mysql
			sybase_ct
		2、	废弃的特性
				不能使用同名的构造函数
				实例方法不能用静态方法的方式调用
		3、 废弃的函数
			    方法调用
				call_user_method()
				call_user_method_array()
				应该采用call_user_func() 和 call_user_func_array()

				加密相关函数
					mcrypt_generic_end()
					mcrypt_ecb()
					mcrypt_cbc()
					mcrypt_cfb()
					mcrypt_ofb()
					注意: PHP7.1 以后mcrypt_*序列函数都将被移除。推荐使用：openssl 序列函数

				杂项
					set_magic_quotes_runtime
					set_socket_blocking
					Split
					imagepsbbox()
					imagepsencodefont()
					imagepsextendfont()
					imagepsfreefont()
					imagepsloadfont()
					imagepsslantfont()
					imagepstext()
					
		4、 废弃的用法
				$HTTP_RAW_POST_DATA 变量被移除, 使用php://input来代
				ini文件里面不再支持#开头的注释, 使用”;”
				移除了ASP格式的支持和脚本语法的支持: <% 和 < script language=php >
		
		
#### php7 变更
		1、字符串处理机制的修改
			含有十六进制字符的字符串不再视为数字, 也不再区别对待.
			var_dump("0x123" == "291"); // false
			var_dump(is_numeric("0x123")); // false
			var_dump("0xe" + "0x1"); // 0
			var_dump(substr("f00", "0x1")) // foo
		2、 整型处理机制修改	
				Int64支持, 统一不同平台下的整型长度, 字符串和文件上传都支持大于2GB. 64位PHP7字符串长度可以超过2^31次方字节.
		3、参数处理机制修改
				不支持重复参数命名
		4、 foreach修改
				foreach()循环对数组内部指针不再起作用
				按照值进行循环的时候, foreach是对该数组的拷贝操作
		5、 list修改
				不再按照相反的顺序赋值
				不再支持字符串拆分功能
				空的list()赋值不再允许
				list()现在也适用于数组对象
		6、 变量处理机制修改
		7、 其他
			1.debug_zval_dump() 现在打印 “int” 替代 “long”, 打印 “float” 替代 “double”
			2.dirname() 增加了可选的第二个参数, depth, 获取当前目录向上 depth 级父目录的名称。
			3.getrusage() 现在支持 Windows.mktime() and gmmktime() 函数不再接受 is_dst 参数。
			4.preg_replace() 函数不再支持 “\e” (PREG_REPLACE_EVAL). 应当使用 preg_replace_callback() 替代。
			5.setlocale() 函数不再接受 category 传入字符串。 应当使用 LC_* 常量。
			6.exec(), system() and passthru() 函数对 NULL 增加了保护.
			7.shmop_open() 现在返回一个资源而非一个int， 这个资源可以传给shmop_size(), shmop_write(), shmop_read(), shmop_close() 和 shmop_delete().
			8.为了避免内存泄露，xml_set_object() 现在在执行结束时需要手动清除 $parse。
			9.curl_setopt 设置项CURLOPT_SAFE_UPLOAD变更

			TRUE 禁用 @ 前缀在 CURLOPT_POSTFIELDS 中发送文件。 意味着 @ 可以在字段中安全得使用了。 可使用 CURLFile作为上传的代替。
			PHP 5.5.0 中添加，默认值 FALSE。 PHP 5.6.0 改默认值为 TRUE。. PHP 7 删除了此选项， 必须使用 CURLFile interface 来上传文件。


#### 如果发挥 PHP7性能
		1、 开启Opcache
				zend_extension=opcache.so
				opcache.enable=1
				opcache.enable_cli=1
		2、 使用GCC 4.8以上进行编译
				只有GCC 4.8以上PHP才会开启Global Register for opline and execute_data支持, 这个会带来5%左右的性能提升(Wordpres的QPS角度衡量)
		3、开启HugePage （根据系统内存决定）
				sudo sysctl vm.nr_hugepages=512
				php.ini中加入   opcache.huge_code_pages=1
		4、PGO (Profile Guided Optimization）		
			第一次编译成功后，用项目代码去训练PHP，会产生一些profile信息，最后根据这些信息第二次gcc编译PHP就可以得到量身定做的PHP7
			需要选择在你要优化的场景中: 访问量最大的, 耗时最多的, 资源消耗最重的一个页面.



## output_buffering
#### buffer
		是一个内存地址空间，Linux系统默认大小一般为4096(4kb),即一个内存页
		主要用于存储速度不同步的设备或者优先级不同的设备之间传办理数据的区域。
		通过buffer，可以使进程这间的相互等待变少
		
		php output_buffering机制，意味在tcp buffer之前，建立了一新的队列，数据必须经过该队列
		当一个php buffer写满的时候，脚本进程会将php buffer中的输出数据交给系统内核交由tcp传给浏览器显示。
		所以，数据会依次写到这几个地方：echo/print -> php buffer -> tcp buffer -> browser

#### php output_buffering
		php buffer是开启的，而且该buffer默认值是4096，即4kb。
		通过在php.ini配置文件中找到output_buffering配置.当echo,print等输出用户数据的时候，输出数据都会写入到php output_buffering中，
		直到output_buffering写满，会将这些数据通过tcp传送给浏览器显示。
		也可以通过ob_start()手动激活php output_buffering机制，使得即便输出超过了4kb数据，也不真的把数据交给tcp传给浏览器，因为ob_start()将php buffer空间设置到了足够大。
		只有直到脚本结束，或者调用ob_end_flush函数，才会把数据发送给客户端浏览器。
	
#### output buffering函数
		ob_get_level
			返回输出缓冲机制的嵌套级别，可以防止模板重复嵌套自己。
		ob_start	
			激活output_buffering机制。一旦激活，脚本输出不再直接出给浏览器，而是先暂时写入php buffer内存区域。
			php默认开启output_buffering机制，只不过，通过调用ob_start()函数据output_buffering值扩展到足够大
		ob_get_contents
			获取一份php buffer中的数据拷贝。值得注意的是，你应该在ob_end_clean()函数调用之前调用该函数，否则ob_get_contents()返回一个空字符中。
		ob_end_flush与ob_end_clean	
			这二个函数有点相似，都会关闭ouptu_buffering机制
			但不同的是，ob_end_flush只是把php buffer中的数据冲(flush/send)到客户端浏览器，而ob_clean_clean将php bufeer中的数据清空(erase)，但不发送给客户端浏览器。
			ob_end_flush调用之后，php buffer中的数据依然存在，ob_get_contents()依然可以获取php buffer中的数据拷贝。
			而ob_end_clean()调用之后ob_get_contents()取到的是空字符串，同时浏览器也接收不到输出，即没有任何输出。



				
				
				
				
				