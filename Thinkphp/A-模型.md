### Thinkphp5.1 模型
	
#### 模型定义
	namespace app\index\model;
	use think\Model;

	class User extends Model
	{		
	}
	模型会自动对应数据表，模型类的命名规则是除去表前缀的数据表名称，采用驼峰法命名，并且首字母大写，
	User=>user    UserType=>user_type  (无前缀)
	
	模型设置
		默认主键为id，如果你没有使用id作为主键名，需要在模型中设置属性：
		protected $pk = 'uid';
		指定数据表甚至数据库
			设置当前模型对应的完整数据表名称
				protected $table = 'think_user';
			设置当前模型的数据库连接
				protected $connection = 'db_config';
		属性			描述
		name		模型名（默认为当前不含后缀的模型类名）
		table		数据表名（默认自动获取）
		pk			主键名（默认为id）
		connection	数据库连接（默认读取数据库配置）
		query		模型使用的查询类名称
		field		模型对应数据表的字段列表（数组）
	
	模型初始化
		//模型初始化
		protected static function init()
		{
			//TODO:初始化内容
		}
		模型初始化方法通常用于注册模型的事件操作。
		- init必须是静态方法，并且只在第一次实例化的时候执行
	
	模型操作
		Db::name('user')->where('id','>',10)->select();
		User::where('id','>',10)->select();
		- 查询结果的类型不同
		- 第一种方式的查询结果是一个（二维）数组，
		- 而第二种方式的查询结果是包含了模型（集合）的数据集。
	
#### 添加/更新/删除/查询
	添加
		save()
		save方法返回影响的记录数，并且只有当before_insert事件返回false的时候返回false
		replace()	
			$user->replace()->save();
		获取自增ID
			$user = new User;
			$user->save();
			echo $user->id;    获取模型的主键
			如果你的主键不是id，而是user_id的话  $user->user_id
		添加多条数据
			$user->saveAll($list);
			saveAll方法新增数据返回的是包含新增模型（带自增ID）的数据集对象。
		静态方法
			$user = User::create([
				'name'  =>  'thinkphp',
				'email' =>  'thinkphp@qq.com'
			]);
			echo $user->id; // 获取自增ID
			 - 和save方法不同的是，create方法返回的是当前模型的对象实例。
	
	更新
		查找并更新
			$user = User::get(1);
			$user->name     = 'thinkphp';
			$user->score	=  Db::raw('score+1');
			$user->save();
	
		直接更新数据
			$user = new User;
			$user->allowField(true)    //过滤post数组中的非数据表字段数据
			->save([
				'name'  => 'thinkphp',
				'email' => 'thinkphp@qq.com'
			],['id' => 1]);   //第二个参数是条件
	
		批量更新数据
			可以使用saveAll方法批量更新数据，只需要在批量更新的数据中包含主键即可
				$user = new User;
				$list = [
					['id'=>1, 'name'=>'thinkphp', 'email'=>'thinkphp@qq.com'],
					['id'=>2, 'name'=>'onethink', 'email'=>'onethink@qq.com']
				];
				$user->saveAll($list);
	
		静态方法
			User::where('id', 1)
				->update(['name' => 'thinkphp']);
	
	
	删除
		删除当前模型
			$user = User::get(1);
			$user->delete();
		根据主键删除
			User::destroy(1);
			User::destroy('1,2,3');
			User::destroy([1,2,3]);
		条件删除
			User::destroy(function($query){
				$query->where('id','>',10);
			});
			User::where('id','>',10)->delete();
	
	查询
		获取单个数据
			$user = User::get(1);
			$user = User::where('name', 'thinkphp')->find();
			$user = User::where('name', 'thinkphp')->findOrEmpty();
			- 使用findOrEmpty方法，当查询数据不存在的话，返回空模型而不是Null。
		获取多个数据
			$list = User::all('1,2,3');
			$list = User::where('status', 1)->limit(3)->order('id', 'asc')->all();
		自定义数据集对象
			protected $resultSetType = '\app\common\Collection';
		使用查询构造器
			User::where('id',10)->find();
			User::where('status',1)->order('id desc')->select();
			User::where('status',1)->limit(10)->select();
			无需实例化模型，直接使用静态方法调用即可
		动态查询
			// 根据name字段查询用户
			$user = User::getByName('thinkphp');
			// 根据email字段查询用户
			$user = User::getByEmail('thinkphp@qq.com');
		聚合查询
			User::count();
			User::where('status','>',0)->count();
			User::where('status',1)->avg('score');
			User::max('score');
		数据分批处理
			User::chunk(100,function($users) {
				foreach($users as $user){
					// 处理user模型对象
				}
			});
	
