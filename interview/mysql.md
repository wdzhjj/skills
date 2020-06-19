## mysql 

### mysql基础
		SELECT 
			column_1,column_2,...  (列)
		FROM
			table_1
		[INNER | LEFT | RIGHT] JOIN table_2 ON conditions
		WHERE
			conditions
		GROUP BY 
			column_1
		HAVING
			group_conditions
		ORDER BY
			column_1
		LIMIT offset,length
			
			
		SELECT * 使用星号(*)可能会返回不使用的列的数据。 它在MySQL数据库服务器和应用程序之间产生不必要的I/O磁盘和网络流量。
				 如果明确指定列，则结果集更可预测并且更易于管理。
				使用星号(*)可能会将敏感信息暴露给未经授权的用户。
		WHERE 子句中的运算符
				BETWEEN 选择在给定范围内的值
				LIKE 匹配基于模式匹配的值
				IN 指定值是否匹配列表中的任何值
				IS NULL 检查该值是否为 NULL
	
		*插入数据
		INSERT INTO TABLE(column_1,column_2...)
			VALUES (value1,value2,...);
		插入多行
			INSERT INTO TABLE(column_1,column_2...)
			VALUES (value1,value2,...),
				   (value1,value2,...),
	
		*更新数据
			UPDATE [LOW_PRIORITY] [IGNORE] table_name
			SET
				column_1 = expr1,
				column_2 = expr2,
				...
			WHERE
				condition;
				
			LOW_PRIORITY修饰符指示UPDATE语句延迟更新，直到没有从表中读取数据的连接。 
			LOW_PRIORITY对仅使用表级锁定的存储引擎(例如MyISAM，MERGE，MEMORY)生效。	
			即使发生错误，IGNORE修饰符也可以使UPDATE语句继续更新行。导致错误(如重复键冲突)的行不会更新。
		
		*删除数据
			DELETE FROM table_name
			WHERE condition;
			where子句是可选的，省略where，delete将删除表中所有行
	
		**创建删除数据库
			CREATE DATABASE [IF NOT EXISTS] database_name;
				IF NOT EXISTS 可选子句防止创建数据库服务器中已存在的数据库错误
			SHOW DATABASES 语句显示MYSQL数据库服务器中的所有数据库
			USE database_name 使用数据库
			
			DROP DATABASE [IF EXISTS] database_name;
				DROP DATABASE是要删除的数据库名称
				IF EXISTS是该语句的可选部分，以防止您删除数据库服务器中  不存在的数据库。
		**创建表
			CREATE TABLE [IF NOT EXISTS] table_name(
				column_list
			) engine=table_type
			column_list 为表定义列，语法为
			column_name data_type[size] [NOT NULL|NULL][DEFAULT value][AUTO_INCREMENT]
			指定主键
				PRIMARY KEY (col1,col2,...)  加在column_list中
		**修改表结构
			ALTER TABLE table_name action1[,action2,...]
			操作可以是添加新列，添加主键，重命名表等任何操作。ALTER TABLE语句允许在单个ALTER TABLE语句中应用多个操作，每个操作由逗号(，)分隔
			* 设置列的自动递增属性
				CHANGE COLUMN task_id task_id INT(11) NOT NULL AUTO_INCREMENT
			* 增加新列到表中
				ADD COLUMN complete DECIMAL(2,1) NULL
				AFTER description;
			* 从表中删除列
				DROP COLUMN description
			* 重命名表
				RENAME TO work_intems
				
#### 连接查询
		连接查询：将多张表（大于等于 2 张表）按照某个指定的条件进行数据的拼接，其最终结果记录数可能有变化，但字段数一定会增加。
			交叉连接：cross join，从一张表中循环取出每一条记录，每条记录都去另外一张表进行匹配，匹配的结果都保留（没有条件匹配），
				  而连接本身的字段会增加，最终形成的结果为笛卡尔积形式。
				  左表 cross join 右表;
			内连接：inner join，从左表中取出每一条记录，和右表中的所有记录进行匹配，并且仅当某个条件在左表和右表中的值相同时，
				    结果才会保留，否则不保留。	  
				    基本语法：左表 + [inner] + join + 右表 + on + 左表.字段 = 右表.字段;
			外连接
				外连接：left\right join，以某张表为主表，取出里面的所有记录，然后让主表中的每条记录都与另外一张表进行连接，不管能否匹配成功，其最终结果都会保留，匹配成功，则正确保留；匹配失败，则将另外一张表的字段都置为NULL.
				基本语法：左表 + left\right + join + 右表 + on + 左表.字段 = 右表.字段;			
				left join：左外连接（左连接），以左表为主表；
				right join：右外连接（右连接），以右表为主表。
			自然连接：
				nature join，自然连接其实就是自动匹配连接条件，系统以两表中同名字段作为匹配条件，如果两表有多个同名字段，那就都作为匹配条件。在这里，自然连接可以分为自然内连接和自然外连接。	

			
