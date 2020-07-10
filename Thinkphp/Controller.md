### 控制器

#### 控制器定义	
	控制器文件通常放在application/module/controller下面，类名和文件名保持大小写一致，并采用驼峰命名（首字母大写）。
		namespace app\index\controller;
		use think\Controller;
		class Index extends Controller
		{
			public function index()
			{
				return 'index';
			}
		}
		为了更方便使用，控制器类建议继承系统的控制器基类think\Controller，虽然无需继承也可以使用。	
	
	前置操作
		可以为某个或者某些操作指定前置执行的操作方法
		beforeActionList属性可以指定某个方法为其他方法的前置操作，数组键名为需要调用的前置方法名，无值的话为当前控制器下所有方法的前置方法。
		['except' => '方法名,方法名']
			表示这些方法不使用前置方法，
		['only' => '方法名,方法名']
			表示只有这些方法使用前置方法。
		protected $beforeActionList = [
			'first',
			'second' =>  ['except'=>'hello'],
			'three'  =>  ['only'=>'hello,data'],
		];
	
	页面跳转
		系统的\think\Controller类内置了两个跳转方法success和error，用于页面跳转提示。
	success和error方法都可以对应的模板，默认的设置是两个方法对应的模板都是：
		'thinkphp/tpl/dispatch_jump.tpl'
	//默认错误跳转对应的模板文件
		'dispatch_error_tmpl' => 'public/error',	
	模板文件可以使用模板标签，并且可以使用下面的模板变量：
		变量	含义
		$data	要返回的数据
		$msg	页面提示信息
		$code	返回的code
		$wait	跳转等待时间 单位为秒
		$url	跳转页面地址
			
	重定向
		\think\Controller类的redirect方法可以实现页面的重定向功能。
		$this->redirect('News/category', ['cate_id' => 2], 302, ['data' => 'hello']);
	
	空操作
		空操作是指系统在找不到指定的操作方法的时候，会定位到空操作（_empty）方法来执行，利用这个机制，我们可以实现错误页面和一些URL的优化。
	    public function _empty($name)
		{
			//把所有城市的操作解析到city方法
			return $this->showCity($name);
		}
	
	空控制器
		空控制器的概念是指当系统找不到指定的控制器名称的时候，系统会尝试定位空控制器(Error)，利用这个机制我们可以用来定制错误页面和进行URL的优化。
	我们可以给项目定义一个Error控制器类
	访问到不存在的空控制器时，定位到空控制器（Error）去执行，


#### 控制器中间件
	protected $middleware = ['Auth'];
	当执行index控制器的时候就会调用Auth中间件，一样支持使用完整的命名空间定义。
	protected $middleware = [ 
    	'Auth' 	=> ['except' 	=> ['hello'] ],
        'Hello' => ['only' 		=> ['hello'] ],
    ];
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	