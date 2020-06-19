# LARAVEL

## 一、Composer

		组件管理工具

		1、linux 安装composer
			apt-get install update    更新系统的软件列表
			apt-get install php 	  安装php环境
			composer需要PHP版本在5.4以上
			apt-get install curl 	  安装curl工具
		=>安装后
			1) curl -sS https://getcomposer.org/installer | php
			2) php -r "readfile('https://getcomposer.org/installer');" | php
			
		2、composer命令行
			
			composer list           获取帮助信息
			composer init           以交互方式填写composer.json文件信息
			composer install		从当前目录地区composer.json文件，处理依赖关系，并安装到verdor目录下
			composer update         获取依赖的最新版本，升级composer.lock文件
			composer require        添加新的依赖包到composer.json文件中并执行更新 
			composer search  		在当前项目中搜索依赖包
			composer show           列举所有可用的资源包
			composer validate       检测compser.json文件是否有效
			composer self-update    将composer工具更新到最新版本
			composer create-project 基于composer穿件一个新的项目
			composer dump-autoload  在添加新的类和项目映射时更新autoloader
	
## 二、构建laravel框架
		web目录创建文件夹作为网站的根目录、
		根目录创建一个composer.json文件
		{
			"require":{
			
			}
		}
		
		添加路由组件
		"require":{
			"illuminate/routing":"*",
			"illuminate/events":"*"
		}
		=>执行 composer update  完成2个组件及其依赖组的下载
		添加控制器模块
		"autoload":{
			"App\\":"app/"
		}
		添加模型组件
		"require":{
			"illuminate/database":"*"
		}
		
		添加视图组件
			"illmuinate/view":"*"
			
			
		
## 三、LARAVEL框架中常用的php语法
		1、命名空间
			最初设计是为了解决命名冲突而产生的一种包装类、函数、和常量方法
			为组件化开发提供了可能。使用某个组件的文件的路径和命名空间具有一定的关系。最终可以通过
			命名空间找到相应的文件
			定义
			namespace App\Http;
			使用
			use Ill\Http\kernel as HttpKernel;
			
		. php命名空间只支持导入类，而不支持导入函数和常量
		
		2、文件包含
			include 和 require
			用于包含并运行指定文件，两者作用一样，处理失败的方式不同
			reuqire出错时产生E_COMPILE_ERROR 会导致脚本程序运行终止
			include出错时 产生E_WARNING 只会发出警告 程序继续运行
		
		3、类的自动加载
			通过魔术方法 
			function __autoload($class){
				require_once($class.".php");
			}
			
			当使用一个类名时，如果该类没有被当前文件包含，则会自动调用魔术方法
			
			spl_autoload_register可以将多个类自动加载方法注册到队列中
			public function register($prepend = false){
				spl_autoload_register(array($this,'loadClass'),true,$prepend);
			}
		
		4、laravel中的实现方案
			laravel框架中  通过 spl_autoload_register() 实现类的自动加载函数注册
			类的自动加载函数队列中包含了两个雷的自动加载函数
			一个是composer生成的基于PSR规范的自动加载函数，
			另一个是laravel框架核心别名的自动加载函数

			

### 匿名函数
		也叫闭包函数，即一个没有指定名称的函数，经常用作回调函数callback参数的值
		闭包类也成匿名函数类，匿名函数本身就是这个类型的对象
		laravel中大量的使用了匿名函数
	
	