#### MYSQL聚合函数				
		cout()：统计分组后，每组的总记录数；
		max()：统计每组中的最大值；
		min()：统计每组中的最小值；
		avg()：统计每组中的平均值；
		sum()：统计每组中的数据总和。
		select sex,count(*),max(age),min(age),avg(age),sum(age) from student group by sex;
		count()函数里面可以使用两种参数
			1、 * 表示统计组内全部记录的数量
			2、 字段名表示统计对应字段非null记录的总数。 使用group by进行分组之后，展示的记录会根据分组的字段值进行排序，默认为升序

#### MYSQL 视图
		创建基本语法：create view + 视图名 + as + select语句;
		查询视图：desc+视图名
				  show tables+视图名
				  show create table+视图名
		使用视图：在操作数据库表的过程中，使用视图，主要就是为了查询，因此将视图当做表一样查询即可。
				  在这里需要注意的是，虽然我们说视图是一个虚拟表，它不保存数据，但是它却可以获取数据。	
		修改视图：alter view + 视图名 + as +新的select语句		  
		删除视图：drop view + 视图名		
		视图意义
			视图可以节省 SQL 语句，将一条复杂的查询语句用视图来进行封装，以后可以直接对视图进行操作；
			数据安全，视图操作主要是针对查询的，如果对视图结构进行处理，例如删除，并不会影响基表的数据；
			视图往往在大型项目中使用，而且是多系统使用，可以对外提供有用的数据，但是隐藏关键（或无用）的数据；
			视图是对外提供友好型的，不同的视图提供不同的数据，就如专门对外设计的一样；
			视图可以更好（或者说，容易）的进行权限控制。
		新增数据：多表视图不能新增数据
				  可以向单表视图新增数据，但视图中包含的字段必须有基表中所有不能为空的字段。
		删除数据：多表视图不能删除数据
				  单表视图可以删除数据
		更新数据：无论多表视图还是单表，都可以进行数据的更新		  
		
		视图算法：
			系统对视图以及外部查询视图的select语句的一种解析方式			
			undefined：未定义（默认的），这不是一种实际使用的算法，而是一个“推卸责任”的算法。在未定义的情况下，告诉系统，视图没有定义算法，请自己选择。
			temptable：临时表算法，系统先执行视图的select语句，后执行外部查询语句。
			merge：合并算法，系统先将视图对应的select语句与外部查询视图的select语句进行合并，然后再执行。此算法比较高效，且在未定义算法的时候，经常会默认选择此算法。
			基本语法：create + [algorithm = temptable/merge/undefined] + view + 视图名 + as + select语句;

#### 数据备份与还原			
		单表数据备份
			每次只能备份一张表，而且只能备份数据，不能备份表结构。
			select */字段列表 + into outfile + '文件存储路径' + from 数据源;
			前提导出的外部文件不存在，即文件存储路径下的文件不存在。
				如：select * into outfile 'D:/CoderLife/testMySQL/class.txt' from class;
			
			单表数据备份的高级操作			
				基本语法：select */字段列表 + into outfile + '文件存储路径' + fields + 字段处理 + lines + 行处理 + from 数据源;
				字段处理：
					enclosed by：指定字段用什么内容包裹，默认是，空字符串；
					terminated by：指定字段以什么结束，默认是\t，Tab键；
					escaped by：指定特殊符号用什么方式处理，默认是\\，反斜线转义。
				行处理：
					starting by：指定每行以什么开始，默认是，空字符串；
					terminated by：指定每行以什么结束，默认是\r\n，换行符。
			数据恢复
				基本语法：load data infile + '文件存储路径' + into table + 表名 + [字段列表] + fields + 字段处理 + lines + 行处理;
		
		SQL备份
			mysqldump.exe -hPup + 数据库名字 + [表名1 + [表名2]] > 备份文件目录
				h：IP或者localhost;
				P：端口号
				u：用户名
				p：密码
	