#### json字段
	这里指的JSON数据包括JSON类型以及JSON格式（但并不是JSON类型字段）的数据
		// 设置json类型字段
		protected $json = ['info'];
		定义后，可以进行以下json数据操作
			- 写入JSON数据
				$user = new User;
				$user->name = 'thinkphp';
				$user->info = [
					'email'    => 'thinkphp@qq.com',
					'nickname '=> '流年',
				];
				$user->save();
			- 查询JSON数据		
				$user = User::get(1);
				echo $user->name; // thinkphp
				$user = User::where('info->nickname','流年')->find();
			- 更新JSON数据
				$user = User::get(1);
				$user->name = 'kancloud';
				$user->info->email = 'kancloud@qq.com';
				$user->info->nickname = 'kancloud';
				$user->save();
	
	
#### 获取器/修改器/搜索器
	- 获取器
		获取器的作用是对模型实例的（原始）数据做出自动处理。一个获取器对应模型的一个特殊方法
		（该方法必须为public类型），方法命名规范为：
			getFieldNameAttr
		FieldName为数据表字段的驼峰转换，定义了获取器之后会在下列情况自动触发：
			模型的数据对象取值操作（$model->field_name）；
			模型的序列化输出操作（$model->toArray()及toJson()）；
			显式调用getAttr方法（$this->getAttr('field_name')）；
		获取器的场景包括：
			时间日期字段的格式化输出；
			集合或枚举类型的输出；
			数字状态字段的输出；
			组合字段的输出；
			
		demo:
			public function getStatusAttr($value){
				$status = [-1=>'删除',0=>'禁用',1=>'正常'];
				return $status[$value];
			}
			
	- 修改器
		和获取器相反，修改器的主要作用是对模型设置的数据对象值进行处理。
			setFieldNameAttr
		修改器的使用场景和读取器类似：
			时间日期字段的转换写入；
			集合或枚举类型的写入；
			数字状态字段的写入；
			某个字段涉及其它字段的条件或者组合写入；

		定义了修改器之后会在下列情况下触发：
			模型对象赋值；
			调用模型的data方法，并且第二个参数传入true；
			调用模型的save方法，并且传入数据；
			显式调用模型的setAttr方法；
			定义了该字段的自动完成；
		demo:
			public function setNameAttr($value)
			{
				return strtolower($value);
			}
				
	- 搜索器
		搜索器的作用是用于封装字段（或者搜索标识）的查询条件表达式，一个搜索器对应一个特殊的方法（该方法必须是public类型），方法命名规范为：
			searchFieldNameAttr
		搜索器的场景包括：
			限制和规范表单的搜索条件；
			预定义查询条件简化查询；	
		public function searchNameAttr($query, $value, $data)
		{
			$query->where('name','like', $value . '%');
		}
    
