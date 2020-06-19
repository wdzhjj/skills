### laravel 数据库操作
		config/database.php 
		.env
		修改连接数据库配置

#### DB facade实现CURD
		查找
		DB::select('select * from student');
		新增
		DB::insert('insert into student(name,age) values(?,?)',['wdz',17]);
			返回false or true
		更新
		DB::update('update student set age = ? where name = ?',[20,'wdz']);
			返回修改行数
		删除
		DB::delete('delete from student where id > ?',[1001]);	

#### 查询构造器来操作数据库
		新增数据
			DB::table('student')->insert(
				['name'=>'imooc','age'=>18],
				['name'=>'imooc2','age'=>19]
			);
		新增返回自增id
			DB::table('student')->insertGetId(
				['name'=>'wdz','age'=>15]
			);
			返回2；
		更新数据
			DB::table('student')
			->where('id',12)
			->update(['age'=>30]);
		自增|自减
			DB::table('student')->in|decrement('age',3);
		
		删除数据
			DB::table('student')->where('id','>','12')->delete();
			DB::table('student')->truncate();      清空数据表，一般不使用

		查询数据
			DB::table('student')->get();
			->get()获取此表的所有数据
			->first();	获取一条记录
			->where()   条件
			->whereRaw()  多个条件   'id>? and age>?',[1001,18]
			->pluck()|lists()	返回指定的字段
			->select()    指定查找
			->chunk()     分段获取数据  
				DB::table('student')->chunk(2,function($student){
				});
		聚合函数
			count()  统计数量
			max() 	 最大值
			min()	 最小值
			avg()    平均数
			sum()    总和

			
		******where子句
			or  可以通过方法链将多个where 约束链接到一起，也可以添加or子句到查询
				orWhere 方法和 where接收参数方法一样
			whereBetween 方法验证列值是否在给定值之间
				DB::table('users')->whereBetween('votes',[1,100])->get();
			whereNotBetween	 	方法验证列值不在给定值之间
			whereIn | whereNotIn	方法验证给定列知否 在|不在 给定数组中
			whereNull | whereNotNull	验证给定列的值 为|不为 Null
			
			高级where子句
				DB::table('users')
					->where('age','>','10')
					->orWhere(function($query){
						$query->where('votes','>',11)
								->where('title','<>','admin');
					})
					->get();
			exists语句
				whereExists方法允许你编写where existSQL子句，whereExists方法接收一个闭包参数，该闭包获取一个查询构建器实例从而允许你定义放置在"exists"子句中的查询
			
			*********排序、分组、限定
				orderBy
					给定列对结果集进行排序，orderBy的第一个参数是你希望排序的列，第二个参数控制着排序方向  asc/desc
				groupBy | having 
					对结果集进行分组，方法类似
					DB::table('users')->groupBy('account_id')
						->having('account_id','>',100)->get();
				havingRaw
					用于设置原生字符串作为having子句的值
					->havingRaw('SUM(price) > 2500')
				skip | take	
					想要限定查询返回的结果集和数目，或者在查询中跳过给定数目的结果
					->skip(10)->take(4)->get();
					
			
			
		
#### Eloqunent ORM  操作数据库
		定义模型
			模型通常位于app目录下，所有Eloqunent模型都继承自Illuminate\Database\Eloquent\Model类
			最简单创建模型  php artisan make:model ModelName
			生成模型时生成数据库迁移 使用  --migration 或 -m选项
				php artisan make:model --migration
				
		建立模型
			指定表名
				protected $table = 'student';
				默认情况下是模型的复数
			指定id
				protected $primaryKey = 'id';
				默认情况下是id
			是否自动维护时间戳
				public $timestamps = false;
			指定允许批量赋值的字段
				protected $fillable = ['name','age'];
			默认获取时间戳的数据类型
				protected function getDateFormat(){
					return time(); }
				
		
		查询数据
			Student::all();		返回所有记录的ORM集合
			find(1001)			返回id为X的模型对象
			findOrFail()		没查到报错
			get()				查询所有数据
			first()				查询第一条
			chunk(n,function(){ })	分段获取数据
			聚合函数
				Student::count();	
			
		使用模型新增数据
			save()
				$data = new Student();
				$data->name='wdz';
				$data->age=148;
				$data->save();
		    create()
				Student::create(
					['name'=>'imooc','age'=>18]          需要允许批量添加
				);
			firstOrCreate()		
				以属性查找用户，如果没有则新增数据，存在则返回数据
			firstOrNew()
				以属性查找用户，如果没有则建立新的实例，需要保存的话用save
				
		使用ORM修改数据
			$data = Student::find(11);
			$data->name = 'wdz';
			$data->save();
			批量更新
				Student::where('id','>',1019)->update(
					['age'=>51]
				);
			删除数据
				通过模型删除
				delete() 返回bool值
				$data = Student::find(1);
				$data->delete();
				通过主键删除
				Student::destory([2,3,4]);	返回影响的数量
			
		*********查询作用域
			作用域允许你定义一个查询条件的通用集合，这样就可以在应用中方便地复用
			你需要频繁获取最受欢迎的用户，要定义一个作用域，只需要简单的在Eloquent模型方法前加上一个scope前缀
			
			使用查询作用域
				作用域被定义好了之后，就可以在查询模型的时候调用作用域方法，但调用时不需要加上scope前缀，你甚至可以在同时调用多个作用域
				$users = App\User::popular()->women()->orderBy('created_at')->get();
				
			动态作用域
				public function scopeOfType($query, $type){
					return $query->where('type',$type);  }
				之后可以在作用于时传递参数
					App\User::ofType('admin')->get();
			
			
		**************事件
			Eloquent模型可以触发事件，允许你在模型生命周期中的多个时间点调用如下这些方法
			creating, created, updating, updated, saving, saved,deleting, deleted, restoring, restored
			事件允许你在一个指定模型类每次保存或更新的时候执行代码。
			一个新模型被首次保存的时候，creating和created事件会被触发。如果一个模型已经在数据库中存在并调用save方法，updating/updated事件会被触发
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			









		