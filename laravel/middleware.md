#### 中间件
		1、
		 HTTP中间件提供了一个便利的机制来过滤进入应用的HTTP请求
		 Laravel框架内置了一些中间件，包括维护模式中间件、认证、CSRF保护中间件等等。所有的中间件都位于app/Http/Middleware目录。
		2、定义中间件
			artisan命令 make：middleware 可以创建一个新的中间件
			将请求往下传递可以通过调用回调函数$next
			理解中间件的最好方式就是将中间件看做HTTP请求到达目标之前必须经过的“层”，每一层都会检查请求甚至会完全拒绝它。
		 
			* 中间件前后
				一个中间件是否请求前还是请求后执行取决于中间件本身
				请求前处理
					//执行
						return $next($request);
				请求处理后执行其任务		
					$request = $next($request);
					//执行
					return $request
		3、注册中间件	
			* 全局中间件
				如果你想要中间件在每一个HTTP请求期间被执行，只需要将相应的中间件类放到app/Http/Kernel.php的数组属性$middleware中即可。
			* 分配中间件到路由
				如果你想要分配中间件到指定路由，首先应该在app/Http/Kernel.php文件中分配给该中间件一个简写的key，默认情况下，该类的$routeMiddleware属性包含了Laravel内置的入口中间件，添加你自己的中间件只需要将其追加到后面并为其分配一个key：
				protected $routeMiddleware = [
					'my' => \App\Http\Middleware\Authenticate::class,
				]
				中间件在HTTP kernel中被定义后，可以在路由选项数组中使用$middleware 键来指定中间件
					Route::get('admin/profile', ['middleware' => 'auth', function () {
					}]);
			* 中间件参数
				中间件还可以接收额外的自定义参数，比如，如果应用需要在执行动作之前验证认证用户是否拥有指定的角色，可以创建一个RoleMiddleware来接收角色名作为额外参数。
				额外的中间件参数会在$next参数之后传入中间件：
		 
			* 可终止的中间件
				有时候中间件可能需要在HTTP响应发送到浏览器之后做一些工作。
				为了实现这个，定义一个可终止的中间件并添加terminate方法到这个中间件：
				public function handle(){}
				public function terminate($request,$response){
					//存储session数据
				}
				
				terminate 方法将会接受请求和响应作为参数。
				一旦你定义了一个可终止的中间件，应该将其加入到HTTP kernel的全局中间件列表中。
				
				
				
				
		 
		 
		 
		 
		 
		 
		 
		 
		 