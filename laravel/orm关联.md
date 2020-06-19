### ORM关联
		定义关联关系
			eloquent关联关系以Eloquent模型类方法的形式被定义。
			定义关联关系为函数能够提供功能强大的方法链和查询能力
		1、一对一
			$this->hasOne('App\Phone');
			Phone模型默认有一个user_id外键，如果希望重写这种约定，传递第二个参数
			$this->hasOne('App\Phone','foreign_key');
			Eloquent假设外键应该在父级有一个与之匹配的id，如果你想要关联关系使用其他值而不是id，传递第三个参数
				$this->hasOne('App\Phone','foreign_key','local_key');
			
			belongsTo 方法定义与hasOne关联关系相对的关联
				$this->belongsTo('App\User');
				Eloquent将会尝试通过Phone模型的user_id去User模型查找与之匹配的记录	
				Eloquent通过关联关系方法名并在方法名后加_id后缀来生成默认的外键名
				如果Phone模型上的外键不是user_id，也可以将自定义的键名作为第二个参数传递到belongsTo方法
				$this->belongsTo('App\User', 'foreign_key');
				如果父模型不使用id作为主键，或者你希望使用别的列来连接子模型，可以将父表自定义键作为第三个参数传递给belongsTo方法
				$this->belongsTo('App\User', 'foreign_key', 'other_key');
				
		2、一对多
			用于定义单个模型拥有多个其他模型的关联关系。
				$this->hasMany('App\Comment');
			Eloquent会自动判断Comment模型的外键，将拥有者模型名称加上id后缀作为外键
			关联关系被定义后，我们可以通过访问comments属性来访问评论集合。
			由于Eloquent提供动态属性，我们可以像访问模型的属性一样访问关联方法
				App\Post::find(1)->commnets;
				foreach($comments as $comment){ ... }
			同时所有关联也是查询构建器，可以添加更多的条件约束到 调用 comments方法获取到评论上
				$comments =
				App\Post::find(1)->commnets()->where('title','foo')->first();
			也可以传递参数来重新设置外键和本地主键
				$this->hasMany('App\Comment','foreign_key','local_key');
		
			反向 belongsTo
		
		3、多对多
			关联关系类似 一个用户有多个角色，同时一个角色被多个用户公用
			通过 Eloqunent基类上的belongsToMany方法的函数来定义
				$this->belongsToMany('App\Role');
			定以后用动态属性roles来访问用户角色
			也可以调用roles方法来添加条件约束到关联查询上
				$roles = App\User::find(1)->roles()->orderBy('name')->get();
			传递参数到belongsToMany方法来定义表中字段的列名
			    第三个参数是定义关联模型的外键名称，第四个参数是连接到模型的外键名称
				belongsToMany('App\Role','user_roles','user_id','role_id')
				
		4、远层的一对多
				return $this->
					hasManyThrough('App\Post','App\User');
				第一个传递参数是最终希望访问的模型的名称，第二个参数是中间模型名称
				
				return $this->hasManyThrough('App\Post', 'App\User', 'country_id', 'user_id');
				如果你想要自定义该关联关系的外键，可以将它们作为第三个、第四个参数传递给hasManyThrough方法。第三个参数是中间模型的外键名，第四个参数是最终模型的外键名
				
				
		
#### 访问器 | 修改器
		定义访问器
			要定义一个访问器，需要在模型中创建一个getFooAttribute方法，其中Foo是你想要访问的字段名
				public function getFooAttribute($value){
					return ucfirst($value); }
				$user = App\User::find(1);
				$foo = $user->foo;                
		
		定义修改器
			要定义一个修改器，需要在模型中定义setFooAttribute方法，其中Foo是你想要访问的字段
			public function setFooAttribute($value){
				$this->attributes['name'] = strtolower($value);
			}
			$user = App\User::find(1);
			$user->first_name = 'Sally';
			修改器会对其调用strtolower函数并将处理后的值设置为内部属性的值
			
		属性转换	
			模型中的$casts属性提供了便利方法转换属性到通用数据类型。
			$casts属性是数组格式，其键是要被转换的属性名称，其值时你想要转换的类型。目前支持的转换类型包括：
			integer, real, float, double, string, boolean, object和array。
			模型中：
				protected $casts = [
					'is_admin' => 'boolean',
				];
			现在，is_admin属性在被访问时总是被转换为boolean，即使底层存储在数据库中的值是integer
			
			
#### 序列化
		当构建JSONAPI时，经常需要转化模型和关联关系为数组或JSON。Eloquent包含便捷方法实现这些转换，以及控制哪些属性被包含到序列化中。
		
		***基本使用
			1、转化模型为数组
				要转化模型及其加载的关联关系为数组，可以使用toArray方法。这个方法是递归的，所以所有属性及其关联对象属性（包括关联的关联）都会被转化为数组：
				$user = App\User::with('roles')->first();
				$user->toArray();
			2、转化模型为JSON
				toJson();
			3、在JSON中隐藏属性显示
				希望在模型数组或者JSON显示中限制模型私密属性，在模型中添加
					protected $hidden = ['password','sex'];
				visible属性定义显示的白名单
					protected $visible = ['first_name','age'];
			4、追加值到JSON
				当添加数据库中没有相应的字段到数组中，实现追加值,首先要定义一个访问器
				public function getIsAdminAttribute(){
					return $this->attributes['admin'] == 'yes';
				}
				定义好访问器后，添加字段名到模型的appends属性
				protected $appends = ['is_admin'];
				字段被添加到appends列表之后，将会被包含到模型数组和JSON表单中，appends数组中的字段还会遵循模型中的visible和hidden设置配置。
			
			
			
			
			
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				