#### 一些选项
	- 自动时间戳
		全局开启，在数据库配置文件中进行设置
			// 开启自动写入时间戳字段
			'auto_timestamp' => true,
		在需要的模型类里面单独开启：
			 protected $autoWriteTimestamp = true;
		默认create_time和update_time (int)
			// 开启自动写入时间戳字段
			'auto_timestamp' => 'datetime',
			 protected $autoWriteTimestamp = 'datetime';
	
	- 只读字段
		只读字段用来保护某些特殊的字段值不被更改，这个字段的值一旦写入，就无法更改。 要使用只读字段的功能，我们只需要在模型中定义readonly属性：
		    protected $readonly = ['name', 'email'];	
	
	- 软删除
		对数据频繁使用删除操作会导致性能问题，软删除的作用就是把数据加上删除标记，而不是真正的删除，同时也便于需要的时候进行数据的恢复。
		use SoftDelete;
		deleteTime属性用于定义你的软删除标记字段，ThinkPHP的软删除功能使用时间戳类型（数据表默认值为Null），用于记录数据的删除时间。
			protected $deleteTime = 'delete_time';
			protected $defaultSoftDelete = 0;
		// 软删除
		User::destroy(1);
		// 真实删除
		User::destroy(1,true);

		$user = User::get(1);
		// 软删除
		$user->delete();
		// 真实删除
		$user->delete(true);
	
	- 类型转换
		protected $type = [
			'status'    =>  'integer',
			'score'     =>  'float',
			'birthday'  =>  'datetime',
			'info'      =>  'array',
		];
	
	- 查询范围
		public function scopeThinkphp($query)
		{
			$query->where('name','thinkphp')->field('id,name');
		}
		User::scope('thinkphp')->find();
	
	- 数组转换
		可以使用toArray方法将当前的模型实例输出为数组
			$user = User::find(1);
			dump($user->toArray());
	
	- JSON序列化
		可以调用模型的toJson方法进行JSON序列化，toJson方法的使用和toArray一样
			$user = User::get(1);
			echo $user->toJson();
	
	
#### 模型关联
	通过模型关联操作把数据表的关联关系对象化，解决了大部分常用的关联场景，
	封装的关联操作比起常规的数据库联表操作更加智能和高效，并且直观。
	避免在模型内部使用复杂的join查询和视图查询。
		模型方法		关联类型
		hasOne			一对一
		belongsTo		一对一
		hasMany			一对多
		hasManyThrough	远程一对多
		belongsToMany	多对多
		morphMany		多态一对多
		morphOne		多态一对一
		morphTo			多态
			
	
	- 一对一关联
		hasOne('关联模型','外键','主键');
		    关联模型（必须）：关联的模型名或者类名
			外键：默认的外键规则是当前模型名（不含命名空间，下同）+_id ，例如user_id
			主键：当前模型主键，默认会自动获取也可以指定传入
		关联查询
			public function profile()
			{
				return $this->hasOne('Profile');
			}
			定义好关联之后，就可以使用下面的方法获取关联数据：
			$user = User::get(1);
			// 输出Profile关联模型的email属性
			echo $user->profile->email;

		定义相对关联
			public function user()
			{
				return $this->belongsTo('User');
			}
			belongsTo('关联模型','外键','关联主键');
			关联模型（必须）：模型名或者模型类名
			外键：当前模型外键，默认的外键名规则是关联模型名+_id
			关联主键：关联模型主键，一般会自动获取也可以指定传入
			我们就可以根据档案资料来获取用户模型的信息
				$profile = Profile::get(1);
				// 输出User关联模型的属性
				echo $profile->user->account;

	
	-  一对多关联
		hasMany('关联模型','外键','主键');
			关联模型（必须）：模型名或者模型类名
			外键：关联模型外键，默认的外键名规则是当前模型名+_id
			主键：当前模型主键，一般会自动获取也可以指定传入
		关联查询
			$article = Article::get(1);
			// 获取文章的所有评论
			dump($article->comments);
			// 也可以进行条件搜索
			dump($article->comments()->where('status',1)->select());
		根据关联条件查询
			$list = Article::has('comments','>',3)->select();
		定义相对的关联
			 return $this->belongsTo('article');
	
	- 远程一对多（之间可能隔了一张表）
		hasManyThrough('关联模型','中间模型','外键','中间表关联键','主键');
			关联模型（必须）：模型名或者模型类名
			中间模型（必须）：模型名或者模型类名
			外键：默认的外键名规则是当前模型名+_id
			中间表关联键：默认的中间表关联键名的规则是中间模型名+_id
			主键：当前模型主键，一般会自动获取也可以指定传入
	
	- 多对多关联
		belongsToMany('关联模型','中间表','外键','关联键');
		    关联模型（必须）：模型名或者模型类名
			中间表：默认规则是当前模型名+_+关联模型名 （可以指定模型名）
			外键：中间表的当前模型外键，默认的外键名规则是关联模型名+_id
			关联键：中间表的当前模型关联键名，默认规则是当前模型名+_id
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	