### php中的特殊语法
		1、魔术方法
			通常情况下不会主动调用，而是在特定的时机被PHP系统自动调用。可以理解为系统
			事件监听方法，在事件发生时才出发执行。
			
			__construct()	  构造函数 实例化对象时调用 使用对象前的初始化操作
			__destruct()	  某个对象的所有引用都被删除或者对象被销毁时执行
			__set()			  用于属性重载，在给不可访问的属性赋值时调用
			__get()			  读取不可访问的属性的值时调用
			__isset()		  对不可访问属性调用isset 或 empty 时调用
			__unset()		  对不可访问属性调用unset 时调用
			__sleep()		  serialize 检查类中时候有sleep。如果存在，该函数将在任何序列化之前
							  运行。 可以清楚对象并返回一个包含有该对象中应被序列化的所有变量名的数组
			__wakeup()		  unserialize....
			__toString()      对象被当做字符串使用时调用
			__invoke()        尝试以调用函数的方法调用一个对象时自动调用 $obj();
			__clone()		  新创建对象|复制生成对象时被调用，可以用于修改属性的值
			__call()		  调用一个不可方位的方法时调用
			__callStatic()    静态方式中调用一个不可访问的方法时自动调用
			__autoload() 	  在视图使用尚未被定义的类时自动调用
			
		2、魔术常量
			__LINE__            显示当前的行号
			__FILE__			文件的完整路径和文件名
			__DIR__				文件所在的目录
			__FUNCTION__		方法名
			__CLASS__			类的名称
			__TRAIT__			trait的名字
			__METHOD__			类的方法名
			__NAMESPACE__	   返回当前的命名空间被区分大小写
	
		3、反射
			主要用来动态的获取系统中类，实例对象，方法等语言构建的信息。通过反射API函数可以实现对这些
			语言构建信息的动态获取和动态操作等。
			laravel的服务容器解析服务的过程就用到了反射机制
			
		4、后期静态绑定
			在类的继承过程中，使用的类不再是当前类，而是调用的类
			后期静态绑定使用关键字static来实现
			通过这种机制 static::不再被解析为定义当前方法所在的类，而是在实际运行时计算得到的，即为运行时最初
			调用的类
	
		5、trait
			一个trait与一个类相似，但trait不能像类一样进行实例化，而是通过关键字use添加到其他类的内部
			从而发挥它的作用
			重要性质
				*优先级
					当前类的方法会覆盖trait中的方法，而trait中的方法会覆盖基类的方法
				*多个trait组合
					通过逗号分隔，通过use关键字列出多个trait
				*解决冲突
					两个trait插入了一个同名的方法，若没有明确解决冲突会产生 一个致命的错误
					需要使用 insteadof 操作符来明确指定冲突方法中的哪一个。
				*修改方法的访问孔子
					使用as语法可以用来吊证方法的访问控制
				*trait抽象方法
					在trait中可以使用抽象成员，使得类中必须实现这个抽象方法
				*trait静态成员
					在trait中可以用静态方法和静态变量
				*trait属性定义
					在trait中同样可以定义属性
						
	
### LARAVEL框架中使用的HTTP协议
		http 协议工作流程
		1) 客户端与服务器需要建立连接，如TCP连接
		2) 连接建立后，客户端想服务器发送一个请求，请求报文由三部分组成：请求行，消息报头，请求内容
		3) 服务器接受到请求后，解析该请求并返回相应信息，响应报文：状态行，消息报头，响应内容
		4) 客户端接收服务器所返回的信息并进行解析，处理和显示
				

## 四、LARAVEL框架应用程序目录结构
		1、根目录
			app:主要包含应用程序的核心代码，用户构建应用的大部分工作都在此目录下进行，包括
				路由文件、控制器文件、模型文件等。
			bootstrap:主要包含几个框架启动和自动加载配置的文件
			config：包含应用程序常用的配置文件信息
			database:包含数据库迁移和数据填充文件
			public：为应用程序的入口目录，包含应用程序入口文件index.php，同时包含静态文件如
					CSS,JS,Images等
			resources：主要包含视图文件
			storage：包含编译后的Blade模板，基于文件的session，文件的缓存和日志等文件
			tests：主要包含自动化测试文件
			vendor:主要包含依赖库文件，其中包括Laravel框架源代码
			.env文件：一个重要的文件，为Laravel框架主配置文件
			composer.json：composer项目依赖管理文件
		
		2、app目录
			Console:主要包含所有的artisan命令
			Events：用来放置与事件相关的类
			Exceptions：包含应用程序的异常处理类，用户处理应用程序抛出的任何异常
			Http:主要包含路由文件、控制器文件、请求文件、中间文件、是应用程序与laravel框架源代码等外部库
				 交互的主要地方
			Jobs：主要包含消息队列的各种消息类文件
			listeners:主要好汉监听实践类文件
			Providers：主要包含服务提供者的相关文件
		app目录下可以放置模型类的文件，用于操作数据，如默认的users.php
	
		3、vendor目录
			主要包含laravel应用程序的外部依赖库，包括laravel框架源代码部分
			该目录文件的组织结构是根据依赖关系决定的，每一个文件夹都是一个功能模块
			可以单独通过composer下载该组件进行使用，laravel框架这样的大组件下还会有许多小组件
			
			composer：主要包含composer按照PSR规范生产的自动加载类。应用程序类的自动加载都是这部分实现的
			laravel：包含laravel框架源代码，代码部分都包含在vendor\laravel\framework\src\Illuminate文件夹下
					 该文件夹下包含很多文件夹，每一个文件夹又是一个组件，组件是独立工作的
			symfony：laravel框架的底层（如请求类、相应类、文件管理类）使用了symfony框架的部分，所以该目录
					包含这部分的内容
			monolog：日志记录模块文件
			phpunit：程序单元测试模块文件
	
	