#### 事务
		1、开启事务	
			start transaction;
		2、提交事务
			commit;
		3、回滚事务
			rollback;
		回滚点：在某个操作成功完成之后，后续的操作有可能成功也有可能失败，但无论后续操作的结果如何，前一次操作都已经成功了，因此我们可以在当前成功的位置，
				设置一个操作点，其可以供后续操作返回该位置，而不是返回所有操作，这个点称之为回滚点。关于回滚点的基本语法为，
			设置回滚点：savepoint + 回滚点名称;
			返回回滚点：rollback to + 回滚点名称;
		自动事务:
			在 MySQL 中，默认的都是自动事务处理，即用户在操作完成之后，其操作结果会立即被同步到数据库中。
			开启自动事务处理：set autocommit = on / 1;
			关闭自动事务处理：set autocommit = off / 0;
#### 数据库变量
		系统变量
			show variables;
			查看具体变量：
				select + @@变量名 + [,@@变量名1,@@变量名2...];
			修改全局级别变量：
				set global 变量名 = 值；
		对话级别变量：
			仅对当前客户端当次连接有效
			修改：
				基本语法 1：set 变量名 = 值;
				基本语法 2：set @@变量名 = 值;
		
		自定义变量：
			set @变量名 = 值；
			查看自定义变量：
				select @变量名
			
### 触发器
		触发器：trigger，是指事先为某张表绑定一段代码，当表中的某些内容发生改变（增、删、改）的时候，
			    系统会自动触发代码并执行。
		触发器包含三个要素：
			事件类型：增删改。insert、delete、update
			触发时间：事件类型前和后，before和after
			触发对象：表中的每一条记录（行）
			每张表只能拥有一种触发时间的一种事件类型的触发器，即每张表最多可以拥有 6 种触发器。
			
		创建触发器：
			delimiter 自定义符号 -- 临时修改语句结束符，在后续语句中只有遇到自定义符号才会结束语句
			create trigger + 触发器名称 + 触发器时间 + 事件类型 on 表名 for each row
			begin -- 代表触发器内容开始
			-- 触发器内容主体，每行用分号结尾
			end -- 代表触发器内容结束
			自定义符号 -- 用于结束语句
			delimiter ; -- 恢复语句结束符
				例子
					（-- 创建触发器
					delimiter $$ -- 临时修改语句结束符
					create trigger after_order after insert on orders for each row
					begin -- 触发器内容开始
						-- 触发器内容主体，每行用分号结尾
						update goods set inventory = inventory - 1 where id = 1;
					end -- 触发器内容结束
					$$ -- 结束语句
					delimiter ; -- 恢复语句结束符）
		查询触发器：
			show triggers + [like 'pattern'];
			show triggers\G;  \G表示旋转
			show create trigger + 触发器名称； 查询创建触发器的语句
		删除触发器：
			drop trigger + 触发器名称
			
#### 代码执行结构
		* 顺序结构
		* 分支结构
		* 循环结构
		分支结构
			if 条件判断 then
				-- 满足条件时，要执行的代码
			else -- 可以没有 else 语句
				-- 不满足条件时，要执行的代码
			end if;
		循环结构
			while 条件判断 do
					--满足条件时 要执行的代码
					--变更循环条件
			end while	
				
		interate:迭代，类似于 continue，表示结束本次循环，不执行后续步骤，直接开始下一次循环
		leave：离开，类似于break，直接结束整个循环
			interate/leave + 循环名称。
				循环名称: while 条件判断 do
				-- 满足条件时要执行的代码
				-- 变更循环条件
				iterate/leave 循环名称; -- 控制循环语句
				end while;

#### 存储过程
		procedure 一种用来处理数据(增删改)的方式，可以理解为没有返回值的函数
		创建过程
			-- 基本语法
			create procedure 过程名([参数列表])
			begin
				--过程体
			end	
					(create procedure pro()
					select * from student;)
		查看过程
			show create procedure + 过程名
		调用过程
			call + 过程名
		修改\删除过程
			过程只能先删除后新增，不能修改
			drop procedure + 过程名
			
		过程函数		
			in，数据只是从过程外部传入给过程内部使用，可以是数值也可以是变量；
			out，此参数只能传递变量，且变量指向的数据需要先清空然后才能进入过程内部，该引用供过程内部使用，过程结束后可以将变量的值传递给过程外部使用；
			inout，此参数只能传递变量，该变量的值可以给过程内部使用，过程结束后可以变量的值传递给过程外部使用。
			=》procedure 过程名(in 参数名字 参数类型, out 参数名字 参数类型, inout 参数名字 参数类型)
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
### MYSQL 数据类型
#### 整数型
		tinyint:迷你整型，使用1个字节存储数据
		smallint:小整型，使用2个字节存储数据
		mediumint:中整型，使用三个字节存储数据
		int：标准整型，使用4个字节存储数据
		bigint：大整型，使用8个字节
