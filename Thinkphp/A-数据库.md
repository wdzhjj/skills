### 数据库

#### 查询构造器
	基本查询
		Db::table('think_user')->where('id',1)->find();
			find 方法查询结果不存在，返回 null，否则返回结果数组
			->findOrFail()
			如果没有查找到数据，则会抛出一个think\db\exception\DataNotFoundException异常。
			->findOrEmpty()
			当查询不存在的时候返回空数组而不是Null
			->select()
			查询多个数据（数据集）使用select方法	
			->selectOrFail();
			希望在没有查找到数据后抛出异常可以使用
		
	助手函数	
		db('user')->where('id',1)->find();
		不同的数据库连接
		db('user','db_config1')->where('id', 1)->find();

	值和列查询
		查询某个字段的值可以用
		Db::table('think_user')->where('id',1)->value('name'); 返回某个字段的值
		查询某一列的值可以用
			->column('name');
			->column('name','id');
		
	数据分批处理	
		->chunk(100, 'myUserIterator');
		chunk方法，该方法一次获取结果集的一小块，然后填充每一小块数据到要处理的闭包，该方法在编写处理大量数据库记录的时候非常有用。
	大批量数据处理	
		如果你需要处理大量的数据，可以使用新版提供的游标查询功能，该查询方式利用了PHP的生成器特性，可以大幅减少大量数据查询的内存占用问题。
		$cursor = Db::table('user')->where('status', 1)->cursor();
		foreach($cursor as $user) echo $user['name'];
		cursor方法返回的是一个生成器对象，user变量是数据表的一条数据（数组）。
		
		
#### 添加
		添加一条数据
			$data = ['foo' => 'bar', 'bar' => 'foo'];
			Db::name('user')->insert($data);
			如果不希望抛出异常，可以使用下面的方法：
				Db::name('user')->strict(false)->insert($data);    不存在的字段的值将会直接抛弃。
			添加数据后如果需要返回新增数据的自增主键，可以使用insertGetId方法新增数据并返回主键值：
				$userId = Db::name('user')->insertGetId($data);
				insertGetId 方法添加数据成功返回添加数据的自增主键
		
		添加多条数据
			添加多条数据直接向 Db 类的 insertAll 方法传入需要添加的数据即可
				Db::name('user')->insertAll($data);	    insertAll 方法添加数据成功返回添加成功的条数
			分批写入
				Db::name('user')->data($data)->limit(100)->insertAll();
		
