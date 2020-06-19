#### laravel Controller

#### 访问请求
			通过依赖注入获取当前HTTP请求实例，应该在控制器的构造函数或方法中对Illuminate\Http\Request类进行类型提示，当前请求实例会被服务容器自动注入
			如果你的控制器方法还期望获取路由参数输入，只需要将路由参数置于其它依赖之后即可，例如，如果你的路由定义如下：
			Route::put('user/{id}','UserController@update');
			你仍然可以对Illuminate\Http\Request进行类型提示并通过如下方式定义控制器方法来访问路由参数：
		
		* 基本请求信息
			1、获取请求URI
				$uri = $request->path();   		返回请求的URI
				$url = $request->url();			获取完整的URL
				if($request->is('admin/*')){}	验证进入的请求是否与给定模式匹配
			2、获取请求方法
				$method = $request->method();
				if($request->isMethod('post')){}
				
		* 单个行为控制器
			定义一个只处理单个行为的控制器，你可以在控制器中放置一个 __invoke 方法
			public function __invoke($id)
			{
				return view('user.profile', ['user' => User::findOrFail($id)]);
			}
						
#### 获取输入
		获取输入值
			从Illuminate\Http\Request 实例中访问用户输入。
			$name = $request->input('name');
							  input('name','wdz') 添加默认值，不存在时返回此值
							  input('products.name')  用.来访问数组
		判断输入值是否出现
			if( $request->has('name') ){ // }
		获取所有输入数据
			$input = $request->all();
		获取输入的部分数据
			$request->only('username','pwd');
			$request->except('credit_card');


#### SESSION
		Session
			Request $request
			赋值、获取session的三种方式
			1、
				$request->session()->put('key','val');
				$request->session()->get('key');
			2、
				session()->put('key','val');
				session()->get('key');
			3、
				Session::put('key','val');
				Session::get('key','val');
				
			以数组的形式存储数据
				Session::put(['key'=>'val']);
			把数据放到Session的数组中
				Session::push('student','sean');
				Session::push('student','imooc');
			取出session数据并删除
				Session::pull('student','default');
			取出所有的值
				Session::all();
			判断session是否存在某个key
			    Session::has('key')
			删除指定key的值
				Session::forget('key');
			清空所有session信息
				Session::flush();
			暂存，只保存一次页面访问
				Session::flash('f-key','f-val');
				
		
		Response
			响应json
				response()->json($data);
			重定向
				return redirect('index');
				action()
					return redirect()->action('TestController@test');
				route()
					return redirect()->route('test');
				back();
					return redirect()->back();
				可以带数据
					->with('message','data');
		
		
		Middleware 中间件
			编写中间件
				app\Http\Middleware
				namespace App\Http\Middleware;
				use Closure;
				class Activity{
					//前置操作
					public function handle($request,Closure $next){
						if()...{
							return redirect()->back();
						}
						return $next($request);
					}
				}
				
				
			注册中间件
				app\Http\Requests\Kernel.php
				protected $routeMiddleware = [
					//在此添加全局中间件
					'activity'=>\App\Http\Middleware\Activity::class,
				];
			
			在route路由中 添加路由群组
				Route::group(['middleware'=>['activity']],function(){
					Route::any....
				});
				

#### 控制器 数据验证
			$this->validate($request,[
				'Student.name'=>'required|min:2|max:20',
				'Student.sex'=>'required|min:0|max:1',
				'Student.age'=>'required|integer',
			],[
				'required'=>':attribute 为必选项',
				'min'=>'最小值'
			],[
				'Student.name'=>'姓名',
				'Student.sex'=>'性别',
			]);
			
			如果验证不成功，会返回到上一个页面，并将错误输出在$errors
			视图中使用  {{ $errors->first() }}		输出第一个错误
			@foreach($errors->all() as $error)
				{{ $error }}
			@endforeach								循环输出所有错误
			

#### 文件上传
			获取上传文件的信息
				$request->file('source');
			文件是否上传成功
				$file->isValid();
			文件的属性
				$file->getClientOriginalName();			原文件名
				$file->getClientOriginalExtension();	扩展名
				$file->getClientMimeType();				MimeType
				$file->getRealPath();					临时绝对路径
				
				
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			