#### 验证器
	php think make:validate index/User
	
	protected $rule = [
		'name' => 'require|max:25',
		'age' => 'number|between:1,120',
		'email' => 'email',
	];
	
	protected $message  =   [
        'name.require' => '名称必须',
        'name.max'     => '名称最多不能超过25个字符',
        'age.number'   => '年龄必须是数字',
        'age.between'  => '年龄只能在1-120之间',
        'email'        => '邮箱格式错误',    
    ];
	
	数据验证
		控制器中
		$data = [
            'name'  => 'thinkphp',
            'email' => 'thinkphp@qq.com',
        ];

        $validate = new \app\index\validate\User;

        if (!$validate->check($data)) {
            dump($validate->getError());
        }
		
		or
		$result = $this->validate(
			[
				'name'  => 'thinkphp',
				'email' => 'thinkphp@qq.com',
			],
		'app\index\validate\User');

	
#### 缓存
	ThinkPHP采用think\Cache类（实际使用think\facade\Cache类即可）提供缓存功能支持。
	内置支持的缓存类型包括file、memcache、wincache、sqlite、redis和xcache。
		参数名		描述
		type		缓存类型或者缓存驱动类名
		expire		缓存有效期（秒）
		prefix		缓存标识前缀
		serialize  （非标量）是否需要自动序列化
	- 设置缓存	
		Cache::set('name',$value,3600);
		缓存自增
			Cache::inc('name',3);
	- 获取缓存
		dump(Cache::get('name')); 
	- 删除缓存	
		Cache::rm('name'); 
	- 获取并删除缓存
		Cache::pull('name'); 
	- 清空缓存
		Cache::clear(); 
	- 不存在则写入缓存数据后返回
		Cache::remember('name',function(){
			return time();
		});
	
	- 助手函数
		cache($options);
		// 设置缓存数据
		cache('name', $value, 3600);
		// 获取缓存数据
		var_dump(cache('name'));
		// 删除缓存数据
		cache('name', NULL);
			
	
	
#### Session | Cookie
	助手函数
		session([
			'prefix'     => 'module',
			'type'       => '',
			'auto_start' => true,
		]);

		// 赋值（当前作用域）
		session('name', 'thinkphp');

		// 赋值think作用域
		session('name', 'thinkphp', 'think');

		// 判断（当前作用域）是否赋值
		session('?name');

		// 取值（当前作用域）
		session('name');

		// 取值think作用域
		session('name', '', 'think');

		// 删除（当前作用域）
		session('name', null);

		// 清除session（当前作用域）
		session(null);

		// 清除think作用域
		session(null, 'think');
			
		// 初始化
		cookie(['prefix' => 'think_', 'expire' => 3600]);

		// 设置
		cookie('name', 'value', 3600);

		// 获取
		echo cookie('name');

		// 删除
		cookie('name', null);

		// 清除
		cookie(null, 'think_');

	

	
#### 命令行
	- 启动内置服务器
		php think run 
	- 查看版本
		php think version
	- 自动生成目录结构
		生成一个test模块的指令
			php think build --module test
		自动生成的模块目录包含了config、controller、model和view目录以及common.php公共文件。	
	
	- 创建类库文件	
		快速生成控制器
			php think make:controller index/Blog  
			--plain  仅仅生成空的控制器
		快速生成模型
			php think make:model index/Blog
		快速生成中间件	
			php think make:middleware Auth
		创建验证器类
			php think make:validate index/User
	
	- 生成类库映射文件
		生成类库映射文件，提高系统自动加载的性能
		php think optimize:autoload
		指令执行成功后，会在runtime目录下面生成classmap.php文件，生成的类库映射文件会扫描系统目录和应用目录的类库。
	
	- 清除缓存文件clear
			php think clear
		清除日志目录
			php think clear --log
		清除日志目录并删除空目录
			php think clear --log --dir
		清除数据缓存目录
			php think clear --cache
		清除数据缓存目录并删除空目录
			php think clear --cache --dir

	- 生成配置缓存
		php think optimize:config
		调用后会在runtime目录下面生成init.php文件，生成配置缓存文件后，应用目录下面的config.phpcommon.php以及tags.php不会被加载，被runtime/init.php取代。
		如果需要生成某个模块的配置缓存，可以使用：
			php think optimize:config index

	- 路由
		生成路由列表
			php think route:list 
			同时会在runtime目录下面生成一个route_list.php的文件，内容和上面的输出结果一致，方便你随时查看
			(box|box double|markdown|-s rule |-s method | list -m)  样式和排序
	
	- 单元测试
		composer require topthink/think-testing=2.0.*
		php think unit
	
	
	