### laravel框架应用程序三个重要环节
		1、路由
			路由大部分记录在laravel\app\Http\routes.php文件中，文件应用程序路由服务提供者启动过程中，通过
			app\Providers\Route-ServiceProvider.php文件中的map()方法和代码 require app_path('Http/routes.php')
			进行加载
			*基础路由设置
				定义格式： Route::方法名('资源标识',闭包函数或控制器响应函数标识)
			*路由参数
				Route::get('资源标识/{参数名[?][/{参数名}...]}',闭包函数或控制器响应标识)[->where('参数名','正则表达式')];
			*路由命名
				Route::get('user/name',['as'=>'name','uses']=>function(){
					return 'laravel';
				});
			*路由群组
				项目很大时会定义很多路由，对路由进行分组，同时添加中间件，前缀，子域名等，使路由定义更加简洁
					Route::group(['prefix'=>'user','middleware'=>'auth'],function(){
						Route::get()...;
					});
		2、控制器
			需要定义一个控制器名称，并集成基础控制类App\Http\Controllers\Controller就可以生吃一个新的控制器，该基础控制器类
			集成自Illuminate\Routing\Controller类，其中定义了控制器所需要的基本方法
		3、控制器路由
			* 基础控制器路由
				Route::get('home/{id}/{name?}','HomeController@index');
				public function index($name,$id=null){
					return 'Hello,'.$name.','.$id;
				}
			
			* 隐式控制器路由
				Route::controller('home','HomeController');
			* Restful 资源控制器路由
				Route::resource('根资源标识','控制器类名');
				
### RESTful 接口请求方法与控制器处理函数对应表
			方法		路径			行为		控制器
			
			GET			/home			索引		index
			GET			/home/create	创建		create
			POST   		/home			保存		store
			GET 		/home/{id}		显示		show
			GET 		/home/{id}/edit	编辑		edit
			PUT/PATCH	/home/{id}		更新		update
			DELETE		/home/{id}		删除		destroy
						
		
		4、视图	
			*基本用法
				return view('user.login');		
			*数据传递
				return view('index',['username'=>'ming','age'=>'39']);
				$data = ['usernamne'=>'ming','sex'=>'male'];
				return view('index',$data);
				return view('index')->with('username','ming')->with('age','180');
				return view('index')->withUsername('ming')->withAge('18');
						
			* blade模板
				@extend('布局文件名'): 用于继承一个布局文件
				@section('区块名'):用于定义一个区块
				@parent：用于显示继承的布局模板中的内容
				@yield('区块文件','默认内容'):用于在布局文件中定义一个区块，在视图文件中同样可以通过
						@section @stop @endsection 来定义这个区块 
				@include('子视图名称'):用于在视图文件中加载子视图文件，使视图文件结构清晰
				
				语法标签
					*变量输出格式
						{{ 变量或返回值为一个变量的函数 }}
						{{$name}}
					*检查数据是否存在并输出
						{{$name or 'default'}}
					*控制流程语句
						@if($user=='ming')
							echo $user;
						@else
							echo 2;
						@endif	



## 五、框架中的设计模式
		1、服务容器
			*依赖和耦合
				依赖可以理解为一个对象实现某个功能需要其他对象相关功能的支持。
				当用new关键字在一个组件内部实例化一个对象时就解决了一个依赖，同时引入另一个严重的问题==耦合
			*工厂模式
				旅游者与交通工具的依赖，变成旅游者与交通工具工厂之间的依赖。
			*IoC模式
				依赖注入模式 Depe-ndency Injection
				控制反转是将组件间的依赖关系从程序内部提到外部容器来管理
				而依赖注如是指组件的依赖通过外部以参数或其他形式注入
		
		2、请求处理管道
			*装饰者模式
				是在开放-关闭原则下实现动态添加或减少功能的一种方式。
				laravel为例，在解析请求生成响应之前或之后需要经过中间件的处理，主要包括验证维护模式、cookie加密、
				开启回话、CSRF保护等，而这些处理有些事在生成响应之前，有些是在生成响应之后，在实际开发过程中有可能
				还需要添加新的处理功能，如果在不修改原有类的基础上动态地添加或减少处理功能将使框架可扩展性大大增强，
				=》可以被装饰者模式解决。
				


## 七、请求到响应的生命周期
		程序的启动阶段是入口文件中的代码 “require_once __DIR__.'/../bootstrap/app.php”
		主要实现了服务容器和实例化的基本注册，包括服务容器本身注册、基础服务提供者注册、核心类别名注册和基本路径
		注册，在注册过程中，服务容器会在对应属性中记录注册的内容，以便在程序运行期间提供对应的服务。

		1、服务容器实例化
			入口文件 index.php 的第一句包含 bootstrap 文件夹下的autoload.php文件，用来实现类的自动加载功能。第二句调用
			bootstrap下的 app.php中的代码，主要用来实例化服务容器，并注册laravel框架的核心类服务，为后面自动生成$kernel
			核心类实例提供基础
			*注册基础绑定
			*注册基础服务提供者
			*注册核心类别名和应用的基础路径
			
		2、核心类(Kernel类)实例化	

		
		
####  HTTP请求实例
		* 获取请求方法
			 
			


				
						
						
						
						
						
						
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	