#### 更新数据		
	Db::name('user')
		->where('id',1)
		->inc('read_time')
		->dec('score',3)
		->exp('name','UPPER(name)')
		->update();
	
	更新字段值
		 ->setField('name', 'thinkphp');
	setInc/setDec方法自增或自减一个字段的值 (如不加第二个参数，默认步长为1）。
	 ->setInc('score',5);
	SET `score` = `score` + 5 
		
#### 删除数据
	// 根据主键删除
	Db::table('think_user')->delete(1);
	Db::table('think_user')->delete([1,2,3]);

	// 条件删除    
	Db::table('think_user')->where('id',1)->delete();
	Db::table('think_user')->where('id','<',10)->delete();
		
		
#### 查询表达式 
	where('字段名','表达式','查询条件');
	whereOr('字段名','表达式','查询条件');
	whereField('表达式','查询条件');
	whereOrField('表达式','查询条件');
	
	表达式			含义				快捷查询方法
	=				等于	
	<>				不等于	
	>				大于	
	>=				大于等于	
	<				小于	
	<=				小于等于	
	[NOT] LIKE		模糊查询			whereLike/whereNotLike
	[NOT] BETWEEN	（不在）区间查询	whereBetween/whereNotBetween
	[NOT] IN		（不在）IN 查询		whereIn/whereNotIn
	[NOT] NULL		查询字段是否（不）是NULL	whereNull/whereNotNull
	[NOT] EXISTS	EXISTS查询			whereExists/whereNotExists
	[NOT] REGEXP	正则（不）匹配查询（仅支持Mysql）	
	[NOT] BETWEEM TIME	时间区间比较	whereBetweenTime
	> TIME			大于某个时间		whereTime
	< TIME			小于某个时间		whereTime
	>= TIME			大于等于某个时间	whereTime
	<= TIME			小于等于某个时间	whereTime
	EXP				表达式查询，支持SQL语法	whereExp


	等于（=）	不等于（<>）   大于（>）   大于等于（>=）    小于（<）    小于等于（<=）
		Db::name('user')->where('id','<>',100)->select();
	[NOT] LIKE	
		Db::name('user')->where('name','like','thinkphp%')->select();
	[NOT] BETWEEN	
		Db::name('user')->where('id','between','1,8')->select();
	[NOT] IN	
		Db::name('user')->where('id','in','1,5,8')->select();
		Db::name('user')->where('id','in',[1,5,8])->select();
	[NOT] NULL 
		Db::name('user')->where('name', null)->where('email','null')->where('name','not null')->select();
	EXP：表达式	
		Db::name('user')->where('id','exp',' IN (1,3,8) ')->select();
		exp查询的条件不会被当成字符串，所以后面的查询条件可以使用任何SQL支持的语法，包括使用函数和字段名称。
		
		
#### 链式操作		
		连贯操作	作用						支持的参数类型
		where*		用于AND查询					字符串、数组和对象
		whereOr*	用于OR查询					字符串、数组和对象
		wheretime*	用于时间日期的快捷查询		字符串
		table		用于定义要操作的数据表名称	字符串和数组
		alias		用于给当前数据表定义别名	字符串
		field*		用于定义要查询的字段		字符串和数组
		order*		用于对结果排序				字符串和数组
		limit		用于限制查询结果数量		字符串和数字
		page		用于查询分页（内部会转换成limit）	字符串和数字
		group		用于对查询的group支持		字符串
		having		用于对查询的having支持		字符串
		join*		用于对查询的join支持		字符串和数组
		union*		用于对查询的union支持		字符串、数组和对象
		view*		用于视图查询				字符串、数组
		distinct	用于查询的distinct支持		布尔值
		lock		用于数据库的锁机制			布尔值
		cache		用于查询缓存				支持多个参数
		relation*	用于关联查询				字符串
		with*		用于关联预载入				字符串、数组
		bind*		用于数据绑定操作			数组或多个参数
		comment		用于SQL注释	字符串
		force		用于数据集的强制索引		字符串
		master		用于设置主服务器读取数据	布尔值
		strict		用于设置是否严格检测字段名是否存在	布尔值
		sequence	用于设置Pgsql的自增序列名	字符串
		failException	用于设置没有查询到数据是否抛出异常	布尔值
		partition	用于设置分表信息			数组 字符串
		
		
		方法				说明
		count	统计数量，参数是要统计的字段名（可选）
		max		获取最大值，参数是要统计的字段名（必须）
		min		获取最小值，参数是要统计的字段名（必须）
		avg		获取平均值，参数是要统计的字段名（必须）
		sum		获取总分，参数是要统计的字段名（必须）	
		
#### 	高级查询
	快捷查询	
		在多个字段之间用|分割表示OR查询，用&分割表示AND查询，可以实现下面的查询
			->where('name|title','like','thinkphp%')
		快捷查询支持所有的查询表达式。
	区间查询	
		->where('name', ['like', '%thinkphp%'], ['like', '%kancloud%'], 'or')
		->where('id', ['>', 0], ['<>', 10], 'and')
	
	数组对象查询	
		$map = [
			'name'   => ['like', 'thinkphp%'],
			'title'  => ['like', '%think%'],
			'id'     => ['>', 10],
			'status' => 1,
		];
		$where          = new Where;
		$where['id']    = ['in', [1, 2, 3]];
		$where['title'] = ['like', '%php%'];
				
		Db::table('think_user')
			->where(new Where($map))
			->whereOr($where->enclose())
			->select();		
				
	使用Query对象查询			
		$query = new \think\db\Query;
		$query->where('id','>',0)
			->where('name','like','%thinkphp');		
		Db::table('think_user')
			->where($query)
			->select();		
						
	快捷方法			
			方法				作用
			whereOr			字段OR查询
			whereXor		字段XOR查询
			whereNull		查询字段是否为Null
			whereNotNull	查询字段是否不为Null
			whereIn			字段IN查询
			whereNotIn		字段NOT IN查询
			whereBetween	字段BETWEEN查询
			whereNotBetween	字段NOT BETWEEN查询
			whereLike		字段LIKE查询
			whereNotLike	字段NOT LIKE查询
			whereExists		EXISTS条件查询
			whereNotExists	NOT EXISTS条件查询
			whereExp		表达式查询
			whereColumn		比较两个字段	
				
	动态查询			
			动态查询			描述
		whereFieldName		查询某个字段的值
		whereOrFieldName	查询某个字段的值
		getByFieldName		根据某个字段查询
		getFieldByFieldName	根据某个字段获取某个值		
				
	原生查询
		query方法
			query方法用于执行SQL查询操作，如果数据非法或者查询错误则返回false，否则返回查询结果数据集（同select方法）。
			Db::query("select * from think_user where status=1");		
		execute方法		
			execute用于更新和写入数据的sql操作，如果数据非法或者查询错误则返回false，否则返回影响的记录数。	
			Db::execute("update think_user set name='thinkphp' where status=1");	
				
				
#### 事务操作
	最简单的方式是使用 transaction 方法操作数据库事务，当闭包中的代码发生异常会自动回滚
		Db::transaction(function () {
			Db::table('think_user')->find(1);
			Db::table('think_user')->delete(1);
		});		
	手动控制事务			
		Db::startTrans();		
		try {
			Db::table('think_user')->find(1);
			Db::table('think_user')->delete(1);
			// 提交事务
			Db::commit();
		} catch (\Exception $e) {
			// 回滚事务
			Db::rollback();
		}		
	
	SQL监听
	如果开启数据库的调试模式的话，你可以对数据库执行的任何SQL操作进行监听，使用如下方法：
		Db::listen(function ($sql, $time, $explain) {
			// 记录SQL
			echo $sql . ' [' . $time . 's]';
			// 查看性能分析结果
			dump($explain);
		});
		
	存储过程
		数据访问层支持存储过程调用
		$resultSet = Db::query('call procedure_name');
			foreach ($resultSet as $result) {   }

	数据集处理方法
		数据库查询得到的结果是数据集
			方法		  描述
			isEmpty		是否为空
			toArray		转换为数组
			all			所有数据
			merge		合并其它数据
			diff		比较数组，返回差集
			flip		交换数据中的键和值
			intersect	比较数组，返回交集
			keys		返回数据中的所有键名
			pop			删除数据中的最后一个元素
			shift		删除数据中的第一个元素
			unshift		在数据开头插入一个元素
			reduce		通过使用用户自定义函数，以字符串返回数组
			reverse		数据倒序重排
			chunk		数据分隔为多个数据块
			each		给数据的每个元素执行回调
			filter		用回调函数过滤数据中的元素
			column		返回数据中的指定列
			sort		对数据排序
			shuffle		将数据打乱
			slice		截取数据中的一部分


























			
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
		
		
		