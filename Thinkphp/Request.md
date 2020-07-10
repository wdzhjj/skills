### tp5.1请求

#### 请求对象
	当前的请求对象由think\Request类负责，在很多场合下并不需要实例化调用，通常使用依赖注入即可。
	在其它场合（例如模板输出等）则可以使用think\facade\Request静态类操作。
	
	请求对象调用
		构造方法注入
			use think\Request;
			
			protected $request;
			public function __construct(Request $request)
			{
				$this->request = $request;
			}
			
			如果你继承了系统的控制器基类think\Controller的话，系统已经自动完成了请求对象的构造方法注入了，你可以直接使用$this->request属性调用当前的请求对象。
				return $this->request->param('name');
	
		操作方法注入
			use think\Request;
			public function index(Request $request)
			{
				return $request->param('name');
			}  
			
		Facade调用
			use think\facade\Request;
			return Request::param('name');
	
		助手函数
			return request()->param('name');
	
	
#### 请求信息
	方法		含义
	host		当前访问域名或者IP
	scheme		当前访问协议
	port		当前访问的端口
	remotePort	当前请求的REMOTE_PORT
	protocol	当前请求的SERVER_PROTOCOL
	contentType	当前请求的CONTENT_TYPE
	domain		当前包含协议的域名
	subDomain	当前访问的子域名
	panDomain	当前访问的泛域名
	rootDomain	当前访问的根域名（V5.1.6+）
	url			当前完整URL
	baseUrl		当前URL（不含QUERY_STRING）
	query		当前请求的QUERY_STRING参数
	baseFile	当前执行的文件
	root		URL访问根地址
	rootUrl		URL访问根目录
	pathinfo	当前请求URL的pathinfo信息（含URL后缀）
	path		请求URL的pathinfo信息(不含URL后缀)
	ext			当前URL的访问后缀
	time		获取当前请求的时间
	type		当前请求的资源类型
	method		当前请求类型
	
	
#### 请求类型
	获取请求类型
	用途				方法
	获取当前请求类型	method
	判断是否GET请求		isGet
	判断是否POST请求	isPost
	判断是否PUT请求		isPut
	判断是否DELETE请求	isDelete
	判断是否AJAX请求	isAjax
	判断是否PJAX请求	isPjax
	判断是否为JSON请求	isJson（V5.1.38+）
	判断是否手机访问	isMobile
	判断是否HEAD请求	isHead
	判断是否PATCH请求	isPatch
	判断是否OPTIONS请求	isOptions
	判断是否为CLI执行	isCli
	判断是否为CGI模式	isCgi

#### 响应输出
	输出类型	快捷方法	对应Response类
	HTML输出	response	\think\Response
	渲染模板输出	view	\think\response\View
	JSON输出	json		\think\response\Json
	JSONP输出	jsonp		\think\response\Jsonp
	XML输出		xml			\think\response\Xml
	页面重定向	redirect	\think\response\Redirect
	附件下载	download	\think\response\Download
	
	输出html格式的内容
		return response($data);
	输出json格式数据给客户端
		return json($data);
	
	设置状态码
	json($data,201)
	view($data,401)
	json($data)->code(201);
	设置头信息
	json($data)->code(201)->header(['Cache-control' => 'no-cache,must-revalidate']);
		方法名			作用
		lastModified	设置Last-Modified头信息
		expires			设置Expires头信息
		eTag			设置ETag头信息
		cacheControl	设置Cache-control头信息
		contentType		设置Content-Type头信息
	
	文件下载
	 return download('image.jpg', 'my.jpg');
		方法		描述
		name		命名下载文件
		expire		下载有效期
		isContent	是否为内容下载
		mimeType	设置文件的mimeType类型
	
	
	
	
	