#### 小数型
		带有小数点或者范围超出整型的数值类型
		浮点型
			float：单精度，占用4个字节存储数据，精度范围大约为七位左右
				直接用float，表示没有小数部分，如果用float(M,D)，其中M代表总长度，D代表小数部分长度，M-D则为整数部分长度
			double：双精度，占用8个字节存储数据，精度十五位左右
		定点型
			decimal
			定点型数据，绝对的保证整数部分不会被四舍五入，也就是说不会丢失精度，
			但小数部分有可能丢失精度，虽然理论上小数部分也不会丢失精度。
#### 日期时间型
		datetime:日期时间，格式为yyyy-MM-dd HH:mm:ss
		date:日期，datetime的date部分
		time：时间，或者说是时间段，为指定的某个时间区间之间，包含正负时间；
		timestamp：时间戳，但并不是真正意义上的时间戳，其是从1970年开始计算的，格式和datetime一致；
		year：年份，共有两种格式，分别为year(2)和year(4).
#### 字符串型
		char(L):L length 可以存储的长度，单位为字符，最大长度为 255
		varchar(L):L length 理论长度65536，但是会多出 1 到 2 个字节来确定存储的实际长度；
		varchar(10)：例如存储 10 个汉字，在 UTF8 环境下，需要 10*3+1=31 个字节。
	
		定长字符串对磁盘空间比较浪费，但是效率高：如果数据基本上确定长度都一样，就使用定长字符串，例如身份证、电话号码等；
		变长字符串对磁盘空间比较节省，但是效率低：如果数据不能确定长度（不同的数据有变化），就使用变长字符串，例如地址、姓名等。
#### 文本字符串
		text：存储文字
		blob：存储二进制数据，通常不用（实际上都是存储路径）
#### 枚举字符串
		enum（‘元素1’，‘元素2’...）
		存储的数据，只能是事先定义好的数据
#### 集合字符串
		set  和枚举类似，实际存储的是数值而不是字符串
		定义： set，元素列表
		使用：可以使用元素列表中的多个元素，用逗号分隔
		
#### 增加主键
		SQL操作中，有3种方法可以给表增加主键
		1、在创建表的时候，直接在字段之后，添加primary key关键字
			number char(10) primary key comment '学号'
		2、	在创建表的时候，在所有的字段之后，使用primary key(主键字段列表)来创建主键（如果有多个字段作为主键，则称之为复合主键）
			primary key(number,course)
		3、当表创建完之后，额外追加主键。可以直接追加主键，也可以通过修改表字段的属性追加主键
			alter table my_pri3 add primary key(course);
		更新、删除主键
			对于主键，没有办法直接更新，主键必须先删除，然后才能更新
			alter table + 表名 + drop primary key;
#### 唯一键
		增加唯一键的三种方法
		1、创建表时，字段后面直接添加 unique或者unique key关键字
		2、在所有字段之后，增加unique key(字段列表)，可以设置复合唯一键
		3、在创建表之后，增加唯一键  
			alter table my_unique3 add unique key(number);
		唯一键与主键本质相同，区别在于：唯一键允许字段值为空，并且允许多个空值存在。
		
#### 索引
		索引：系统根据某种算法，将已有的数据（未来可能新增的数据），单独建立一个文件，这个文件能够实现快速匹配数据，
			  并且能够快速的找到对应的记录，几乎所有的索引都是建立在字段之上的。
			MySQL 中提供了多种索引，包括：

				主键索引primary key
				唯一键索引unique key
				全文索引fulltext index
				普通索引index
		索引的意义：
			提升查询数据的效率；
			约束数据的有效性。
		但是增加索引是有前提条件的，这是因为索引本身会产生索引文件（有的时候可能会比数据本身都大），因此非常耗费磁盘空间。
		如果某个字段需要作为查询的条件经常使用，可以使用索引；
		如果某个字段需要进行数据的有效性约束，也可以使用索引（主键或唯一键）。

