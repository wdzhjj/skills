#### Laravel 路由 
		
		基础路由
			Route::get('basic1',function(){
				return 'hello';
			});
			Route::post('basic2',function(){
				return 'hello';
			});
			
			匹配响应请求
			Route::match(['get','post'],'multy',function(){
				return 'multy';
			});
			
			匹配所有请求
			Route::any('multy2',function(){
				return 'multy2';
			});
		
			路由参数
				Route::get('user/{id}',function($id){
					return 'user-'.$id;
				});
			可选参数
				Route::get('user/{name?}',function($name = null){
					return 'username-'.$name;
				});
				可以跟正则表达式来限制
				->where('name','[A-Za-z]+');       不符合会报错
			
			路由中输出视图
				return view('welcome');
			路由关联控制器
				Route::get('member/info','MemberController@index');
				Route::get('member/info',['uses'=>'MemberController@index']);
				传递参数
					Route::any('member/{id}',['uses'=>'MemberController@index'])
					->where('id','[0-9]+');
				
		全局约束
			如果想要路由参数在全局范围内被给定正则表达式约束，可以使用pattern方法。
			在RruteServicePrvider类的boot方法中定义约束模式
				public function boot(Router $router){
					$router->pattern('id','[0-9]+');
					parent::boot($router);
				}
		
#### 路由分组
		路由分组允许我们在多个路由中共享路由属性，比如中间件和命名空间等，这样的话一大波共享属性的路由就不必再各自定义这些属性。共享属性以数组的形式被作为第一个参数传递到Route::group方法中。
		1、中间件
			分配中间件给分组中的所有路由，可以在分组属性数组中使用 middleware键。中间件将会按照数组中定义的顺序依次执行
			Route::group(['middleware'=>'auth'], function(){
				Route::get('/',function(){
					//使用auth中间件
				});
				Route::get('/user',function(){
					//使用auth中间件
				});
			});
		2、命名空间
				Route::group(['namespace'=>'User'],function(){
					//控制器在 App\Http\Controller\Admin\User 命名空间下
 				});
		3、子域名路由
				路由分组还可以被用于子域名路由通配符，子域名可以像URIs一样被分配给路由参数，
				从而允许捕获子域名的部分用于路由或者控制器，子域名可以通过分组属性数组中的domain键来指定
					Route::group(['domain' => '{account}.myapp.com'], function () {
		4、路由前缀
				属性prefix可以用来为分组中每个给定URI添加一个前缀
					Route::group(['prefix' => 'admin'], function () {
					

#### 防止CSRF攻击
		1、
		Laravel使得防止应用遭到跨站请求伪造攻击变得简单。
		跨站请求伪造是一种通过伪装授权用户的请求来利用授信网站的恶意漏洞。
		Laravel自动为每一个被应用管理的有效用户Session生成一个CSRF“令牌”，该令牌用于验证授权用户和发起请求者是否是同一个人。
			<?php echo csrf_field(); ?>   
			还可以使用Blade模板引擎提供的方式：
			{!! csrf_field() !!}
			生成如下html
			<input type="hidden" name="_token" value="<?php echo csrf_token(); ?>">
		2、从CSRF保护中排除URIs
			比如，如果你在使用Stripe来处理支付并用到他们的webhook系统，这时候你就需要从Laravel的CSRF保护中排除webhook处理器路由。
			你可以通过在VerifyCsrfToken中间件中将要排除的URIs添加到$except属性：
			class VerifyCsrfToken extends BaseVerifier{
				protected $except = [
					'stripe/*',
				];
			}
		
		3、 X-CSRF-Token
			除了将CSRF令牌作为一个POST参数进行检查，Laravel的VerifyCsrfToken中间件还会检查X-CSRF-TOKEN请求头，你可以将令牌保存在"meta"标签中：
				<meta name="csrf-token" content="{{ csrf_token() }}">
			创建完这个meta标签后，就可以在js库如jQuery中添加该令牌到所有请求头，这为基于AJAX的应用提供了简单、方便的方式来避免CSRF攻击：
				$.ajaxSetup({
						headers: {
							'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
						}
				});
		
		4、X-XSRF-Token
			Laravel还将CSRF令牌保存到了名为XSRF-TOKEN的cookie中，你可以使用该cookie值来设置X-XSRF-TOKEN请求头。一些JavaScript框架，比如Angular，将会为你自动进行设置，基本上你不太会手动设置这个值。
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		