#### 安全
	- 输入安全
	    设置public目录为唯一对外访问目录，不要把资源文件放入应用目录；
		开启表单令牌验证避免数据的重复提交，能起到CSRF防御作用；
		使用框架提供的请求变量获取方法（Request类param方法及input助手函数）而不是原生系统变量获取用户输入数据；
		对不同的应用需求设置default_filter过滤规则（默认没有任何过滤规则），常见的安全过滤函数包括stripslashes、htmlentities、htmlspecialchars和strip_tags等，请根据业务场景选择最合适的过滤方法；
		使用验证类对业务数据设置必要的验证规则；
		如果可能开启强制路由或者设置MISS路由规则，严格规范每个URL请求；
	
	- 数据库安全
		尽量少使用字符串查询条件，如果不得已的情况下 使用手动参数绑定功能；
		不要让用户输入决定要查询或者写入的字段；
		不要让用户输入决定你的字段排序；
		对于敏感数据在输出的时候使用hidden方法进行隐藏；
		对于数据的写入操作应当做好权限检查工作；
		写入数据严格使用field方法限制写入字段；
		对于需要输出到页面的数据做好必要的XSS过滤；
		
	- 其他建议
	    对所有公共的操作方法做必要的安全检查，防止用户通过URL直接调用；
		不要缓存需要用户认证的页面；
		对用户的上传文件，做必要的安全检查，例如上传路径和非法格式；
		对于项目进行充分的测试，不要生成业务逻辑的安全隐患（这可能是最大的安全问题）；
		最后一点，做好服务器的安全防护，安全问题的关键其实是找到你的最薄弱环节；
	
	- 架构及开发过程优化建议：
		路由尽量使用域名路由或者路由分组；
		在路由中进行验证和权限判断；
		合理规划数据表字段类型及索引；
		结合业务逻辑使用数据缓存，减少数据库压力；
		
	- 在应用完成部署之后，建议对应用进行相关优化，包括：
		如果开发过程中开启了调试模式的话，关闭调试模式（参考调试模式）；
		通过命令行生成类库映射文件；
		通过命令行生成配置缓存文件；
		生成数据表字段缓存文件；
	
	
	
#### 助手函数
		助手函数				描述
		abort				中断执行并发送HTTP状态码
		action				调用控制器类的操作
		app					快速获取容器中的实例 支持依赖注入
		behavior			执行某个行为
		bind				快速绑定对象实例
		cache				缓存管理
		call				调用反射执行callable 支持依赖注入
		class_basename		获取类名(不包含命名空间)
		class_uses_recursive	获取一个类里所有用到的trait
		config				获取和设置配置参数
		container			获取容器对象实例
		controller			实例化控制器
		cookie				Cookie管理
		db					实例化数据库类
		debug				调试时间和内存占用
		dump				浏览器友好的变量输出
		env					获取环境变量（V5.1.3+）
		exception			抛出异常处理
		halt				变量调试输出并中断执行
		input				获取输入数据 支持默认值和过滤
		json				JSON数据输出
		jsonp				JSONP数据输出
		lang				获取语言变量值
		model				实例化Model
		parse_name			字符串命名风格转换
		redirect			重定向输出
		request				实例化Request对象
		response			实例化Response对象
		route				注册路由规则（V5.1.3+）
		session				Session管理
		token				生成表单令牌输出
		trace				记录日志信息
		trait_uses_recursive	获取一个trait里所有引用到的trait
		url	Url生成
		validate			实例化验证器
		view				渲染模板输出
		widget				渲染输出Widget
		xml	XML				数据输出
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	