### 范式
		Normal Farmat是为了解决数据的存储和优化问题	
		1NF
			第一范式：在设计表存储数据的时候，如果表中设计的字段存储的数据，在取出来使用之前还需要额外的处理（拆分），那么表的设计就不满足第一范式，
			第一范式要求字段的数据具有原子性，不可再分。
		2NF
			第二范式：在数据表的设计过程中，如果有复合主键（多字段主键），且表中有字段并不是由整个主键来确定，而是依赖复合主键中的某个字段（主键的部分），
			也就是说存在字段依赖主键的部分的问题（称之为部分依赖），第二范式就是要解决表设计中不允许出现部分依赖。
		3NF
			第三范式：需要满足第一范式和第二范式，理论上讲，每张表中的所有字段都应该直接依赖主键（逻辑主键，代表是业务主键），如果表设计中存在一个字段，
			并不直接依赖主键，而是通过某个非主键字段依赖，最终实现主键依赖（把这种不是直接依赖主键，而是依赖非主键字段的依赖关系，称之为传递依赖），
			第三范式就是要解决表设计中出现传递依赖的问题。
		逆规范化
			在某些特定的环境中（例如淘宝数据库），在设计表的时候，如果一张表中有几个字段是需要从另外的表中去获取数据，理论上讲，
			的确可以获得想要的数据，但是相对来说，其效率低会一点。此时为了提高查询效率，咱们会刻意的在某些表中，不去保存另外一张表的主键（逻辑主键），
			而是直接保存想要存储的数据信息，这样的话，在查询数据的时候，这张表就可以直接提供咱们想要的数据，而不需要多表查询，但是这样做会导致数据冗余。
			实际上，逆规范化是磁盘利用率和效率之间的对抗。
		
### 蠕虫复制
		从已有的数据表中获取数据，然后将数据进行新增操作
		根据已有表创建新表=》复制表结构
			create table + 表名 + like + [数据库名.]表名;
		蠕虫复制的步骤为：先查出数据，然后将查出的数据新增一遍。
		基本语法：insert into + 表名 + [()] + select + 字段列表/* + from + 表名;
			如  insert into my_copy select * from my_collate_bin;
			
		
		
				

	
	
	
	
### MYSQL常用进阶
	
	
#### 查看mysql数据库及编码格式
		1、查看数据库编码格式
			show variables like 'character_set_database';
		2、查看数据表的编码格式
			show create table table_name;
		3、创建数据库时指定数据库的字符集
			create database dbname character set utf8;
		4、创建数据表时指定数据表的编码格式
			create table table_name(
				name varchar(45) not null,
				price double not null
			)default charset = utf8;
		5、修改数据库的编码格式
			alter database dbname character set utf8;
		6、修改数据表格编码格式
			alter table table_name character set utf8;
		7、修改字段编码格式
			alter table <表名> change <字段名> <字段名> <类型> character
		8、添加外键
			alter table 表名 add constraint 外键名 foreign key 字段名 REFERENCES 外表表名 字段名
		9、删除外键
			alter table 表名 drop foreign key 外键名
	

#### mysqldump备份数据库
		只导出表结构 不导出数据
			mysqldump --opt -d dname -uroot -p >xxx.sql
		备份数据库
			mysqldump dname > bakname
			mysqldump -A -uroot -p dname > bakname;
			mysqldump -d -A --add-drop-table -uroot -p >bakname.sql
		导出数据不导出结构
			mysqldump -t dbname -uroot -p > xxx.sql
		导出数据和表结构
			mysqldump 数据库名 -uroot -p >xxx.sql
		导出特定表结构
			mysqldump -uroot -p -B 数据库名 --table 表名 > xxx.sql
			
#### mysql查看当前数据库
		1、select database();
		2、show tables;   =>会显示 table_in_ ...
		3、status         =>current database
		
#### Truncate
		Truncate Table 用来删除表中的所有行,而不记录单个行操作。
		TRUNCATE TABLE 比DELETE速度更快，使用的系统资源和事务日志资源更少
		当不需要该表时，用drop；保留表，删除所有记录，使用truncate；当你要删除部分记录时,用 delete.
		不可对以下表使用TRUNCATE
			1、用FOREIGN KEY 约束引用的表
			2、参与索引视图的表
			3、通过使用事务复制或合并复制发布的表
			4、TRUNCATE TABLE 不能激活触发器，因为该操作不记录各个行删除
					

					
					
### Mysql 权限	
		grant all privileges on *.* to jack@'localhost' identified by 'jack' with grant option
		grant命令
			all privileges 表示所有权限，也可用select、update
			on 指定权限针对哪些库和表
			*.* 前*用来指定数据库名 后*指定表名
			to 将权限赋予某个用户
			jack@'localhost' jack用户 @后接限制的主机，可以是ip、ip段、域名、%  %表示任何地方
			identified by 指定用户的登录密码
			with grant option	表示此用户可以将拥有的权限授权给别人
			
			flush privileges 刷新权限 使权限生效
			show grants 查看权限
			show grants for 'jack'@'%'; 查看某个用户
			revoke delete on*.* from jack'@'localhost  回收权限
			drop user 'jack'@'localhost'  删除用户
			rename user 'jack'@'%' to 'jim'@'%'  对账户重命名
			
			
			
			
			
			
			
			
			
			
		









		
			
		